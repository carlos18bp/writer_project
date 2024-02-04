import os
from faker import Faker
from django.core.files import File
from django.core.management.base import BaseCommand
from writer.models import Blog

class Command(BaseCommand):
    help = 'Create Blog records in the database'

    def add_arguments(self, parser):
        parser.add_argument('number_of_blogs', type=int, nargs='?', default=10)

    def handle(self, *args, **options):
        number_of_blogs = options['number_of_blogs']
        fake = Faker()  

        for _ in range(number_of_blogs):
            new_blog = Blog.objects.create(
                title = fake.word(),
                description  = fake.text(max_nb_chars=300),
            )

            image_path = os.getcwd() + '/media/temp/blog_temp1.jpg'
            name_file = image_path.split("/")[-1]
            with open(image_path, 'rb') as file:
                new_blog.image.save(name_file, File(file), save=True)

            self.stdout.write(self.style.SUCCESS(f'Blog "{new_blog}" created'))
        
        print(f'"{len(Blog.objects.all())}" Blog records created')