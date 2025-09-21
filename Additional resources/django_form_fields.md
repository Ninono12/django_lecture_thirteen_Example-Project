# Django Form Fields 🧾

A quick reference of commonly used Django form fields, with simple examples and short descriptions.

---

### `CharField`

Text input for short strings.

```python
name = forms.CharField(max_length=100)
```

---

### `EmailField`

Validates that the input is a valid email address.

```python
email = forms.EmailField()
```

---

### `BooleanField`

Checkbox input (True/False).

```python
subscribe = forms.BooleanField(required=False)
```

---

### `ChoiceField`

Dropdown menu with predefined options.

```python
role = forms.ChoiceField(choices=[('admin', 'Admin'), ('user', 'User')])
```

---

### `MultipleChoiceField`

Allows selecting multiple options.

```python
interests = forms.MultipleChoiceField(
    choices=[('coding', 'Coding'), ('music', 'Music')],
    widget=forms.CheckboxSelectMultiple
)
```

---

### `IntegerField`

Accepts only whole numbers.

```python
age = forms.IntegerField()
```

---

### `FloatField`

Accepts decimal numbers.

```python
rating = forms.FloatField()
```

---

### `DecimalField`

High-precision decimal input.

```python
price = forms.DecimalField(max_digits=5, decimal_places=2)
```

---

### `DateField`

Accepts a date input.

```python
birth_date = forms.DateField()
```

---

### `DateTimeField`

Accepts both date and time.

```python
appointment = forms.DateTimeField()
```

---

### `TimeField`

Accepts only a time value.

```python
meeting_time = forms.TimeField()
```

---

### `URLField`

Validates a URL string.

```python
website = forms.URLField()
```

---

### `SlugField`

For slugs (URL-friendly text).

```python
slug = forms.SlugField()
```

---

### `FileField`

For file uploads.

```python
resume = forms.FileField()
```

---

### `ImageField`

For image file uploads.

```python
photo = forms.ImageField()
```
