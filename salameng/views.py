from django.shortcuts import render


def index(request):
    return render(request, 'salameng/index.html', context={})


def test_view():
    pass
