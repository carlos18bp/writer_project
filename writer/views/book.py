from django.http import JsonResponse
from writer.serializers.book_serializer import book_serializer
from writer.models import Book

def index(request):
    """
    Index view to return a JSON books serialized reponse.

    :param request: Django object request.
    :type request: django.http.HttpRequest

    :return: JSON books serialized reponse.
    :rtype: django.http.JsonResponse
    """
    books = Book.objects.all().order_by('-id')

    return JsonResponse(book_serializer(books), safe=False)