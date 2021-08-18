from django.shortcuts import render

 

# Create your views here.
def app2_bye(request):
    return render(request,'app2_bye.html')
