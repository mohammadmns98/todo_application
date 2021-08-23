from django.urls import path
from .views import register,login_view,logout_view


urlpatterns = [
    path('register/', register, name='user-create'),
    path('login/', login_view, name='user-login'),
    path('logout/', logout_view, name='user-logout'),

]
