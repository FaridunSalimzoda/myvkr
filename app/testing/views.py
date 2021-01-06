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
            return redirect('test_home')
        else:
            error = 'error'
    form = TestForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'testing/addtest.html', data)

def test_dateil(request, pk):
    #test = list(TestTable.objects.filter(id=pk).values())
    #quest = QuestionsTable.objects.filter(id_test=pk)
    ku = list(TestTable.objects.filter(id=pk).values())
    top = QuestionsTable.objects.filter(id_test=pk)
    return render(request, 'testing/test_detail.html', {'post': ku[0], 'top': top, 'pk': pk})

def question_deteil(request, pk, kk):
    qi = list(QuestionsTable.objects.filter(id=pk).values())
    ans = AnswerTable.objects.filter(id_test=pk)
    return render(request, 'cours/deteil.html', {'ans': ans[0], 'pk': pk, 'kk': kk})


class TestUpdateView(UpdateView):
    model = TestTable
    template_name = 'testing/update_test.html'
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
    return render(request, 'testing/add_quest.html', date)

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
    return render(request,'testing/addtest.html', dat)