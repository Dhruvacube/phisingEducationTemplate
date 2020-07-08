from django.shortcuts import render

# Create your views here.
def indexmain(request):
    return render(request, "indexmain.html")
