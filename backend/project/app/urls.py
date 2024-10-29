from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import signup_view, CustomLoginView, home, problem_statement, team_management, create_team, join_team, submit_solution

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', home, name='home'),
    path('problem_statement/', problem_statement, name='problem_statement'),
    path('teams/', team_management, name='team_management'),  # Main team page
    path('teams/create/', create_team, name='create_team'),    # Create team
    path('teams/join/', join_team, name='join_team'), 
    path('submit/', submit_solution, name='submit_solution'),
]
