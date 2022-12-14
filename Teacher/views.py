from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from administrationpanel.models import AdminUser, StudentFee

# Create your views here.


def home(request):
    return render(request, 'Administration/index.html')


def Profile(request):
    return render(request, 'Teacher/Profile.html')


def Attendance(request):
    return render(request, 'Teacher/Attendance.html')


def AttendanceReport(request):
    return render(request, 'Teacher/AttendanceReport.html')


def ViewAttendance(request):
    return render(request, 'Teacher/ViewAttendance.html')


def Fees(request):
    return render(request, 'Teacher/Fees.html')


def FeeDues(request):
    value = request.GET['value']
    students=StudentFee.objects.filter(Std=value)
    return render(request, 'Teacher/FeeDues.html',{'students':students,'std':value})


def HomeWork(request):
    return render(request, 'Teacher/HomeWork.html')


def ProgressCard(request):
    return render(request, 'Teacher/ProgressCard.html')


def Assignment(request):
    return render(request, 'Teacher/Assignment.html')


def Notice(request):
    return render(request, 'Teacher/Notice.html')


def TeacherDashboard(request):
    return render(request, 'Teacher/TeacherDashboard.html')


def AddAttendance(request):
    return render(request, 'Teacher/AddAttendance.html')


def ViewAttendance(request):
    return render(request, 'Teacher/ViewAttendance.html')


def ChangePassword(request):
    if request.method == "POST":
        Email = request.POST["email"]
        password = request.POST["pswd"]
        RptPassword = request.POST["rptpswd"]
        user = AdminUser.objects.get(email=Email) 
        if AdminUser.objects.filter(email=Email).exists() and user.is_teacher:            
            if password == RptPassword:                  
                # AdminUser.objects.filter(id=user.id).update(password=password)
                if password == RptPassword:                  
                    u = AdminUser.objects.get(username=user.username)
                    # print(user.password)
                    u.set_password(password)
                    u.save()
                messages.info(request, 'Password has been changed')
                return render(request, 'Teacher/TeacherLogin.html')
            else:
                messages.info(request, 'Password does not match')
        else:
            messages.info(request, 'Email Does not Exist')

    return render(request, 'Teacher/ChangePassword.html')



def signup(request):
    if request.method=='POST':
        uname=request.POST["uname"]
        email=request.POST["email"]
        password=request.POST["password"]
        if AdminUser.objects.filter(username=uname).exists():
            messages.info(request,'Username already used')
            # return redirect('signup')

            return render(request,'Teacher/signup.html')

        elif AdminUser.objects.filter(email=email).exists():
            messages.info(request,'Email already used')
            # return redirect('signup')
            return render(request,'Teacher/signup.html')
        else:
            user_data=AdminUser.objects.create_user(username=uname, email=email, password=password, is_teacher=True)
            user_data.save()
            # return redirect('AdminLogin')
            return render(request,'Teacher/TeacherLogin.html')
    else:
        return render(request,'Teacher/signup.html')

def TeacherLogin(request):
    if request.method=='POST':
        uname=request.POST['uname']
        password=request.POST['password']            
        user = authenticate(request, username=uname, password=password)
        if user is not None and user.is_teacher:            
            login(request, user)
            # return redirect("dashboard")
            return render(request, 'Teacher/TeacherDashboard.html')
        else:
            messages.info(request,'Invalid Username or Password')
            # return redirect('TeacherLogin')
            return render(request, 'Teacher/TeacherLogin.html')
    else:
        return render(request, 'Teacher/TeacherLogin.html')

def StudentsRegister(request):
    return render(request, 'Teacher/StudentsRegister.html')

def StudentsMarks(request):
    return render(request, 'Teacher/StudentsMarks.html')

def TimeTable(request):
    return render(request, 'Teacher/TimeTable.html')


def Teacherlogout(request):
    logout(request)
    # return render(request, '../Administration/index.html')
    return redirect('../Administration/index')






