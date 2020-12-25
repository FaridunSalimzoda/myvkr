from .models import QuestionsTable, AnswerTable, TestTable
from django.forms import ModelForm, TextInput, Textarea, Select, TimeInput

class TestForm(ModelForm):
    class Meta:
        model = TestTable
        fields = ['test_name', 'time', 'id_topic']
        widgets = {
            'test_name': TextInput(attrs={
                'class': 'form_class',
                'placeholder': 'Название теста'
            }),
            'time': TextInput(attrs={
                'class': 'form_class',
                'placeholder': 'Время прохождения'
            }),
            'id_topic': Select(attrs={
                'class': 'form_class',
                'placeholder': 'Название темы'
            })
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


