import random
import json
from faker import Faker

from conf import MODEL

fake_data = Faker("ru_RU")


def generate_title() -> str:
    """Chooses a random book title from a text file"""
    books = []
    with open("books.txt", encoding="utf-8") as f:
        for title in f.readlines():
            books.append(title.strip())
    return random.choice(books)


def generate_year() -> int:
    """Creates a random year"""
    return random.randint(1600, 2022)


def generate_pages() -> int:
    """Creates a random number of pages"""
    return random.randint(16, 3000)


def generate_isbn13() -> str:
    """Generates a random isbn13 number with Faker"""
    return fake_data.isbn13()


def generate_rating() -> float:
    """Generates a random rating"""
    return round(random.uniform(0, 5), 2)


def generate_price() -> float:
    """Generates a random price"""
    return round(random.uniform(200, 6000), 2)


def generate_author() -> list:
    """Returns a list with 1-3 author names using Faker"""
    authors = []
    for _ in range(random.randint(1, 3)):
        authors.append(fake_data.name())
    return authors


def generate_book(count_:int = 1) -> dict:
    """Generates fake book information while keeping track of how many times this function's been called"""
    while True:
        book = {
            "model": MODEL,
            "pk": count_,
            "fields": {
                "title": generate_title(),
                "year": generate_year(),
                "pages": generate_pages(),
                "isbn13": generate_isbn13(),
                "rating": generate_rating(),
                "price": generate_price(),
                "author": generate_author()
            }
        }
        yield book
        count_ += 1


def generate_books(number_of_books: int, pk: int = 1) -> list:
    """Returns a list of fake books"""
    books = []
    gen_b = generate_book(pk)
    for i in range(number_of_books):
        books.append(next(gen_b))
    return books


if __name__ == '__main__':
    with open("books.json", "w", encoding="utf-8") as output_file:
        json.dump(generate_books(100), output_file, ensure_ascii=False, indent=2)
