from django.shortcuts import render
# Create your views here.
def feesdj(request):
    return render(request,'fees/info.html')