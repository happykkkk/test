from django.db import models


class SchoolSubject(models.Model):

    title = models.CharField(max_length=20, verbose_name="Название предмета")

    def __str__(self):
        return self.title


class Student(models.Model):

    firs_name = models.CharField(max_length=10, verbose_name="Имя")
    last_name = models.CharField(max_length=12, verbose_name='Фамилия')

    def __str__(self):
        return "Ученик: {} {}".format(self.firs_name, self.last_name)


class Teacher(models.Model):

    first_name = models.CharField(max_length=10, verbose_name="Имя")
    last_name = models.CharField(max_length=12, verbose_name="Фамилия")

    def __str__(self):
        return "Учитель: {} {}".format(self.first_name, self.last_name)


class Journal(models.Model):

    title = models.CharField(max_length=10)
    subject = models.ManyToManyField(SchoolSubject, verbose_name="Предметы")
    grade = models.IntegerField(blank=True, verbose_name="Оценка")
    date = models.DateField(verbose_name="Дата провидения занятия")
    class_students = models.ManyToManyField(Student, verbose_name="Список учащихся")

    def __str__(self):
        return self.title
