# **Django Forms: Comprehensive Guide (Classic Forms)**


## **1. Introduction to Django Forms**
Django forms handle HTML form creation, validation, and processing. They help:
- Generate HTML form fields
- Validate submitted data
- Clean and sanitize input
- Display errors automatically

---

## **2. Creating a Basic Form**
### **Define a Form in `forms.py`**
```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Your Name", 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="Email Address",
        help_text="Enter a valid email address."
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4}),
        required=True
    )
    subscribe = forms.BooleanField(
        label="Subscribe to newsletter",
        required=False,
        initial=True
    )
```

### **Key Components:**
| Component | Description | Example |
|-----------|-------------|---------|
| **Field Types** | Defines input type (`CharField`, `EmailField`, etc.) | `forms.CharField()` |
| **Widgets** | Controls HTML rendering | `forms.Textarea()` |
| **Labels** | Custom field labels | `label="Your Name"` |
| **Help Text** | Additional guidance | `help_text="Enter a valid email"` |
| **Validation** | Built-in & custom checks | `required=True` |

---

## **3. Rendering Forms in Templates**
### **Automatic Rendering**
```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}  <!-- Renders as paragraphs -->
    {{ form.as_table }}  <!-- Renders as table rows -->
    {{ form.as_ul }}  <!-- Renders as list items -->
    <button type="submit">Submit</button>
</form>
```

### **Manual Rendering (More Control)**
```html
<form method="post">
    {% csrf_token %}
    
    <div class="form-group">
        {{ form.name.label_tag }}
        {{ form.name }}
        {% if form.name.errors %}
            <div class="error">{{ form.name.errors }}</div>
        {% endif %}
    </div>
    
    <div class="form-group">
        {{ form.email.label_tag }}
        {{ form.email }}
        <small class="help-text">{{ form.email.help_text }}</small>
    </div>
    
    <button type="submit">Submit</button>
</form>
```

---

## **4. Processing Forms in Views**
### **Basic Form Handling in `views.py`**
```python
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process data (e.g., send email, save to DB)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            # Redirect after success
            return redirect('success-page')
    else:
        form = ContactForm()  # Empty form for GET requests
    
    return render(request, 'contact.html', {'form': form})
```

### **Key Methods:**
| Method | Purpose |
|--------|---------|
| `form.is_valid()` | Checks if data passes validation |
| `form.cleaned_data` | Access validated data (e.g., `form.cleaned_data['email']`) |
| `form.errors` | Returns validation errors |

---

## **5. Form Validation**
### **Built-in Validators**
```python
from django.core.validators import validate_email, MinLengthValidator

class SignupForm(forms.Form):
    email = forms.EmailField(validators=[validate_email])
    password = forms.CharField(
        validators=[MinLengthValidator(8)],
        widget=forms.PasswordInput
    )
```

### **Custom Validation**
```python
def clean_username(self):
    username = self.cleaned_data['username']
    if User.objects.filter(username=username).exists():
        raise forms.ValidationError("Username already taken!")
    return username

def clean(self):
    cleaned_data = super().clean()
    password = cleaned_data.get('password')
    confirm_password = cleaned_data.get('confirm_password')
    
    if password != confirm_password:
        raise forms.ValidationError("Passwords do not match!")
```

---

## **6. Common Form Fields & Widgets**
### **Field Types**
| Field | Description | Example |
|-------|-------------|---------|
| `CharField` | Text input | `forms.CharField(max_length=100)` |
| `EmailField` | Email validation | `forms.EmailField()` |
| `BooleanField` | Checkbox | `forms.BooleanField(required=False)` |
| `ChoiceField` | Dropdown select | `forms.ChoiceField(choices=[('A', 'Option A'), ('B', 'Option B')])` |
| `DateField` | Date picker | `forms.DateField(widget=forms.SelectDateWidget)` |

### **Widgets (Control HTML Rendering)**
```python
message = forms.CharField(
    widget=forms.Textarea(attrs={
        'rows': 4,
        'class': 'form-control',
        'placeholder': 'Enter your message...'
    })
)
```

---

## **7. Best Practices**
1. **Always use `{% csrf_token %}`** for security.
2. **Separate forms** into `forms.py` (not in views).
3. **Use `required=False`** for optional fields.
4. **Customize widgets** for better UX (e.g., date pickers).
5. **Sanitize input** before processing.

---

## **8. Example: Complete Contact Form**
### **forms.py**
```python
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    attachment = forms.FileField(required=False)
```

### **contact.html**
```html
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Send</button>
</form>
```

### **views.py**
```python
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            # Process data (e.g., send email)
            return redirect('thank-you')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
```

---

## **Conclusion**
Django forms simplify:
✅ HTML generation  
✅ Data validation  
✅ Security (CSRF, sanitization)  
✅ Error handling  
