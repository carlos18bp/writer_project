import os
from faker import Faker
from django.core.files import File
from django.core.management.base import BaseCommand
from writer.models import Book

class Command(BaseCommand):
    help = 'Create Book records in the database'

    def add_arguments(self, parser):
        parser.add_argument('number_of_books', type=int, nargs='?', default=10)

    def handle(self, *args, **options):
        number_of_books = options['number_of_books']
        fake = Faker()  

        for _ in range(number_of_books):
            new_book = Book.objects.create(
                title = fake.word(),
                description  = fake.text(max_nb_chars=300),
            )

            image_path = os.getcwd() + '/media/temp/book_temp1.jpg'
            name_file = image_path.split("/")[-1]
            with open(image_path, 'rb') as file:
                new_book.image.save(name_file, File(file), save=True)

            self.stdout.write(self.style.SUCCESS(f'Book "{new_book}" created'))
        
        print(f'"{len(Book.objects.all())}" Book records created')