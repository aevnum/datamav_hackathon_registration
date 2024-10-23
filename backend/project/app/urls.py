from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import signup_view, CustomLoginView, home, problem_statement

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', home, name='home'),
    path('problem_statement/', problem_statement, name='problem_statement'),
]
