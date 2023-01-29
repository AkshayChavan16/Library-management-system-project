from django.db import models


# Create your models here.
class Course(models.Model):
    cname = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.cname}'


class Book(models.Model):
    bname = models.CharField(max_length=50)
    authname = models.CharField(max_length=50)
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.bname}'


class Student(models.Model):
    sname = models.CharField(max_length=50)
    spassw = models.CharField(max_length=50)
    sphno = models.BigIntegerField()
    sem = models.CharField(max_length=50)
    scourse = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.sname}'


class Issuebook(models.Model):
    studname = models.ForeignKey(Student, on_delete=models.CASCADE)
    bookname = models.ForeignKey(Book, on_delete=models.CASCADE)
    startdate = models.DateField()
    enddate = models.DateField()
