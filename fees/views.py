from django.shortcuts import render
# Create your views here.
def fees_dj(request):
    return render(request,'fees/info.html')