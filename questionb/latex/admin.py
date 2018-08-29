from django.contrib import admin
from .models import *

# Combining Modules:
# ------------------

# Module View
class ModuleTabularInline(admin.TabularInline):
    model = Modules
    min_length = 2

# Inserting Module in Course
class CourseAdmin(admin.ModelAdmin):
    inlines = [ModuleTabularInline]
    
    class Meta:
        model = Course

# Inserting List Display Views
class branchdisp(admin.ModelAdmin):
    list_display = ('branch', 'specialization'),

class semesterdisp(admin.ModelAdmin):
    list_display = ('branch', 'sem_abbreviation'),

class coursedisp(admin.ModelAdmin):
    list_display = ('sem_abbreviation', 'course', 'course_code')

class moduledisp(admin.ModelAdmin):
    list_display = ('course', 'module')


admin.site.register(Branch, branchdisp)
admin.site.register(Semester, semesterdisp)
admin.site.register(Course, CourseAdmin)
admin.site.register(Modules, moduledisp)
