from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('courses', views.index),
    path('courses/create', views.create),
    path('courses/destroy/<int:course_id>', views.destroy),
    path('courses/delete', views.delete),
]