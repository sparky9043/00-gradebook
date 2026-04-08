from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=50)
    date_added = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['date_added']
    
    def get_year(self):
        return self.date_added.year
    
    def __str__(self):
        return self.title
    
class Student(models.Model):
    course = models.ManyToManyField(Course)
    name = models.CharField(max_length=50)
    level = models.DecimalField(max_digits=2, decimal_places=0)
    dob = models.DateField()
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name