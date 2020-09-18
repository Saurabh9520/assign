from django.db import models

# Create your models here.
class List(models.Model):
    Choose = (
        ('First Task', 'First Task'),
        ('second Task', 'Second_task'),
        ('Third _task', 'Third_task')
    )
    Task_name = models.CharField(max_length=20, unique=True)
    Task_choose = models.CharField(max_length=20, null=True, choices=Choose)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.Task_name

