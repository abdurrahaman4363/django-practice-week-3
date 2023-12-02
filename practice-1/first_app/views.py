from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def home(request):
    # return HttpResponse("app page")
    # backend theke front end e data dictionary format e patathe hoi
    # context: jokhon backend theke frontend e data patai tokhon dictionary format e data patai etake context bole

    d = {'author':'Abdur Rahaman', 'age':23,'list':['JavaScript','is','Important','For','All'],'courses':[
        {
            'id':1,
            'name':'python',
            'fee':5000
        },
       
        {
            'id':2,
            'name':'django',
            'fee':10000
        },
        {
            'id':3,
            'name':'C',
            'fee':1000
        },
         {
            'id':4,
            'name':'java',
            'fee':4000
        },
         {
            'id':5,
            'name':'javaScript',
            'fee':50000
        },
         {
            'id':6,
            'name':'c++',
            'fee':500
        },
    ],
    'birthday':datetime.datetime.now(),
    'val' : '',
    }
    # return render(request,'home.html',context=d)
    return render(request,'home.html',d)
    # return render(request,'home.html',{'author':'Rahim', 'age':20,'color':'black'})