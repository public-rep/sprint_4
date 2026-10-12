import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_initial_state(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')

        assert collector.get_books_genre() == {'Гарри Поттер': ''}
        assert collector.get_list_of_favorites_books() == []

    def test_add_new_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')

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

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Властелин колец')

        assert collector.get_books_genre() == {
            'Гарри Поттер': '',
            'Властелин колец': ''
        }

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')

        collector.set_book_genre('Гарри Поттер', 'Фантастика')

        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

    def test_set_book_genre_rejects_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')

        collector.set_book_genre('Гарри Поттер', 'Роман')

        assert collector.get_book_genre('Гарри Поттер') == ''

    def test_set_book_genre_for_nonexistent_book(self):
        collector = BooksCollector()

        collector.set_book_genre('Несуществующая книга', 'Фантастика')

        assert collector.get_book_genre('Несуществующая книга') is None

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')

        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

    def test_get_book_genre_for_book_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')

        assert collector.get_book_genre('Гарри Поттер') == ''

    def test_get_book_genre_for_nonexistent_book(self):
        collector = BooksCollector()

        assert collector.get_book_genre('Несуществующая книга') is None

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

    def test_get_books_with_nonexistent_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.set_book_genre('Книга 1', 'Фантастика')

        assert collector.get_books_with_specific_genre('Роман') == []

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Книга для детей')
        collector.add_new_book('Мультфильм')
        collector.add_new_book('Книга ужасов')
        collector.add_new_book('Книга без жанра')

        collector.set_book_genre('Книга для детей', 'Фантастика')
        collector.set_book_genre('Мультфильм', 'Мультфильмы')
        collector.set_book_genre('Книга ужасов', 'Ужасы')

        assert collector.get_books_for_children() == [
            'Книга для детей',
            'Мультфильм'
        ]

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')

        collector.add_book_in_favorites('Гарри Поттер')

        assert collector.get_list_of_favorites_books() == ['Гарри Поттер']

    def test_add_book_in_favorites_does_not_add_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')

        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')

        assert collector.get_list_of_favorites_books() == ['Гарри Поттер']

    def test_add_nonexistent_book_to_favorites(self):
        collector = BooksCollector()

        collector.add_book_in_favorites('Несуществующая книга')

        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')

        collector.delete_book_from_favorites('Гарри Поттер')

        assert collector.get_list_of_favorites_books() == []

    def test_delete_nonexistent_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')

        collector.delete_book_from_favorites('Несуществующая книга')

        assert collector.get_list_of_favorites_books() == ['Гарри Поттер']

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