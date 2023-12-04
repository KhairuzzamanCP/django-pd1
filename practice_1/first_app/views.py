from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    d ={'author':'Rana','age': 15,'lst':['python','is','best'],'birthday':datetime.datetime.now(),'add':10 ,'C':'django' ,'ct':'django is best','len':' ','low':'CODING','courses': [
    {
       'id':1,
       'name': 'python',
       'fee':5000 
    },
    {
      'id':2,
       'name': 'django',
       'fee':10000 
        
    },
    {
      'id':3,
       'name': 'DSA',
       'fee':6000
    }
    ]}
    return render (request, 'home.html', d)
     
