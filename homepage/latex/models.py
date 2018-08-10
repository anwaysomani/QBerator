from django.db import models
from django.urls import reverse

class Question(models.Model):
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

                            
    """marks = models.TypedChoiceField(
            label="Select marks",
            choices=((0, "2"), (1, "5"), (2, "10")),
            coerce=lambda x: bool(int(x)),
            blank=True)
    priority = models.TypedChoiceField(
            label="Priority Level",
            choices=((0, "1"), (1, "2"), (2, "3"), (3, "4")),
            coerce=lambda y: bool(int(y)),
            blank=True)"""

    class Meta:
        ordering = ('question',)
        index_together = (('branch', 'course', 'module', 'chapter', 'question', 'marks', 'priority'),)
        db_table = 'quest'
        verbose_name = 'Question'
        verbose_name_plural = 'Question'
    
    # returns to index page after clicking submit
    def get_absolute_url(self):
        return reverse('latex:index')
