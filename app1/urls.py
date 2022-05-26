
from django.urls import path
from . import views






urlpatterns = [
    path('album/',views.Albumview.as_view()),
    path('album/<int:pk>/',views.Albumview.as_view()),
]
