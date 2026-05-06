from django import forms
from django.core.exceptions import ValidationError
from .models import Contact, Job


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'phone_number']
        labels = {
            'name': 'Nombres y Apellidos',
            'email': 'Correo de contacto',
            'phone_number': 'numero telefónico',
            'subject': 'Pequeña descripción',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    # 'placeholder':'Ingrese el nombre del autor'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': ' form-control',
                }
            ),
            'phone_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    # 'placeholder': 'Ingrese una nacionalidad para el autor'
                }
            ),
            'subject': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    # 'placeholder': 'Ingrese una pequeña descripcion para el autor'
                }
            )
        }


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['name_applicant', 'email_applicant', 'subject_applicant',
                  'phone_number_applicant', 'file']
        labels = {
            'name_applicant': 'Nombres',
            'email_applicant': 'Correo de contacto',
            'subject_applicant': 'Pequeña descripción',
            'phone_number_applicant': 'numero telefónico',
            'file': 'Curriculum',
        }
        widgets = {
            'name_applicant': forms.TextInput(
                attrs={
                    'title': 'Nombres y apellidos',
                    'class': 'form-control bg-white opacity-50 rounded-0',
                    # 'placeholder':'Ingrese el nombre del autor'
                }
            ),
            'email_applicant': forms.EmailInput(
                attrs={

                    'class': 'form-control bg-white opacity-50 rounded-0',
                }
            ),
            'phone_number_applicant': forms.TextInput(
                attrs={

                    'class': 'form-control bg-white opacity-50 rounded-0',

                }
            ),
            'subject_applicant': forms.TextInput(
                attrs={
                    'class': 'form-control bg-white opacity-50 rounded-0',

                }
            ),
            'file': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Archivos en formato PDF',
                }
            )
        }
