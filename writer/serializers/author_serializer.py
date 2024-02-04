import json

def author_serializer(author):
    """
    Author serializer.
    """

    author_data = {
        'id': author.id,
        'first_name': author.first_name,
        'last_name': author.last_name,
        'email': author.email,
        'contact': author.contact,
        'second_contact': author.second_contact,
        'address': author.address
    }

    return json.dumps(author_data)