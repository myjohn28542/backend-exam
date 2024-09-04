from django.db import models

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.name


class Classroom(models.Model):
    grade = models.CharField(max_length=20)
    section = models.CharField(max_length=5)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='classrooms')

    def __str__(self):
        return f"{self.grade} {self.section}"


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')])
    classrooms = models.ManyToManyField(Classroom, related_name='teachers')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')])
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
