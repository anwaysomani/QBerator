"""
Admin extension for viewing questions from database

Developer: Anway Somani

"""
# import model
from .models import Question

# Register models
admin.site.register(Question)
