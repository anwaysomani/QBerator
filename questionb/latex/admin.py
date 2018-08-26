from django.contrib import admin
from .models import *

# displaying list for BranchSem
class branchdisp(admin.ModelAdmin):
    list_display = ('branch', 'specialization', 'semester')

# displaying list for Subject
class subjectdisp(admin.ModelAdmin):
    list_display = ('branch', 'subject', 'sub_code')


# Registering mods in admin
admin.site.register(BranchSem,branchdisp)
admin.site.register(Subject,subjectdisp)
