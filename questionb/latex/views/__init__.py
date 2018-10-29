# Importing from login.py
# -----------------------

# Main page, Faculty and HOD Login Page
# Importing post-Login page
from .login import findex, hindex, error

# Importing from eachcrs.py(file containing question for each subject)
from .eachcrs import *

# Importing view from .epdf for Exporting file to pdf(trial)
from .epdf import html_to_pdf_view, generate_pdf

from .quespaper import *
