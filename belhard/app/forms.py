from django.forms import Form, IntegerField, ModelForm, EmailInput, TextInput, Textarea

from .models import Contact


class CalculateForm(Form):
    width = IntegerField(min_value=1)
    height = IntegerField(min_value=1)


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
        widgets = {
            'name': TextInput(
                attrs={
                   'type': 'text',
                    'name': 'name',
                    'class': 'form-control',
                    'id': 'name',
                    'placeholder': 'Ваше имя',
                    'required': True
                }
            ),
        'email': EmailInput(
            attrs={
                'type': 'email',
                'class': 'form-control',
                'name': 'email',
                'id': 'email',
                'placeholder': 'Ваша почта',
                'required': True
            }
        ),
        'message': Textarea(
            attrs={
                'class': 'form-control',
                'name': 'message',
                'rows': '5',
                'placeholder': 'Сообщение',
                'required': True
            }
        )
    }
