from django.shortcuts import render
# Create your views here.
def learndj(request):
    return render(request,'course/info.html')