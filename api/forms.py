from django import forms
from .models import Post
from django.core.exceptions import ValidationError
# import RPi.GPIO as GPIO
# from mfrc522 import SimpleMFRC522


class StudentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['first_name', 'surname', 'patronymic', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Максим'}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Окулов'}),
            'patronymic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Вадимович'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@gmail.com'}),
        }

    def save(self):
        id = '1231111111231111'
        # r = SimpleMFRC522()
        # id, data = r.read()
        new_student = Post.objects.create(
            first_name=self.cleaned_data['first_name'],
            surname=self.cleaned_data['surname'],
            patronymic=self.cleaned_data['patronymic'],
            email=self.cleaned_data['email'],
            slug=id
        )
        return new_student