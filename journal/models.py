from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator


class Student(models.Model):
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	patronymic = models.CharField(max_length=100)

	def __str__ (self):
		return "%s %s"%(self.firstname,self.lastname)


class Subject(models.Model):
	name = models.CharField(max_length=100)
	teacher = models.CharField(max_length=100,blank=True,null=True)
	#description 
	

	def __str__ (self):
		return self.name 

class Mark(models.Model):
    student = models.ForeignKey(Student)
    subject = models.ForeignKey(Subject)
    value = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)], null=False, blank=False)


    def __str__ (self):
    	return str(self.value)
