from django.db import models
from accounts.models import Account
# Create your models here.


Status= (
    ('Open',"Open"),
    ('Hold',"Hold"),
    ('Closed',"Closed"),
    ('Work in Progress',"Work in Progress"),
)

priority =(
    ("Low","Low"),
    ("Medium","Medium"),
    ("High","High"),
)
class Todo(models.Model):
    assign_to = models.ForeignKey(Account,on_delete=models.CASCADE)
    search = models.CharField(max_length=200,null=True,blank=True)
    title = models.CharField(max_length=100)
    task = models.TextField(max_length=300)
    company_name = models.CharField(max_length=100,null=True,blank=True)
    deadline = models.DateField()
    status = models.CharField(max_length=20,null=True,blank=True,choices = Status,default='Open')
    remark = models.TextField(max_length=300,null=True,blank=True,default="No Remarks")
    priority = models.CharField(max_length=10,null=True,blank=True,choices=priority,default='Medium')

Type = (
    ('Bug',"Bug"),
    ('Suggestion',"Suggestion"),
)


Exp = (
    ("Good","Good"),
    ("Average","Average"),
    ("Bad","Bad"),
)



class Feedback(models.Model):

    user = models.CharField(max_length=50,null=True,blank=True)
    type = models.CharField(max_length=10,null=True,blank=True,choices=Type,default = 'Suggestion')
    experience = models.CharField(max_length=10,null=True,blank=True,choices=Exp,default='Good')
    feedback = models.TextField(max_length=500)
    
    def __str__(self):
        return f"{self.user} + {self.type}"
