from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_one_book_twice_book_added_once(self):
        collector = BooksCollector()

        collector.add_new_book("Джейн Эйр")
        collector.add_new_book("Джейн Эйр")

        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_name_length_more_than_40_no_book_added(self):
        collector = BooksCollector()

        collector.add_new_book("Название книги длиной тут более 40 символов, такая добавиться не должна")

        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_genre_dont_exist_no_genre_set(self):
        collector = BooksCollector()
        collector.add_new_book("Джейн Эйр")

        collector.set_book_genre("Джейн Эйр", "Роман")

        assert collector.books_genre["Джейн Эйр"] == ""

    def test_get_book_genre_book_without_genre_result_empty(self):
        collector = BooksCollector()
        collector.add_new_book("Джейн Эйр")

        assert collector.get_book_genre("Джейн Эйр") == ""

    @pytest.mark.parametrize("genre", ['Ужасы', 'Фантастика'])
    def test_get_books_with_specific_genre_genre_from_list_result_book(self, genre):
        collector = BooksCollector()
        collector.add_new_book("Кладбище домашних животных")
        collector.set_book_genre("Кладбище домашних животных", "Ужасы")
        collector.add_new_book("Дюна")
        collector.set_book_genre("Дюна", "Фантастика")

        assert collector.get_books_with_specific_genre(genre) is not None

    def test_get_books_genre_no_books_empty_dictionary(self):
        collector = BooksCollector()

        assert collector.get_books_genre() == {}

    def test_get_books_for_children_age_rating_books_only_result_empty(self):
        collector = BooksCollector()

        collector.add_new_book("Кладбище домашних животных")
        collector.set_book_genre("Кладбище домашних животных", "Ужасы")
        collector.add_new_book("Убийство в Восточном Экспрессе")
        collector.set_book_genre("Убийство в Восточном Экспрессе", "Детективы")

        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_two_books_two_books_added(self):
        collector = BooksCollector()

        collector.add_new_book("Кладбище домашних животных")
        collector.set_book_genre("Кладбище домашних животных", "Ужасы")
        collector.add_new_book("Дюна")
        collector.set_book_genre("Дюна", "Фантастика")

        collector.add_book_in_favorites("Кладбище домашних животных")
        collector.add_book_in_favorites("Дюна")

        assert len(collector.get_list_of_favorites_books()) == 2

    def test_delete_book_from_favorites_book_not_favorite_no_books_removed(self):
        collector = BooksCollector()

        collector.add_new_book("Кладбище домашних животных")
        collector.set_book_genre("Кладбище домашних животных", "Ужасы")
        collector.add_new_book("Дюна")
        collector.set_book_genre("Дюна", "Фантастика")

        collector.add_book_in_favorites("Дюна")
        collector.delete_book_from_favorites("Кладбище домашних животных")

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_get_list_of_favorites_books_one_favorite_book_result_one(self):
        collector = BooksCollector()

        collector.add_new_book("Кладбище домашних животных")
        collector.set_book_genre("Кладбище домашних животных", "Ужасы")
        collector.add_new_book("Дюна")
        collector.set_book_genre("Дюна", "Фантастика")

        collector.add_book_in_favorites("Дюна")

        assert len(collector.get_list_of_favorites_books()) == 1

















