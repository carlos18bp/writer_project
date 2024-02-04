from django.core.management.base import BaseCommand
from writer.models import Author, Blog, Book

class Command(BaseCommand):
    help = 'Create rake records in the database'

    """
    To delete fake data via console, run:
    python3 manage.py delete_fake_data
    """
    def handle(self, *args, **options):
        Author.objects.all().delete()
        Blog.objects.all().delete()
        Book.objects.all().delete()