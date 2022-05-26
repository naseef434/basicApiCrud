
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('album/',views.Albumview.as_view()),
    path('album/<int:pk>/',views.Albumview.as_view()),
]

