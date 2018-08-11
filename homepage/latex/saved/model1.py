from django.db import models
from django.urls import reverse


"""class Question(models.Model):
    branch = models.CharField(blank=False, max_length=60)
    course = models.CharField(blank=False, max_length=60)
    module = models.CharField(blank=False, max_length=60)
    chapter = models.CharField(blank=False, max_length=60)
    question = models.CharField(blank=False, max_length=200)

    MARK_CHOICES = ((0, "2"), (1, "5"), (2, "10"))
    marks = models.CharField(max_length=1, 
                             choices=MARK_CHOICES,
                             blank=False)
    PRIORITY_CHOICES = ((0, '1'), (1, '2'), (2, '3'), (3, '4'))
    priority = models.CharField(max_length=1,
                                choices=PRIORITY_CHOICES,
                                blank=False)

    class Meta:
        ordering = ('question',)
        index_together = (('branch', 'course', 'module', 'chapter', 'question', 'marks', 'priority'),)
        db_table = 'quest'
        verbose_name = 'Question'
        verbose_name_plural = 'Question'
    
    # returns to index page after clicking submit
    def get_absolute_url(self):
        return reverse('latex:index')"""


"""from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_faculty = models.BooleanField(default=False)
    is_hod = models.BooleanField(default=False)

class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)"""


class CreateQuestion(models.Model):
    BRANCH_CHOICE = (
            ('Bachelor Of Technology(B.Tech)', 'Bachelor Of Technology(B.Tech)'),
            ('Bachelor Of Computer Applications(BCA)', 'Bachelor Of Computer Applications(BCA)',),
            ('Bachelor Of Science(B.Sc)', 'Bachelor Of Science(B.Sc)'),
            ('Bachelor of Buisness Administration(BBA)', 'Bachelor Of Buisness Administration(BBA)'),
            ('Bachelor Of Commerce(B.Com)', 'Bachelor Of Commerce(B.Com)'),
    )
    branch = models.CharField(max_length=50, choices=BRANCH_CHOICE)
    specialization = models.CharField(max_length=50)
    SEMESTER_CHOICE = (
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
    )
    semester = models.IntegerField(choices=SEMESTER_CHOICE)
    course = models.CharField(max_length=50)
    module = models.CharField(max_length=50)
    chapter = models.CharField(max_length=40)
    question = models.CharField(max_length=250)
    MARK_CHOICE = (
            ('2', '2'),
            ('5', '5'),
            ('10', '10'),
    )
    marks = models.IntegerField(choices=MARK_CHOICE)
    PRIORITY_CHOICE = (
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
    )
    priority = models.IntegerField(choices=PRIORITY_CHOICE)
