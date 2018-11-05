"""
Admin view for manipulating admin section 
from app: latex

Developer: Anway Somani

"""


from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Branch, Specialization, Semester, Subject, Module, Chapter, QuestionPaper, SubjectCategory, Question

# Adding verbose names to fields

# Changing link to Many-To-Many Field View
class SubjectAdmin(admin.ModelAdmin):
    list_filter = ('semester',)
    list_display = ('id', 'subject', 'subject_code')
    search_fields = ('subject',)

    # Improting media file for django admin
    class Media:
        css = {'all': ('css//admin/admin.css',),}

class BranchAdmin(admin.ModelAdmin):
    list_display = ('br_abbr', 'branch')
    labels = {
        'br_abbr': 'Branch Abbreviation'
    }

class SubjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('total_marks', 'required_2mk', 'required_5mk', 'required_10mk')
    fields = ['total_marks', ('required_2mk', 'maximum_2mk'), ('required_5mk', 'maximum_5mk'), ('required_10mk', 'maximum_10mk')]


# ------------------------------------------------------------------
# Registering models for application: latex                       #| 
# ------------------------------------------------------------------
admin.site.register(Branch, BranchAdmin)                          #|
admin.site.register(Specialization)                               #|
admin.site.register(Semester)                                     #|
admin.site.register(Subject, SubjectAdmin)                        #|
admin.site.register(Module)                                       #|
admin.site.register(Chapter)                                      #|
admin.site.register(QuestionPaper)                                #|
admin.site.register(SubjectCategory, SubjectCategoryAdmin)        #|
# ------------------------------------------------------------------

# Sample declaration for Question module(testing purpose)
admin.site.register(Question)

