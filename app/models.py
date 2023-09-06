from django.db import models

# Create your models here.
class school(models.Model):
    school_name=models.CharField(max_length=100,primary_key=True)
    principal_name=models.CharField(max_length=100)
    school_location=models.CharField(max_length=100)

    def __str__(self):
        return self.school_name

class student(models.Model):
    school_name=models.ForeignKey(school,on_delete=models.CASCADE)
    student_name=models.CharField(max_length=100)
    sid=models.IntegerField(primary_key=True)

    def __str__(self):
        return self.student_name