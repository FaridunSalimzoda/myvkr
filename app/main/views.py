from django.shortcuts import render

# Create your views here.
def index(request):
    data = {
        'title': 'Гланая страница'
    }
    return render(request, 'main/index.html', data)

def adt(request):

    return render(request, 'main/test_home.html')

def addtest(request):

    return render(request, 'main/addtest.html')
