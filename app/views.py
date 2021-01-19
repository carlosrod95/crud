"""
Definition of views.
"""

from datetime import datetime
from django.http import HttpRequest
from django.shortcuts import render, redirect  
from app.forms import HistorialForm  
from app.models import Historial  
from django.shortcuts import (get_object_or_404, 
                              HttpResponseRedirect) 
  
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = HistorialForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = HistorialForm()  
    return render(request,'app/referente.html',{'form':form})  

def show(request):  
    historials = Historial.objects.all()  
    return render(request,'app/show.html',{'historials':historials})  

def edit(request, id):  
    historial = Historial.objects.get(id=id)  
    return render(request,
                  'app/edit.html', 
                  {
                      'historial':historial
                      }
                  ) 

#def update(request, id):  
#    historial = get_object_or_404(Historial, id=id)
#    if request.method == 'POST':
#        form = HistorialForm(request.POST, instance = historial) 
#        #form = HistorialForm( instance = historial) 
#        if form.is_valid():  
#            form.save(commit=True)
#            historial.save()  
#        return redirect('/show')
#    else:
#        form = HistorialForm(instance=historial)
#    return render(request, 
#                  'app/edit.html',
#                 {
#                     #'historial':historial,
#                     'form':form
#                 })  

def update(request, id):  
    historial = Historial.objects.get(id=id)  
    if request.method == 'POST':
        form = HistorialForm(request.POST, instance = historial)  
        if form.is_valid():  
            form.save()  
            return redirect("/show")  
        else:
            form = HistorialForm()
    return render(request, 
                  'app/edit.html', 
                  {
                      'historial': historial,
                      'form':form
                      })  



def destroy(request, id):  
    historial = Historial.objects.get(id=id)  
    historial.delete()  
    return redirect("/show")  

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
