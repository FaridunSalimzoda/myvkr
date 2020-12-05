from .models import kursu, addtopic
from django.forms import ModelForm, TextInput, Textarea, Select


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
        fields = ['title', 'task', 'kursu_ptr']

        # fields['kursu_prt'] = pk

        widgets = {
            'title': TextInput(attrs={
                'class': 'form_class',
                'placeholder': 'Название темы'
            }),
            'task': Textarea(attrs={
                'class': 'form_class',
                'placeholder': 'Описание темы'
            }),
            'kursu_ptr': Select(attrs={
                'class': 'form_class',
                'placeholder': 'Название курса'
            }),
        }