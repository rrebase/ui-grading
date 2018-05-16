from django.db import models


class Student(models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    student_code = models.CharField(max_length=6)
    uniid = models.CharField(max_length=100)
    points = models.IntegerField(default=0)
    plagiarism = models.BooleanField(default=False)
    kommentaar = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class MainTask(models.Model):
    short_description = models.CharField(max_length=100)
    long_description = models.TextField(blank=True)
    points = models.IntegerField(default=10)

    def __str__(self):
        return self.short_description


class BonusTask(models.Model):
    short_description = models.CharField(max_length=100)
    long_description = models.TextField(blank=True)
    points = models.IntegerField(default=1)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.short_description
