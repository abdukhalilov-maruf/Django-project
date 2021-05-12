from django.urls import path
from . import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
   path('', views.index, name='index'),
   path('<int:pk>', views.NewsDetailView.as_view(), name='post'),
   path('works', views.works, name='works'),

   path('login', views.login_user, name='login'),
   path('logout', LogoutView.as_view(template_name='maina/login.html'), name='logout'),
   path('register', views.register_user, name='register'),
]
