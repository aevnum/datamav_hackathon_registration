from django.urls import path
from .views import signup_view, CustomLoginView, home

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', home, name='home'),
]