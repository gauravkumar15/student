from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm, Register

# Create your views here.

def home(request):
    students = Student.objects.all()
    return render(request,'stu/home.html',{'students':students})

def detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request,'stu/detail.html',{'student':student})

def new(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request,'stu/new.html', {'form':form})

def register(request):
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('home')
    else:
        form = Register()
        return render(request, 'stu/regis.html', {'form':form})

