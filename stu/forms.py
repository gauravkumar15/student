from django import forms
from .models import Student
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ('Name','Roll_no','Father_name','Department','Address',)
        
class Register(forms.ModelForm):
    password = forms.CharField(label='Password', widget = forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username','email',)