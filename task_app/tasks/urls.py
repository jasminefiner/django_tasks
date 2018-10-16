from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.tasks, name='tasks'),
    path('accounts/login/',
         auth_views.LoginView.as_view(
                                template_name='login.html',
                                redirect_field_name='tasks',
                                redirect_authenticated_user=True
                                ),
         name='login'
         ),
    path('accounts/logout', auth_views.LogoutView.as_view(
                                next_page='home',
                                template_name='logout.html',
                                redirect_field_name='home'),
        name='logout'
    )

]
