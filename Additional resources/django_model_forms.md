# Django Model Forms 📄

Django Model Forms provide a powerful way to automatically create forms based on your database models.

## ✅ What is a ModelForm?

A **ModelForm** is a helper class that lets you create a Django form based on a model. It automatically generates form fields that correspond to the model fields.

## 🧱 Basic Usage

```python
# models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
```

```python
# forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']
```

## 💾 Using the Form in Views

```python
# views.py
from django.shortcuts import render, redirect
from .forms import BookForm

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})
```

## 🧩 Customize Fields

You can customize widgets, labels, or add extra fields:

```python
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        labels = {
            'title': 'Book Title',
        }
        widgets = {
            'published_date': forms.SelectDateWidget(),
        }
```

## 🧪 Validating Data

Add custom validation logic with `clean()` or `clean_<field>()` methods:

```python
def clean_title(self):
    title = self.cleaned_data.get('title')
    if "django" not in title.lower():
        raise forms.ValidationError("Title must contain the word 'Django'.")
    return title
```

## 🌐 Templates Example

```html
<!-- add_book.html -->
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Add Book</button>
</form>
```

