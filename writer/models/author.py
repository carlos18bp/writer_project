from django.db import models

class Author(models.Model):
    """
    Author model.

    :ivar first_name: first name author.
    :vartype first_name: str
    :ivar last_name: last name author.
    :vartype last_name: str
    :ivar email: email author.
    :vartype email: str
    :ivar contact: contact author.
    :vartype contact: str
    :ivar second_contact: second contact author.
    :vartype second_contact: str
    :ivar address: address author.
    :vartype address: str
    """

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, null=True)
    contact = models.CharField(max_length=40)
    second_contact = models.CharField(max_length=40, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)

def __str__(self):
    return self.first_name