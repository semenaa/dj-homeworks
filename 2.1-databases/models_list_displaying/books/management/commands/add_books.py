from django.core.management.base import BaseCommand, CommandError
from books.models import Book
import json

class Command(BaseCommand):
    help = 'Adds books to the database'

    def handle(self, *args, **options):
        with open('fixtures/books.json', encoding='utf') as f:
            loaded_books = json.load(f)
            for book in loaded_books:
                b = Book(
                    id=book['pk'],
                    name=book['fields']['name'],
                    author=book['fields']['author'],
                    pub_date=book['fields']['pub_date']
                )
                b.save()


