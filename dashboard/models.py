from django.db import models
from email.mime import image
from django.contrib.auth.models import User
class Notes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    description=models.TextField()
    def _str_(self):
        return self.title
    class Meta:
       verbose_name="notes"
       verbose_name_plural="notes"
class Homework(models.Model):
      user=models.ForeignKey(User,on_delete=models.CASCADE)
      subject=models.CharField(max_length=50)
      title=models.CharField(max_length=100)
      description=models.TextField()
      due=models.DateTimeField()
      is_finished=models.BooleanField(default=False)
      def _str_(self):
          return self.title
class Todo(models.Model):
      user=models.ForeignKey(User,on_delete=models.CASCADE)
      title=models.CharField(max_length=100)
      is_finished=models.BooleanField(default=False)
      def _str_(self):
          return self.title
# Create your models here.
#rec

class product(models.Model):
    name=models.CharField(max_length=40)
    description=models.CharField(max_length=200,default='')
    image=models.ImageField(upload_to='upload/products/')
    def __str__(self):
      return self.name 
    
