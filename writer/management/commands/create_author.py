import os
from faker import Faker
from django.core.files import File
from django.core.management.base import BaseCommand
from writer.models import Author

class Command(BaseCommand):
    help = 'Create author records in the database'

    def add_arguments(self, parser):
        parser.add_argument('number_of_authors', type=int, nargs='?', default=1)

    def handle(self, *args, **options):
        fake = Faker()
        
        new_author = Author.objects.create(
            first_name = fake.first_name(),
            last_name = fake.last_name(),
            email = fake.email(),
            contact = fake.random_int(min=3000000000, max=3030000000),
            second_contact = fake.random_int(min=3000000000, max=3030000000),
            address = fake.street_address(),
        )

        image_path = os.getcwd() + '/media/temp/author_temp1.jpg'
        name_file = image_path.split("/")[-1]
        with open(image_path, 'rb') as file:
            new_author.image.save(name_file, File(file), save=True)

        self.stdout.write(self.style.SUCCESS(f'Author "{new_author}" created'))
        
        print(f'"{len(Author.objects.all())}" author records created')