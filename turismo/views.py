from django.shortcuts import render

# Create your views here.


def turismo(request):
    return render(request, 'turismo/turismo.html')


def brasil(request):
    return render(request, 'turismo/brasil.html')


def italia(request):
    return render(request, 'turismo/italia.html')


def alemanha(request):
    return render(request, 'turismo/alemanha.html')
