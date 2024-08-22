from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

from app_view.forms import ContactForm

class MyView(View):
    name = 'rizan'
    def get(self, request):
        context = {'msg' : 'Welcome Back!'}
        template_name = 'index.html'
        # return HttpResponse('<h1>Class Baed View - GET </h1>')
        # return HttpResponse(self.name)
        return render(request, template_name, context)
    

def contactfun(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank You Form Submittrd!')
    else:
        template_name = 'contact.html'
        form = ContactForm
        return render(request, template_name, {'form':form})
    
def contact_func_view(request, template_name):
    if request.method == 'GET':
        template_name = template_name
        form = ContactForm
        return render(request, template_name , {'form':form})

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank You Form Submitted!!') 
    
class ContactClassView(View):
    template_name = ''
    def get(self, request):
        form = ContactForm
        return render(request, self.template_name , {'form':form})
    
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank You Form Submitted!!')

class MyViewChild(MyView):
    def get(self, request):
        return HttpResponse(self.name)
    



    
