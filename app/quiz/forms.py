from django import forms
from django.forms.widgets import RadioSelect
from django.forms import ModelForm, TextInput, Textarea, Select, CharField
from  .models import Quiz


class QuestionForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        choice_list = [x for x in question.get_answers_list()]
        self.fields["answers"] = forms.ChoiceField(choices=choice_list, widget=RadioSelect)


class QuizForm(forms.Form):
    class Meta:
        model = Quiz
        fields = ['title', 'description', 'category', 'random_order', 'max_questions', 'answers_at_end'
                            'exam_paper', 'single_attempt', 'pass_mark', 'success_text', 'fail_text', 'draft']
        widgets = {
            'title': TextInput(attrs={
                'class': '',
                'placeholder': 'Название курса'
            }),
            'description': Textarea(attrs={
                'class': '',
                'placeholder': 'Описание курса'
            }),
            'category': Select(attrs={
                'class': 'form_class',
                'placeholder': 'Название курса'
            }),


        }