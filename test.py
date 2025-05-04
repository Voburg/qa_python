import pytest

from main import BooksCollector

class TestBooksCollector:
# Тесты для add_new_book
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_two_identical_books(self, collector):

        collector.add_new_book('Друзья')
        collector.add_new_book('Друзья')

        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize("book_name, expected_result", {
        ("Гарри Поттер", True), ("", False), ("большесорокасимволовбольшесорокасимволовЙ", False)
    })
    def test_add_new_book(self, collector, book_name, expected_result):
        collector.add_new_book(book_name)
        assert book_name in collector.books_genre if expected_result else book_name not in collector.books_genre

# Тесты для set_book_genre
    @pytest.mark.parametrize("book_name, genre, expected_result", {
        ("Гарри Поттер", "Фантастика", "Фантастика"), ("Пролетая над гнездом кукушки", "Детективы", "Детективы")
    })
    def test_set_book_genre(self, collector, book_name, genre, expected_result):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == expected_result

# Тесты для get_book_genre
    def test_get_book_genre_direct(self, collector):
        collector.books_genre["Туарег"] = "Детективы"
        assert collector.get_book_genre("Туарег") == "Детективы"

# Тесты для get_books_with_specific_genre
    def test_get_books_with_specific_genre_with_books(self, collector):
        collector.add_new_book("Марсианин")
        collector.set_book_genre("Марсианин", "Фантастика")
        collector.add_new_book("Землянин")
        collector.set_book_genre("Землянин", "Фантастика")
        assert collector.get_books_with_specific_genre("Фантастика") == ["Марсианин","Землянин"]

# Тесты для get_books_genre
    def test_get_books_genre_with_books(self, collector):
        collector.add_new_book("Марсианин")
        collector.set_book_genre("Марсианин", "Фантастика")
        collector.add_new_book("Полиция")
        collector.set_book_genre("Полиция", "Детективы")
        assert collector.get_books_genre() == {"Марсианин": "Фантастика", "Полиция": "Детективы"}

# Тесты для get_books_for_children
    def test_get_books_for_children(self, collector):
        collector.add_new_book("Чебурашка")
        collector.add_new_book("Полиция")
        collector.set_book_genre("Чебурашка", "Мультфильмы")
        collector.set_book_genre("Полиция", "Детективы")
        result = collector.get_books_for_children()
        assert "Чебурашка" in result
        assert "Полиция" not in result

# Тесты для add_book_in_favorites
    def test_add_book_in_favorites_add_two_books(self, collector):
        collector.add_new_book("Чебурашка")
        collector.add_new_book("Игрок")
        collector.add_book_in_favorites("Чебурашка")
        collector.add_book_in_favorites("Игрок")
        assert len(collector.get_list_of_favorites_books()) == 2

# Тесты для delete_book_from_favorites
    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book("Чебурашка")
        collector.add_book_in_favorites("Чебурашка")
        collector.delete_book_from_favorites("Чебурашка")
        assert collector.get_list_of_favorites_books() == []

# Тесты для get_list_of_favorites_books
    def test_get_list_of_favorites_books_(self, collector):
        collector.add_new_book("Цветы для Элджернона")
        collector.add_book_in_favorites("Цветы для Элджернона")
        assert collector.get_list_of_favorites_books() == ["Цветы для Элджернона"]