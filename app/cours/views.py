from django.shortcuts import render, redirect
from .models import CoueseTable, TopicTable, AssignedCoursesTable, RolesTable , TestTable, QuestionsTable, AnswerTable, ExamTable, ResultsTable
from .form import kursuform, topicform, QuestionsForm, AnswerForm
from django.views.generic import DetailView, UpdateView, DeleteView


def cour(request):
    ku = CoueseTable.objects.order_by('id')
    return render(request, 'cours/cours_home.html', {'ku': ku})


def detail(request, pk):
    ku = list(CoueseTable.objects.filter(id=pk).values())
    top = TopicTable.objects.filter(id_course=pk)
    return render(request, 'cours/datail.html', {'post': ku[0], 'top': top, 'pk': pk})

def topic_dateil(request, pk, kk):
    top = TopicTable.objects.filter(id_course=pk)
    ku = list(CoueseTable.objects.filter(id=pk).values())
    return render(request, 'cours/topic.html', {'top': top[0], 'pk': pk, 'kk': kk})
# class kursDetailView(DetailView):
#    model = kursu
#     template_name = 'cours/datail.html'
#     context_object_name = 'post'


class kursUpdateView(UpdateView):
    model = CoueseTable
    template_name = 'cours/update.html'

    form_class = kursuform

class topicUpdateView(UpdateView):
    model = TopicTable
    template_name = 'cours/update_topic.html'

    form_class = topicform

class kursDeleteView(DeleteView):
    model = CoueseTable
    success_url = '/course/'
    template_name = 'cours/cours_delete.html'

class topicDeleteView(DeleteView):
    model = TopicTable
    success_url = '/course/'
    template_name = 'cours/delete_topic.html'


def newtopic(request, pk: any):
    error = ''
    if request.method == 'POST':
        form = topicform(request.POST)
        if form.is_valid():
            # form['kursu'] = kursu.objects.filter(id=pk)
            form.save()
            return redirect('kurs')
        else:
            error = 'error'
    form = topicform()
    # form['kursu'] = kursu.objects.filter(id=pk)
    data = {
        'form': form,
        'error': error,
        'pk': pk
    }
    return render(request, 'cours/addTopic.html', data)


def adk(request):
    error = ''
    if request.method == 'POST':
        form = kursuform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ho')
        else:
            error = 'error'
    form = kursuform()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'cours/addKurs.html', data)

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