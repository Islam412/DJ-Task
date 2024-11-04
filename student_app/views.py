from django.shortcuts import render, redirect
from .models import Student, MyUser



def home_view(request):
    students = Student.objects.all()
    return render(request, 'student_app/home.html', {'students': students})



def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        MyUser.objects.create(username=username, password=password)
        return redirect('login')
    return render(request, 'student_app/register.html')



def login_view(request):
    if request.method == 'POST':
        user = MyUser.objects.filter(username=request.POST['username'],password=request.POST['password'])   
        return redirect('home')
    return render(request, 'student_app/login.html')





def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        address = request.POST['address']
        Student.objects.create(name=name, age=age, address=address)
        return redirect('home')
    return render(request, 'student_app/add_student.html')