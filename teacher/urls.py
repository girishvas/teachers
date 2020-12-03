from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required
from teacher import views


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    # url(r'^products/$', login_required(views.ManageProductView.as_view()), name='products'),
    path('add-teacher/', AddTeacher.as_view(), name='add-teacher'),
    path('teacher/<int:id>/', TeacherDetails.as_view(), name='teacher'),
    path('validate_email/', views.validate_email, name='validate_email'),
    path('validate_mobile/', views.validate_mobile, name='validate_mobile'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]