# django-verified-email-field
Simple model and form field to get verified email

Renders two input fields: `e-mail` and `verification code`.
The verification code is send to the e-mail address using AJAX or during field's `clean`,
if there is no valid code for given e-mail, so it works even without javascript.
For the javascript to work properly You need to have [jQuery](https://code.jquery.com/) included in Your page.

All the texts and email templates may be configured in `settings` and overidden by field's keyword arguments.
(See [settings.py](verified_email_field/settings.py) and [fieldsetup.py](verified_email_field/fieldsetup.py) for more information)

## Installation

```bash
pip install django-verified-email-field
```

## Configuration

 1. add  `'verified_email_field'` to Your `settings.INSTALLED_APPS`
 1. include `verified_email_field.urls` in your project's urls.py using namespace `'verified-email-field'`:
```python
from django.conf.urls import url, include

urlpatterns = [
    ...
    url(r'^verified-email-field/', include('verified_email_field.urls')),
    ...
]
```

## Usage

Use `VerifiedEmailField` in Your forms:
```python
from django import forms
from verified_email_field.forms import VerifiedEmailField

class RegistrationForm(forms.ModelForm):
    email = VerifiedEmailField(label='email', fieldsetup_id='registration-form-email', required=True)
```

Or in Your models:
```python
from django.db import models
from verified_email_field.models import VerifiedEmailField

class User(models.Model):
    email = VerifiedEmailField('e-mail', fieldsetup_id='user-email')
```

Ensure that `form.media.js` (`{{ form.media.js }}`) is being rendered in your template
and [jQuery](https://code.jquery.com/) is included in Your page.
