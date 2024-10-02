from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

'''urlpatterns = [
    path('admin/users/', views.UserList.as_view(), name='user-list'),
    path('admin/users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('notes/', views.NoteList.as_view(), name='note-list'),
    path('notes/<int:pk>/', views.NoteDetail.as_view(), name='note-detail'),
]'''

urlpatterns = [
    path('', views.home, name='home'),
    path('note/<int:note_id>/', views.note_detail, name='note_detail'),
    path('note/new/', views.note_new, name='note_new'),
    path('note/<int:note_id>/edit/', views.note_edit, name='note_edit'),
    path('note/<int:note_id>/delete/', views.note_delete, name='note_delete'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.CustomLoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
]