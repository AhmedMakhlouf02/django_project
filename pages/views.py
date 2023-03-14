from django.shortcuts import render
from django.http import HttpResponse
#from .models import Login
from .forms import LoginForm
# Create your views here.


def index(request):
    x = {'name':'ahmed',
         'age':19552684174,
         }
    return render(request, 'pages/index.html',x )

def about(request):
    if request.method == 'POST':
        dataform = LoginForm(request.POST).save()
        if dataform.is_valid():
            dataform.save()
        
    #username = request.POST.get('username')
    #password = request.POST.get('password')
    #data = Login(username=username , password=password)
    
    
    return render(request, 'pages/about.html', {'lf':LoginForm})


    