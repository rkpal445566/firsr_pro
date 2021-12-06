from django.shortcuts import render

# Create your views here.
def ed(request):
    skill={'skill':'active'}
    return render(request, 'edu/edu1.html',skill)
