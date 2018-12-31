from django.db import models


# Report models
class Issue(models.Model):
    name = models.CharField(max_length=70)
    issue = models.TextField(null=False)
    image = models.FileField(null=True)
   
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Issue'
        verbose_name_plural = 'Issues'

class Color(models.Model):
    color = models.CharField(max_length=25)

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = 'Color Lab'
        verbose_name_plural = 'Color Lab'
