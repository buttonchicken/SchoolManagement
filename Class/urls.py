from django.urls import path
from .views import *

urlpatterns = [
    path('addetails',AddClassDetails.as_view()),
    path('addmarks',AddStudentMarks.as_view()),
    path('getmarks',GetScore.as_view())
]
