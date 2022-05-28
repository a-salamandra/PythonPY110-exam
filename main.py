from faker import Faker
import random
import json
fake_data = Faker("ru_RU")

from conf import MODEL

def generate_title():
    books = []
    with open("books.txt", encoding="utf-8") as f:
        for title in f.readlines():
            books.append(title.strip())
    return random.choice(books)

def generate_year():
    return random.randint(1600,2022)

def generate_pages():
    return random.randint(16, 3000)

def generate_isbn13():
    return fake_data.isbn13()

def generate_rating():
    return round(random.uniform(0, 5),2)

def generate_price():
    return round(random.uniform(200,6000),2)

def generate_author():
    authors = []
    for _ in range (random.randint(1,3)):
        authors.append(fake_data.name())
    return authors

def generate_book(count_= 1):
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



if __name__ == '__main__':

    books = []
    gen = generate_book(1)
    for _ in range(100):
        books.append(next(gen))

    with open ("books.json", "w",encoding="utf-8") as output_file:
        json.dump(books,output_file, ensure_ascii=False,indent=2)



