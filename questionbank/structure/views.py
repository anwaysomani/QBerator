from django.shortcuts import render

def StructureMain(request):
    return render(request, 'structure.html', {})

# Views for redirecting urls for base pages in structure templates
def indexPage(request):
    return render(request, 'erdiagram/index.html', {})

# View for individual er page
def individualER(request):
    return render(request, 'erdiagram/individual.html', {})

def dataFlowDiag(request):
    return render(request, 'data-flow/df-main.html', {})

def documentation(request):
    return render(request, 'documentation/qbdocs.html', {})
