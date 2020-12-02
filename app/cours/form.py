from .models import kursu, addtopic
from django.forms import ModelForm, TextInput, Textarea


class kursuform(ModelForm):
    class Meta:
        model = kursu
        fields = ['title', 'task', 'teache']

        widgets = {
            'title': TextInput(attrs={
                'class': '',
                'placeholder': 'Название курса'
            }),
            'task': Textarea(attrs={
                'class': '',
                'placeholder': 'Описание курса'
            }),
            'teache': TextInput(attrs={
                'class': '',
                'placeholder': 'Преподаватель'
            })
        }


class topicform(ModelForm):
    class Meta:
        model = addtopic
        fields = ['title']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form_class',
                'placeholder': 'Название темы'
            })
        }