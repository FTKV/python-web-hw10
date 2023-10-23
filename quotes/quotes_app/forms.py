from django.forms import ModelForm, CharField, DateField, TextInput, DateInput, Textarea

from .models import Author, Tag, Quote


class DateInput(DateInput):
    input_type = 'date'


class AuthorForm(ModelForm):

    fullname = CharField(min_length=2, max_length=150, required=True, widget=TextInput())
    born_date = DateField(required=True, widget=DateInput())
    born_location = CharField(min_length=2, max_length=150, required=True, widget=TextInput())
    description = CharField(min_length=10, max_length=10000, required=True, widget=Textarea())

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class TagForm(ModelForm):

    title = CharField(min_length=1, max_length=50, required=True, widget=TextInput())
    
    class Meta:
        model = Tag
        fields = ['title']


class QuoteForm(ModelForm):

    quote = CharField(min_length=5, max_length=1000, required=True, widget=Textarea())

    class Meta:
        model = Quote
        fields = ['quote']
        exclude = ['author', 'tags']
