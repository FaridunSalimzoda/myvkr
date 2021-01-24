from .models import QuestionsTable, AnswerTable, TestTable, ResultsTable
from django.forms import ModelForm, TextInput, Textarea, Select, TimeInput, IntegerField, CheckboxInput

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
        fields = ['id_test','text', 'number', 'ball']
        widgets = {
            'id_test': Select(attrs={
                'class': 'form_class',
                'placeholder': 'Название теста'}),
            'text': Textarea(attrs={
                'id': 'message',
                'placeholder': 'Добавьте вопрос'
            }),
            'number': TextInput(attrs={
                'id': 'message',
                'placeholder': 'Добавьте номер вопроса'
            }),
            'ball': TextInput(attrs={
                'id': 'message',
                'placeholder': 'Добавьте оценку за вопрос'
            })

        }

class AnswerForm(ModelForm):
    class Meta:
        model = AnswerTable
        fields = ['text_answer', 'try_answer', 'id_question']
        widgets = {
            'text_answer': TextInput(attrs={
                'id': 'message',
                'placeholder': 'Добавьте ответ'
            }),
            'try_answer': CheckboxInput(attrs={
                'placeholder': 'Правильный ответ'
            }),
            ' id_question': Select(attrs={
                'class': 'form_class',
                'placeholder': 'Название теста'}),
        }

class UserTestForm(ModelForm):
    class Meta:
        model = ResultsTable
        fields = ['estimation', 'timer']
        widgets = {
            'estimation': TextInput(attrs={
                'id': 'message',
                'placeholder': 'Добавьте ответ'}),
            'timer': TimeInput,
        }
