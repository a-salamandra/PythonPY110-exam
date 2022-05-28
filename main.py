import random
import json
from faker import Faker

from conf import MODEL

fake_data = Faker("ru_RU")


def generate_title() -> str:
    books = []
    with open("books.txt", encoding="utf-8") as f:
        for title in f.readlines():
            books.append(title.strip())
    return random.choice(books)


def generate_year() -> int:
    return random.randint(1600, 2022)


def generate_pages() -> int:
    return random.randint(16, 3000)


def generate_isbn13() -> str:
    return fake_data.isbn13()


def generate_rating() -> float:
    return round(random.uniform(0, 5), 2)


def generate_price() -> float:
    return round(random.uniform(200, 6000), 2)


def generate_author() -> list:
    authors = []
    for _ in range(random.randint(1, 3)):
        authors.append(fake_data.name())
    return authors


def generate_book(count_:int = 1) -> dict:
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
    books = []
    gen_b = generate_book(pk)
    for i in range(number_of_books):
        books.append(next(gen_b))
    return books


if __name__ == '__main__':
    with open("books.json", "w", encoding="utf-8") as output_file:
        json.dump(generate_books(100), output_file, ensure_ascii=False, indent=2)
