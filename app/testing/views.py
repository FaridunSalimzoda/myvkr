from django.shortcuts import render
from .models import TestTable, QuestionsTable, AnswerTable, ExamTable, ResultsTable
from .form import QuestionsForm, AnswerForm


def test_home(request):
    return render(request, 'testing/test_home.html')


def addtest(request):

    return render(request, 'testing/addtest.html')


def addQuestions(request):
    error = ''
    if request.method == 'POST':
        form = QuestionsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'error'
    form = QuestionsForm()
    date = {
        'form': form,
        'error': error
    }
    return render(request, 'testing/addtest.html', date)

def addAnswer(request):
    error = ''
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error: 'error'
    form = AnswerForm()
    dat = {
        'form': form,
        'error': error
    }
    return render(request,'testing/addtest.html', dat )