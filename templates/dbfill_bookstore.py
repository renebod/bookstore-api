from bookstore.models import *

authors = ["Harper Lee", "Jane Austen", "George Orwell", "J.D. Salinger", \
           "F. Scott Fitzgerald", "Emily Brontë", "Charlotte Brontë", \
           "Ray Bradbury", "William Golding"]

books = [{"title": "To Kill a Mockingbird", "author": "Harper Lee"}, \
         {"title": "Pride and Prejudice", "author": "Jane Austen"}, \
         {"title": "1984", "author": "George Orwell"}, \
         {"title": "The Catcher in the Rye", "author": "J.D. Salinger"}, \
         {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}, \
         {"title": "Wuthering Heights", "author": "Emily Brontë"}, \
         {"title": "Jane Eyre", "author": "Charlotte Brontë"}, \
         {"title": "Fahrenheit 451", "author": "Ray Bradbury"}, \
         {"title": "Lord of the Flies", "author": "William Golding"}, \
         {"title": "Persuasion", "author": "Jane Austen"}]


def run():
    for a in authors:
        Author.objects.get_or_create(name=a)

    for b in books:
        Book.objects.get_or_create(title=b['title'], \
                                   author=Author.objects.get(name=b['author']))

    print("Imported %s books, by %s authors" % (len(Book.objects.all()),\
                                                len(Author.objects.all())))
