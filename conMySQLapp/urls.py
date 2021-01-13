from django.urls import path
from . import views


urlpatterns = [
    path('', views.studentList, name='studentlist'),
    path('student-list-create/', views.studentListCreate, name='stdlistcreate'),
    path('student-list-edit/<int:stdid>/', views.studentListEdit, name='stdlistedit'),
    path('student-list-delete/<int:stdid>/', views.studentListDelete, name='stdlistdelete'),
]
