"""
Admin view for manipulating admin section 
from app: latex
"""


from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Branch, Specialization, Semester, Subject, Module, Chapter, SubjectCategory, Question

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
    list_display = ('branch_abbreviation', 'branch')
    labels = {
        'br_abbr': 'Branch Abbreviation'
    }

class SubjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('total_marks', 'required_2mk', 'required_5mk', 'required_10mk')
    fields = ['total_marks', ('required_2mk', 'maximum_2mk'), ('required_5mk', 'maximum_5mk'), ('required_10mk', 'maximum_10mk')]

class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('branch', 'specialization_abbreviation')
    labels = {
        'specialization_abbreviation': 'Specialization'
    }

class SemesterAdmin(admin.ModelAdmin):
    search_fields = ('specialization',)

# ------------------------------------------------------------------
# Registering models for application: latex                       #| 
# ------------------------------------------------------------------
admin.site.register(Branch, BranchAdmin)                          #|
admin.site.register(Specialization, SpecializationAdmin)          #|
admin.site.register(Semester, SemesterAdmin)                      #|
admin.site.register(Subject, SubjectAdmin)                        #|
admin.site.register(Module)                                       #|
admin.site.register(Chapter)                                      #|
admin.site.register(SubjectCategory, SubjectCategoryAdmin)        #|
# ------------------------------------------------------------------

# Sample declaration for Question module(testing purpose)
admin.site.register(Question)

