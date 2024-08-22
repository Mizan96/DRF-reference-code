from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView, RedirectView

from django.views import View

from app_crud.models import User

from app_crud.forms import UserForm

# Create your views here.

class UserView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        student = User.objects.all()
        form = UserForm()
        context = {
            'student': student,
            'form': form,
        }
        return context
    
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password  = form.cleaned_data['password']
            # user = User(name=name, email=email)
            user = User(name=name, email=email, password=password)
            user.save()
        return HttpResponseRedirect('/')
    
class UserUpdateView(View):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        form = UserForm(instance=user)
        return render(request, 'update.html', {'form': form})
    
    def post(self, request, pk):
        user = User.objects.get(pk=pk)
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    
class UserDeleteView(RedirectView):
    url = '/'
    def get_redirect_url(self, *args: Any, **kwargs):
        delete_id = kwargs['pk']
        User.objects.get(pk=delete_id).delete()
        return super().get_redirect_url(*args, **kwargs)

    
       
