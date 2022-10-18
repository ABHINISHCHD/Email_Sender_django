from tkinter import Widget
from turtle import width
from .models import *
from django import forms




class staff_form(forms.ModelForm):


    class Meta:
        model=staff
        fields=['name','email','phone','address','position']
        widgets={
            'name':forms.TextInput(attrs={'placeholder':"enter name",
            'class':'form-control'}),
            
            'email':forms.EmailInput(attrs={'placeholder':"enter email",
            'class':'form-control'}),
            
            'phone':forms.NumberInput(attrs={'placeholder':"enter phone",
            'class':'form-control'}),
            
            'address':forms.TextInput(attrs={'placeholder':"enter address",
            'class':'form-control'}),
            
            'position':forms.TextInput(attrs={'placeholder':"enter position",
            'class':'form-control'})

        }

class student_form(forms.ModelForm):
    class Meta:
        model=student
        fields=['name','email','phone','address']
        widgets={
            'name':forms.TextInput(attrs={'placeholder':"enter name",
            'class':'form-control'}),
            
            'email':forms.EmailInput(attrs={'placeholder':"enter email",
            'class':'form-control'}),
            
            'phone':forms.NumberInput(attrs={'placeholder':"enter phone",
            'class':'form-control'}),
            
            'address':forms.TextInput(attrs={'placeholder':"enter address",
            'class':'form-control'}),
            

        }

