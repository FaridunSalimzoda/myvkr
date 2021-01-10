from django.shortcuts import render, redirect, get_object_or_404
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
    ans = AnswerTable.objects.filter(id_question=kk)
    return render(request, 'testing/quest_deteil.html', {'ans': ans, 'pk': pk, 'kk': kk})

def answer_detele(request, pk, kk, tt):
    ans =  list(AnswerTable.objects.filter(id=tt).values())
    return render(request, 'testing/answer_detele.html', {'ans': ans, 'pk': pk, 'kk': kk, 'tt': tt})


class AnswerUpdateView(UpdateView):
    model = AnswerTable
    template_name = 'testing/answer_update.html'
    form_class = AnswerForm

    def get_object(self, *args, **kwargs):
        question = get_object_or_404(AnswerTable, id_question=self.kwargs['kk'], id=self.kwargs['tt'])
        return question

class AnswerDeleteView(DeleteView):
    model = AnswerTable
    template_name = 'testing/answer_delete.html'
    success_url = '/testing/'

    def get_object(self, *args, **kwargs):
        question = get_object_or_404(AnswerTable, id_question=self.kwargs['kk'], id=self.kwargs['tt'])
        return question

class QuestionsUpdateView(UpdateView):
    model = QuestionsTable
    template_name = 'testing/quest_update.html'
    form_class  = QuestionsForm

    def get_object(self, *args, **kwargs):
        question = get_object_or_404(QuestionsTable, id_test=self.kwargs['pk'], id=self.kwargs['kk'])
        return question

class QuestionsDeleteView(DeleteView):
    model = QuestionsTable
    template_name = 'testing/quest_delete.html'
    success_url = '/testing/'

    def get_object(self, *args, **kwargs):
        question = get_object_or_404(QuestionsTable, id_test=self.kwargs['pk'], id=self.kwargs['kk'])
        return question


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

def addAnswer(request, pk: any):
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
        'error': error,
        'pk': pk
    }
    return render(request,'testing/add_answer.html', dat)

