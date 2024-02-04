import json

def book_serializer(books):
    """
    Book serializer.
    """
    books_serialized = []

    for book in books:
        book_data = {
            'id': book.id,
            'title': book.title,
            'description': book.description,
            'image_url': book.image.url,
        }
        books_serialized.append(book_data)

    return json.dumps(books_serialized)