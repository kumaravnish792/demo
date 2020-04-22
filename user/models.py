from django.db import models

# Create your models here.

class Employee(models.Model):
	employee_id = models.CharField(max_length=10,null=False)
	name = models.CharField(max_length=200, null=True)
	salary = models.CharField(max_length=1000, null=True)
	d_o_j = models.DateTimeField(auto_now_add=True, null=True)
	state = models.CharField(max_length=20, null=True)

	def __str__(self):
		return self.name

class Progress(models.Model):
	name = models.CharField(max_length=50, null=True)
	count = models.IntegerField()

	def __str__(self):
		return self.name

