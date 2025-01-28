from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('manage_programs/', views.manage_programs, name='manage_programs'),
    path('manage_rooms/', views.manage_rooms, name='manage_rooms'),
    path('manage_course/', views.manage_course, name='manage_course'),
    path('manage_exam/', views.manage_exam, name='manage_exam'),
    # Add more paths as needed

    path('program_list/', views.program_list, name='program_list'),
    path('add-program/', views.add_program, name='add_program'),
    path('edit-program/<int:pk>/', views.edit_program, name='edit_program'),
    path('delete-program/<int:pk>/', views.delete_program, name='delete_program'),

    path('room_list/', views.room_list, name='room_list'),
    path('add-room/', views.add_room, name='add_room'),
    path('edit-room/<int:pk>/', views.edit_room, name='edit_room'),
    path('delete-room/<int:pk>/', views.delete_room, name='delete_room'),

    path('course_list/', views.course_list, name='course_list'),
    path('add-course/', views.add_course, name='add_course'),
    path('edit-course/<int:pk>/', views.edit_course, name='edit_course'),
    path('delete-course/<int:pk>/', views.delete_course, name='delete_course'),

    path('exam_list/', views.exam_list, name='exam_list'),
    path('add-exam/', views.add_exam, name='add_exam'),
    path('edit-exam/<int:pk>/', views.edit_exam, name='edit_exam'),
    path('delete-exam/<int:pk>/', views.delete_exam, name='delete_exam'),
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]
