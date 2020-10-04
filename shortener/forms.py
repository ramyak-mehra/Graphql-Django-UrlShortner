
from django import forms
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField
from django.core.exceptions import ValidationError
from captcha.widgets import ReCaptchaV3
from .models import URL
from shorty.settings import WEBSITE_NAME


class CreateLinkForm(forms.ModelForm):

    def clean(self):
        full_url = self.cleaned_data.get('full_url')
        if URL.objects.filter(full_url=full_url).exists():
            raise ValidationError("raise an error")
        return self.cleaned_data

    captcha = ReCaptchaField(
        label='',
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.85,
            }
        )
    )

    class Meta:
        model = URL
        fields = ['full_url', 'captcha']
