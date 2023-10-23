import re

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from .models import Author, Tag, Quote
from .forms import AuthorForm, TagForm, QuoteForm

# Create your views here.
def main(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes_app/index.html', {"quotes": quotes})


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.born_location = "in " + re.sub("^in ", "", author.born_location, flags=re.IGNORECASE)
            author.added_by = request.user
            author.save()
            return redirect(to='quotes_app:main')
        else:
            return render(request, 'quotes_app/author.html', {'form': form})

    return render(request, 'quotes_app/author.html', {'form': AuthorForm()})


@login_required
def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.added_by = request.user
            tag.save()
            return redirect(to='quotes_app:main')
        else:
            return render(request, 'quotes_app/tag.html', {'form': form})

    return render(request, 'quotes_app/tag.html', {'form': TagForm()})


@login_required
def add_quote(request):
    authors = Author.objects.all()
    tags = Tag.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save(commit=False)
            print(request.POST)
            new_quote.author = Author.objects.filter(fullname=request.POST.getlist('authors')[0]).first()
            new_quote.added_by = request.user
            new_quote.save()
            choice_tags = Tag.objects.filter(title__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)

            return redirect(to='quotes_app:main')
        else:
            return render(request, 'quotes_app/quote.html', {"authors": authors, "tags": tags, 'form': form})

    return render(request, 'quotes_app/quote.html', {"authors": authors, "tags": tags, 'form': QuoteForm()})


def author_info(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'quotes_app/author_info.html', {'author': author})