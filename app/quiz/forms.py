from django import forms
from django.forms.widgets import RadioSelect
from django.forms import ModelForm, TextInput, Textarea, Select, CharField, CheckboxInput
from  .models import Quiz


class QuestionForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        choice_list = [x for x in question.get_answers_list()]
        self.fields["answers"] = forms.ChoiceField(choices=choice_list, widget=RadioSelect)


class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'description', 'category', 'random_order', 'max_questions', 'answers_at_end',
                  'exam_paper', 'pass_mark','single_attempt', 'fail_text', 'draft', 'success_text', 'url']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form_class',
                }),
            'description': Textarea(attrs={
                'class': 'form_class',

            }),
            'category': Select(attrs={
                'class': 'form_class',

            }),
               'random_order': CheckboxInput(attrs={

               }),

                  'max_questions': TextInput(attrs={
                      'class': 'form_class'
                  }),
                  'answers_at_end': CheckboxInput(attrs={}),
                'exam_paper': CheckboxInput(attrs={}),
                  'single_attempt': CheckboxInput(attrs={
                      'class': 'form_class',
                      'placeholder': 'Пользователю будет разрешена только одна попытка'
                  }),
                  'pass_mark': TextInput(attrs={}),
                'success_text': TextInput(attrs={'class': 'form_class'}),
                'fail_text': TextInput(attrs={'class': 'form_class'}),
                'draft': CheckboxInput(attrs={}),
                'url': TextInput(attrs={})
        }