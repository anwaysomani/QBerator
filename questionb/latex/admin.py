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

#class coursedisp(admin.ModelAdmin):
 #   list_display = ('sem_abbreviation', 'course', 'course_code')

class moduledisp(admin.ModelAdmin):
    list_display = ('course', 'module')


admin.site.register(Branch)
admin.site.register(Semester)
admin.site.register(Course, CourseAdmin)
admin.site.register(Modules)
admin.site.register(Branch1)
admin.site.register(Specialization1)
admin.site.register(Semester1)
admin.site.register(Subject1)
admin.site.register(Module1)
admin.site.register(Chapter1)

