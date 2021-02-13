from django.shortcuts import render

# Create your views here.
def index(request):
    data = {
        'title': 'Гланая страница'
    }
    return render(request, 'main/index.html', data)



def addtest(request):

    return render(request, 'main/addtest.html')
