from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='students'

urlpatterns = [
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('signup', views.signup, name='signup'),
    path('', views.StudentListView.as_view(), name='student-index'),
    path('add-student', views.StudentCreateView.as_view(), name='add-student'),
    path('<int:pk>/update-student', views.StudentUpdateView.as_view(), name='update-student'),
    path('<int:pk>/delete-student', views.StudentDeleteView.as_view(), name='delete-student'),
]