from django.db import models

class Book(models.Model):
    """
    Book model.

    :ivar title: title book.
    :vartype title: str
    :ivar description: description book.
    :vartype description: str
    :ivar image: image by book.
    :vartype image: Image
    """

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='book_images/', null=True, blank=True)

    def __str__(self):
        return self.title