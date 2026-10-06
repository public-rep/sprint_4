import pytest

from main import BooksCollector

class TestBooksCollector:


 def test_initial_state(self):
    collector = BooksCollector()

    assert collector.get_books_genre() == {}
    assert collector.get_list_of_favorites_books() == []

 def test_add_new_book(self):
    collector = BooksCollector()

    collector.add_new_book('Гарри Поттер')

    assert collector.get_books_genre() == {'Гарри Поттер': ''}
    assert collector.get_book_genre('Гарри Поттер') == ''

 @pytest.mark.parametrize('book_name', ['', 'А' * 41])
 def test_add_new_book_rejects_invalid_names(self, book_name):
    collector = BooksCollector()

    collector.add_new_book(book_name)

    assert book_name not in collector.get_books_genre()

 def test_add_new_book_does_not_add_duplicate(self):
    collector = BooksCollector()

    collector.add_new_book('Гарри Поттер')
    collector.add_new_book('Гарри Поттер')

    assert len(collector.get_books_genre()) == 1

 @pytest.mark.parametrize(
    'book_name, genre, expected',
    [
        ('Гарри Поттер', 'Фантастика', 'Фантастика'),
        ('Гарри Поттер', 'Роман', ''),
        ('Несуществующая книга', 'Фантастика', None),
    ]
)
 def test_set_and_get_book_genre(self, book_name, genre, expected):
    collector = BooksCollector()

    collector.add_new_book('Гарри Поттер')
    collector.set_book_genre(book_name, genre)

    assert collector.get_book_genre(book_name) == expected

 def test_get_books_with_specific_genre(self):
    collector = BooksCollector()

    collector.add_new_book('Книга 1')
    collector.add_new_book('Книга 2')
    collector.add_new_book('Книга 3')

    collector.set_book_genre('Книга 1', 'Фантастика')
    collector.set_book_genre('Книга 2', 'Фантастика')
    collector.set_book_genre('Книга 3', 'Ужасы')

    assert collector.get_books_with_specific_genre('Фантастика') == [
        'Книга 1',
        'Книга 2'
    ]

    assert collector.get_books_with_specific_genre('Роман') == []

 def test_get_books_for_children(self):
    collector = BooksCollector()

    collector.add_new_book('Фантастика')
    collector.add_new_book('Мультфильм')
    collector.add_new_book('Ужасы')
    collector.add_new_book('Без жанра')

    collector.set_book_genre('Фантастика', 'Фантастика')
    collector.set_book_genre('Мультфильм', 'Мультфильмы')
    collector.set_book_genre('Ужасы', 'Ужасы')

    assert collector.get_books_for_children() == [
        'Фантастика',
        'Мультфильм'
    ]

 def test_add_book_to_favorites(self):
    collector = BooksCollector()

    collector.add_new_book('Гарри Поттер')

    collector.add_book_in_favorites('Гарри Поттер')
    collector.add_book_in_favorites('Гарри Поттер')
    collector.add_book_in_favorites('Несуществующая книга')

    assert collector.get_list_of_favorites_books() == ['Гарри Поттер']

 def test_delete_book_from_favorites(self):
    collector = BooksCollector()

    collector.add_new_book('Гарри Поттер')
    collector.add_new_book('Книга 2')

    collector.add_book_in_favorites('Гарри Поттер')
    collector.add_book_in_favorites('Книга 2')

    collector.delete_book_from_favorites('Гарри Поттер')
    collector.delete_book_from_favorites('Несуществующая книга')

    assert collector.get_list_of_favorites_books() == ['Книга 2']

 def test_get_list_of_favorites_books(self):
    collector = BooksCollector()

    collector.add_new_book('Книга 1')
    collector.add_new_book('Книга 2')

    collector.add_book_in_favorites('Книга 1')
    collector.add_book_in_favorites('Книга 2')

    assert collector.get_list_of_favorites_books() == [
        'Книга 1',
        'Книга 2'
    ]
