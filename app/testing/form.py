from .models import QuestionsTable, AnswerTable
from django.forms import ModelForm, TextInput, Textarea, Select


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


