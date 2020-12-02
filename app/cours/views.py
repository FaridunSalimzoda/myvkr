from django.shortcuts import render, redirect
from .models import kursu, addtopic
from .form import kursuform, topicform
from django.views.generic import DetailView, UpdateView, DeleteView


def cour(request):
    ku = kursu.objects.order_by('id')
    return render(request, 'cours/cours_home.html', {'ku': ku})


def detail(request, pk):
    ku = list(kursu.objects.filter(id=pk).values())
    top = addtopic.objects.order_by('id')
    return render(request, 'cours/datail.html', {'post': ku[0], 'top': top, 'pk': pk})

def topic_dateil(request, pk, kk):
    top = list(addtopic.objects.filter(id=kk).values())
    ku = list(kursu.objects.filter(id=pk).values())
    return render(request, 'cours/topic.html', {'top': top[0], 'pk': pk, 'kk': kk})
# class kursDetailView(DetailView):
#    model = kursu
#     template_name = 'cours/datail.html'
#     context_object_name = 'post'


class kursUpdateView(UpdateView):
    model = kursu
    template_name = 'cours/update.html'

    form_class = kursuform


class kursDeleteView(DeleteView):
    model = kursu
    success_url = '/course/'
    template_name = 'cours/cours_delete.html'


def newtopic(request, pk: any):
    error = ''
    if request.method == 'POST':
        form = topicform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kurs')
        else:
            error = 'error'
    form = topicform()
    data = {
        'form': form,
        'error': error
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
