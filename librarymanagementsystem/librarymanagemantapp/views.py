from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

from librarymanagemantapp.models import Student, Course, Book, Issuebook


# Create your views here.
def log_fun(request):
    return render(request,'login.html',{'data':''})

def adminsign_fun(request):
    return render(request,'adminsignup.html',{'data':''})

def studentsign_fun(request):
    c1 = Course.objects.all()
    return render(request,'studentsignup.html',{'data':'','lis':c1})

def checklog_fun(request):
    usern=request.POST['tName']
    userp=request.POST['tpass']
    user1=authenticate(username=usern,password=userp)
    if user1 is not None:
        if user1.is_superuser:
            return render(request,'admin_home.html')
        else:
            return render(request, 'login.html', {'data': 'user is not super user'})
    elif Student.objects.filter(Q(sname=usern) & Q(spassw=userp)).exists():

        request.session['student'] = usern

        return render(request,'student_home.html',{'Name':request.session['student']})
    else:
        return render(request, 'login.html', {'data': 'inavlid username or password'})


def adminreg_fun(request):
    usern=request.POST['tname']
    usere=request.POST['temail']
    userp=request.POST['tpass']
    if User.objects.filter(Q(username=usern)|Q(email=usere)).exists():
        return render(request, 'adminsignup.html', {'data': 'username or email already exists'})
    else:
        u1=User.objects.create_superuser(username=usern, email=usere, password=userp)
        u1.save()
        return render(request, 'login.html', {'data': 'Account created successfully'})


def studentreg_fun(request):
    usern = request.POST['tname']
    users = request.POST['tsem']
    userm = request.POST['tmob']
    userc = request.POST['ddlcourse']
    userp = request.POST['tpass']
    if Student.objects.filter(Q(sname=usern)):
        return render(request, 'studentsignup.html', {'data': 'user name already exists try another'})
    else:
        s1=Student()
        s1.sname=usern
        s1.spassw=userp
        s1.sem=users
        s1.sphno=userm
        s1.scourse=Course.objects.get(cname=userc)
        s1.save()
        return render(request, 'login.html', {'data': 'Registered successfully'})


def admin_home_fun(request):
    return render(request, 'admin_home.html')


def addbooks_fun(request):
    s1 = Course.objects.all()
    return render(request, 'add_books.html', {'Course_Data': s1})


def bookreaddata_fun(request):
    s1 = Book()
    s1.bname = request.POST['txtName']
    s1.authname = request.POST['txtAuthor']
    s1.courseid = Course.objects.get(cname=request.POST['ddlCourse'])
    s1.save()
    return render(request,'add_books.html')


def displaybook_fun(request):
    s1 = Book.objects.all()
    return render(request, 'displaybook.html', {'data': s1})


def admindelete_fun(request,id):
    s1 = Book.objects.get(id=id)
    s1.delete()
    return redirect('display')


def adminupdate_fun(request,id):
    s1 = Book.objects.get(id=id)
    course = Course.objects.all()

    if request.method == 'POST':
        s1.bname = request.POST['txtName']
        s1.authname = request.POST['txtAuthor']
        s1.courseid = Course.objects.get(cname=request.POST['ddlCourse'])
        s1.save()
        return redirect('display')
    return render(request, 'adminupdate.html', {'data': s1, 'Course_Data': course})


def assign_book_fun(request):
    course = Course.objects.all()
    return render(request,'assignbook.html',{'Course_Data': course})


def read_sem_course_fun(request):
    stdsem = request.POST['txtsem']
    course = request.POST['ddlcourse']
    students = Student.objects.filter(Q(sem=stdsem) & Q(scourse=Course.objects.get(cname=course)))
    print(students)
    books = Book.objects.filter(courseid=Course.objects.get(cname=course))
    print(books)
    return render(request, 'assignbook.html', {'Student_Data': students, 'Book_Data': books})


def read_student_book_fun(request):
    b = Issuebook()
    b.studname = Student.objects.get(sname=request.POST['ddlStdname'])
    b.bookname = Book.objects.get(bname=request.POST['ddlBookname'])
    b.startdate = request.POST['startdate']
    b.enddate = request.POST['enddate']
    b.save()
    course = Course.objects.all()
    return render(request, 'assignbook.html', {'Course_Data':course, 'msg': 'Book Assigned Successfully'})


def display_IssuedBook_fun(request):
    Ibooks = Issuebook.objects.all()
    return render(request, 'DisplayIssuedBooks.html', {'bk':Ibooks})


def update_book_fun(request,id):
    b = Issuebook.objects.get(id=id)
    s = Student.objects.get(id=b.studname_id)
    bk = Book.objects.filter(courseid=s.scourse)
    print(b.startdate)
    if request.method == 'POST':
        b.studname = Student.objects.get(sname=request.POST['txtstdname'])
        b.bookname = Book.objects.get(bname=request.POST['ddlbkname'])
        b.startdate = request.POST['startdate']
        b.enddate = request.POST['enddate']
        b.save()
        return redirect('IssuedBooks')
    return render(request, 'UpdateIssuedBook.html', {'ib': b,'stud':s, 'books': bk})


def delete_book_fun(request, id):
    b = Issuebook.objects.get(id=id)
    b.delete()
    return redirect('IssuedBooks')


def admin_logout_fun(request):
    return redirect('log')


def student_home_fun(request):
    return render(request, 'student_home.html',{'Name':request.session['student']})

def stud_books_fun(request):
    s = Student.objects.get(sname=request.session['student'])
    b=  Issuebook.objects.filter(studname=s)
    return render(request,'stud_books.html',{'data':b})

def get_prof_fun(request):
    s = Student.objects.get(sname=request.session['student'])
    return render(request,'stud_profile.html',{'data':s})



def student_logout_fun(request):
    return redirect('log')