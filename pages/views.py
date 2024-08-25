from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def home(request):
        return render(request, 'pages/home.html')
def index(request):
        n={'name':'tasneem','age':'2888888888888888888888883'}
        return render(request,'pages/index.html',n)
       # return HttpResponse("Hello, world!")

def about(request):
        #return HttpResponse('about page')
        return render(request,'pages/about.html')