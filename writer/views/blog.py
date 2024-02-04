from django.http import JsonResponse
from writer.serializers.blog_serializer import blog_serializer
from writer.models import Blog

def index(request):
    """
    Index view to return a JSON blogs serialized reponse.

    :param request: Django object request.
    :type request: django.http.HttpRequest

    :return: JSON blogs serialized reponse.
    :rtype: django.http.JsonResponse
    """
    blogs = Blog.objects.all().order_by('-id')

    return JsonResponse(blog_serializer(blogs), safe=False)