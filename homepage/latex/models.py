from django.db import models

# fields for interlinked (dependencies)

class Branch(models.Model):
    BRANCH_CHOICE = (
            ('Bachelor Of Technology(B.Tech)', 'Bachelor Of Technology(B.Tech)'),
            ('Bachelor Of Computer Applications(BCA)', 'Bachelor Of Computer Applications(BCA)',),
            ('Bachelor Of Science(B.Sc)', 'Bachelor Of Science(B.Sc)'),
            ('Bachelor of Buisness Administration(BBA)', 'Bachelor Of Buisness Administration(BBA)'),
            ('Bachelor Of Commerce(B.Com)', 'Bachelor Of Commerce(B.Com)'),
    )
    name = models.CharField(max_length=50, choices=BRANCH_CHOICE)

    def __unicode__(self):
        return u'%s' % self.name

class Specialization(models.Model):
    name = models.CharField(max_length=50)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'%s' % self.name

class Semester(models.Model):
    sem = models.IntegerField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'%s' % self.name

class Course(models.Model):
    name = models.CharField(max_length=50)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'%s' % self.name

class Module(models.Model):
    name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'%s' % self.name

class Chapter(models.Model):
    name = models.CharField(max_length=50)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'%s' % self.name

class Question(models.Model):
    quest = models.CharField(max_length=250)

    def __unicode__(self):
        return u'%s' % self.quest

class Marks(models.Model):
    MARKS_CHOICE = (
            ('2', '2'),
            ('5', '5'),
            ('10', '10'),
    )
    marks = models.IntegerField(choices=MARKS_CHOICE)

    def __unicode__(self):
        return u'%s' % self.marks

class Additional(models.Model):
    PRIORITY_CHOICE = (
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
    )
    priority = models.IntegerField(choices=PRIORITY_CHOICE)
    note = models.CharField(max_length=200)

