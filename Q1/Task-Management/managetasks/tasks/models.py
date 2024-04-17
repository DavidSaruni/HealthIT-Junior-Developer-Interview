from django.db import models

# Create your models here.
class Task(models.Model):
    priority_choices = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    ]

    status_choices = [
        ('started', 'Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ]
    
    name = models.CharField(max_length=200, null=True, blank=True) 
    priority = models.CharField(max_length=200, choices=priority_choices, null=True, blank=True)
    status = models.CharField(max_length=200, choices=status_choices, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    # used null and blank as True to help me do my testing without issues
    
    def __str__(self):
        return self.name

    # return tasks according to priority and status for 6 months
    def get_tasks(self):
        tasks = Task.objects.filter(date__gte='2023-09-01', date__lte='2024-04-17').order_by('priority', 'status')
        return tasks