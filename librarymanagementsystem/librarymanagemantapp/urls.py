from django.urls import path

from librarymanagemantapp import views

urlpatterns=[
    path('',views.log_fun,name='log'),
    path('adminsignup',views.adminsign_fun,name='adminsignup'),
    path('studsignup',views.studentsign_fun,name='studsignup'),
    path("checkdata",views.checklog_fun),

    path('adminreg',views.adminreg_fun),
    path('studentreg',views.studentreg_fun),

    path('home', views.admin_home_fun, name='home'),  # it will redirect to home.html

    path('add_book', views.addbooks_fun,name='add'),
    path('readdata',views.bookreaddata_fun),

    path('displaybook', views.displaybook_fun, name='display'),  # it will display student table data in display.html file

    path('delete/<int:id>', views.admindelete_fun, name='del'),  # it will delete record from student table
    path('update/<int:id>',views.adminupdate_fun,name='up'), # it will update student data

    path('assignbook',views.assign_book_fun,name='assign'),
    path('readsemcourse', views.read_sem_course_fun),
    path('readstdbook', views.read_student_book_fun),

    path('disIssuedBk', views.display_IssuedBook_fun, name='IssuedBooks'),
    path('updatebook/<int:id>', views.update_book_fun, name='upbk'),
    path('delbook/<int:id>', views.delete_book_fun, name='delbk'),

    path('',views.admin_logout_fun,name='logoutt'),

    path('shome', views.student_home_fun, name='Shome'),  # it will redirect to student_home.html

    path('stud_books', views.stud_books_fun, name='stud_books'),

    path('getprofile', views.get_prof_fun, name='getprof'),

    path('', views.student_logout_fun, name='logouttt'),

]