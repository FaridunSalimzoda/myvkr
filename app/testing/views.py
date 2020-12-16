from django.shortcuts import render

# Create your views here.

def test_home(request):
    return render(request, 'testing/test_home.html')


def addtest(request):

    return render(request, 'testing/addtest.html')
