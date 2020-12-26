from django.shortcuts import render,redirect
from .models import TestTable, QuestionsTable, AnswerTable, ExamTable, ResultsTable
from .form import QuestionsForm, AnswerForm, TestForm
from django.views.generic import UpdateView,DeleteView
from cours.models import TopicTable

def test_home(request):
    ku = TestTable.objects.order_by('id')
    return render(request, 'testing/test_home.html', {'ku': ku})


def addtest(request):
    error = ''
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addtest')
        else:
            error = 'error'
    form = TestForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'testing/addtest.html', data)

def test_dateil(request, pk):
    ku = list(TopicTable.objects.filter(id=pk).values())
    test = TestTable.objects.filter(id_topic=pk)
    return render(request, 'testing/test_detail.html', {'post': ku[0], 'test': test, 'pk': pk})

class TestUpdateView(UpdateView):
    model = TestTable
    template_name = 'testing/test_update.html'
    form_class = TestForm

class TestDeleteView(DeleteView):
    model = TestTable
    success_url = '/testing/'
    template_name = 'testing/test_delete.html'

def addQuestions(request, pk: any):
    error = ''
    if request.method == 'POST':
        form = QuestionsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kurs')
        else:
            error = 'error'
    form = QuestionsForm()
    date = {
        'form': form,
        'error': error,
        'pk': pk
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