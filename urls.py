
from django.urls.conf import path
from . import views

urlpatterns = [
    
    path('project/',views.home,name='home')
    
]
