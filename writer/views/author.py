from django.http import JsonResponse
from writer.serializers.author_serializer import author_serializer
from writer.models import Author

def index(request):
    """
    Index view to return a JSON author serialized reponse.

    :param request: Django object request.
    :type request: django.http.HttpRequest

    :return: JSON author serialized reponse.
    :rtype: django.http.JsonResponse
    """
    author = Author.objects.all().order_by('-id')

    return JsonResponse(author_serializer(author), safe=False)