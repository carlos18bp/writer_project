import json

def blog_serializer(blogs):
    """
    Blog serializer.
    """
    blogs_serialized = []

    for blog in blogs:
        blog_data = {
            'id': blog.id,
            'title': blog.title,
            'description': blog.description,
            'image_url': blog.image.url,
        }
        blogs_serialized.append(blog_data)

    return json.dumps(blogs_serialized)