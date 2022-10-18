
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import ListView,CreateView
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.views.generic import RedirectView
# Create your views here.
from django.contrib import messages

def default(request):
    return render(request,'home.html')


class staff_view(ListView):
    model=staff
    context_object_name='obj'
    template_name='staff.html'
    
class student_view(ListView):
    model=student
    context_object_name='obj'
    template_name='students.html'
    
class staff_form_view(CreateView):
    model=staff
    form_class=staff_form
    template_name='staff_create.html'
    success_url='/'

class student_form_view(CreateView):
    model=student
    form_class=student_form
    template_name='student_create.html'
    success_url='/'

  
class send_email(RedirectView):
    def post(self,request):
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        send_mail(subject,message,'abhinish943@gmail.com',[email],fail_silently=False)
        messages.success(request,'Email has Sent')
        return redirect('/')



class send_email_collectively(RedirectView):
    def post(self,*args,**kwargs):
        subject=self.request.POST.get('subject')
        message=self.request.POST.get('message')
        check=kwargs['name']
        if check=='student':
            obj=student.objects.all()
            email=[]
            for i in obj:
                send_mail(subject,message,'abhinish943@gmail.com',[i.email],fail_silently=False)
            messages.success(self.request,'Email has Sent')
            return redirect('/')
            
        else:
            obj=staff.objects.all()
            email=[]
            for i in obj:
                send_mail(subject,message,'abhinish943@gmail.com',[i.email],fail_silently=False)
            messages.success(self.request,'Email has Sent')
            return redirect('/')

    def get(self,*args,**kwargs):
        return render(self.request,'message_form.html')
    