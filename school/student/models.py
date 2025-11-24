from django.db import models


class Student(models.Model):
    firstname = models.CharField(max_length=225)
    lastname = models.CharField(max_length=225)
    phone = models.IntegerField(null=True)
    join_date = models.DateField(null=True)

    def __str__(self):
        return self.firstname
