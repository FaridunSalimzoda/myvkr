from .models import CoueseTable,TopicTable, QuestionsTable, AnswerTable
from django.forms import ModelForm, TextInput, Textarea, Select


class kursuform(ModelForm):
    class Meta:
        model = CoueseTable
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
        model = TopicTable
        fields = ['title', 'task', 'id_course']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form_class',
                'placeholder': 'Название темы'
            }),
            'task': Textarea(attrs={
                'class': 'form_class',
                'placeholder': 'Описание темы'
            }),
            'id_course': Select(attrs={
                'class': 'form_class',
                'placeholder': 'Название курса'
            }),
        }

class QuestionsForm(ModelForm):
    class Meta:
        model = QuestionsTable
        fields = ['text']
        widgets = {
            'text': Textarea(attrs={
                'id': 'message',
                'placeholder': 'Добавьте вопрос'
            })
        }

class AnswerForm(ModelForm):
    class Meta:
        model = AnswerTable
        fields = ['text_answer']
        widgets = {
            'text-answer': TextInput(attrs={
                'id': 'message',
                'placeholder': 'Добавьте ответ'
            })
        }