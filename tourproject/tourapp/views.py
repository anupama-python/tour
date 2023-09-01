from django.http import HttpResponse
from django.shortcuts import render
from .models import Place,persons


#Create your views here.
def demo(request):
   obj=Place.objects.all()
   return render(request,"index.html",{'result':obj})

def demo1(request):
   obj=persons.objects.all()
   return render(request,"index.html",{'result':obj})
#def about(request):
 #   return render(request,"about.html")

#def home(request):
 #   return render(request,"home.html")
#def contact(request):
 #   return HttpResponse("contact")
#def thanks(request):
   # return HttpResponse("Thanks")
#def detail(request):
#    return HttpResponse("detail")
#def addition(request):
   # x=int(request.GET['num1'])
    #y=int(request.GET['num2'])
    #add=x+y
    #mul=x*y
    #div=x/y
    #sub=x-y


  #  return render(request,"result.html",{'result':add,'result1':mul,'result2':div,'result3':sub})
