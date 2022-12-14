from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from administrationpanel.models import AdminUser, StudentFee

# Create your views here.


def home(request):
    return render(request, 'Administration/index.html')


def Profile(request):
    return render(request, 'Student/Profile.html')


def AttendanceReport(request):
    return render(request, 'Student/AttendanceReport.html')


def ChangePassword(request):

    if request.method == "POST":
        Email = request.POST["email"]
        password = request.POST["pswd"]
        RptPassword = request.POST["rptpswd"]
        user = AdminUser.objects.get(email=Email)
        if AdminUser.objects.filter(email=Email).exists() and user.is_student:
            if password == RptPassword:
                # AdminUser.objects.filter(id=user.id).update(password=password)
                if password == RptPassword:                  
                    u = AdminUser.objects.get(username=user.username)
                    # print(user.password)
                    u.set_password(password)
                    u.save()
                messages.info(request, 'Password has been changed')
                return render(request, 'Student/StudentLogin.html')
            else:
                messages.info(request, 'Password does not match')
        else:
            messages.info(request, 'Email Does not Exist')

    return render(request, 'Student/ChangePassword.html')


def ViewAttendance(request):
    return render(request, 'Student/ViewAttendance.html')


def Attendance(request):
    return render(request, 'Student/Attendance.html')


def HomeWork(request):
    return render(request, 'Student/HomeWork.html')


def ProgressCard(request):
    return render(request, 'Student/ProgressCard.html')


def Assignment(request):
    return render(request, 'Student/Assignment.html')


def Fees(request):
    user = request.session.get('user_name')
    print(user)
    user=StudentFee.objects.get(Name=user)
    student = StudentFee.objects.filter(id=user.id)
    return render(request, 'Student/Fees.html',{'students':student})


def Notice(request):
    return render(request, 'Student/Notice.html')


def StudentDashboard(request):
    user = request.session.get('user_name')
    print(user)
    student = StudentFee.objects.get(Name=user)
    # studentID=StudentFee.objects.filter(id=student.id)
    fees = student.PaidFee
    print(fees)
    return render(request, 'Student/StudentDashboard.html', {'fee':fees})


def signup(request):
    if request.method == 'POST':
        uname = request.POST["uname"]
        email = request.POST["email"]
        password = request.POST["password"]
        if AdminUser.objects.filter(username=uname).exists():
            messages.info(request, 'Username already used')
            return render(request, 'Student/signup.html')

        elif AdminUser.objects.filter(email=email).exists():
            messages.info(request, 'Email already used')
            # return redirect('signup')
            return render(request, 'Student/signup.html')
        else:
            user_data = AdminUser.objects.create_user(
                username=uname, email=email, password=password, is_student=True)
            user_data.save()
            fee_data = StudentFee.objects.create(Email=email, TotalFee=8000, PendingFee=8000)            
            fee_data.save()
            # return redirect('AdminLogin')
            return render(request, 'Student/StudentLogin.html')
    else:
        return render(request, 'Student/signup.html')


def StudentLogin(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        password = request.POST['password']
        is_student = 'true'
        # obj = AdminUser.objects.first()
        user = authenticate(request, username=uname, password=password)

        # getuser = AdminUser.objects.get(id=user.)

        # print(check)
        if user is not None and user.is_student:
            # if user.is_student == True:
            # print(user, uname, password)
            # if Studentdetails.objects.filter(Name=user.username).exists():
            #     user_name = Studentdetails.objects.get(Name = user.username)
            login(request, user)
            user_name=user.Name
            request.session['user_name'] = user_name
            # print(user_name)
            # return redirect("dashboard")
            return render(request, 'Student/StudentDashboard.html')
        else:
            # print(user, uname, password)
            messages.info(request, 'Invalid Username or Password')
            # return redirect('AdminLogin')
            return render(request, 'Student/StudentLogin.html')
    else:
        return render(request, 'Student/StudentLogin.html')


def Studentlogout(request):
    logout(request)
    # return render(request, 'Administration/index.html')
    return redirect('../Administration/index')
