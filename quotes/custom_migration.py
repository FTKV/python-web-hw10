from datetime import datetime
import os

import django
from mongoengine import connect, Document, StringField, ListField, ReferenceField, CASCADE


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quotes.settings")
django.setup()


import quotes_app.models


client_mongo = connect(
    host=f"mongodb+srv://mongo_user:vLrVCAba9af1aNrm@cluster-zero.w7uymdt.mongodb.net/python_web_hw09_01", ssl=True
)


class Author(Document):
    fullname = StringField(required=True, max_length=150)
    born_date = StringField(max_length=150)
    born_location = StringField(max_length=150)
    description = StringField(max_length=10000)
    meta = {"allow_inheritance": True, "collection": "authors"}


class Quote(Document):
    quote = StringField(required=True)
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=50))
    meta = {"allow_inheritance": True, "collection": "quotes"}


if __name__ == '__main__':
    authors_in_mongo = Author.objects.all()
    quotes_in_mongo = Quote.objects.all()

    for author_in_mongo in authors_in_mongo:
        author = quotes_app.models.Author()
        author.fullname = author_in_mongo.fullname
        author.born_date = datetime.strptime(author_in_mongo.born_date, "%B %d, %Y")
        author.born_location = author_in_mongo.born_location
        author.description = author_in_mongo.description
        author.save()

    for quote_in_mongo in quotes_in_mongo:
        quote = quotes_app.models.Quote()
        quote.quote = quote_in_mongo.quote
        quote.author = quotes_app.models.Author.objects.filter(fullname=quote_in_mongo.author.fullname).first()
        quote.save()
        
        for tag_in_mongo in quote_in_mongo.tags:
            tag = quotes_app.models.Tag()
            tag.title = tag_in_mongo
            if not quote.tags.filter(title=tag_in_mongo):
                if not quotes_app.models.Tag.objects.filter(title=tag_in_mongo):
                    tag.save()
                tag = quotes_app.models.Tag.objects.filter(title=tag_in_mongo).first()
                quote.tags.add(tag)

    print("Done")
