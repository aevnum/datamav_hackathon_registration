from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from .models import Teams, Problem, Submission
from django.contrib import messages
from .forms import SignupForm, LoginForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'index.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(request.POST)
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful signup
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'


def problem_statement(request):
    problems = Problem.objects.all()  # Fetch all problems from the database
    return render(request, 'problem_statements.html', {'problems': problems})

@login_required
def create_team(request):
    if request.method == 'POST':
        team_name = request.POST.get('team_name')
        if Teams.objects.filter(name=team_name).exists():
            alert = {"type": "error", "message": "A team with this name already exists."}
        else:
            team_id = f"TM{Teams.objects.count() + 1:05d}"  # Generate a unique team ID
            team = Teams.objects.create(name=team_name, team_id=team_id, created_by=request.user)
            team.members.add(request.user)
            alert = {"type": "success", "message": f"Team '{team_name}' created successfully with ID {team_id}."}
        return render(request, 'teams.html', {"alert": alert})
    return render(request, 'teams.html')

@login_required
def join_team(request):
    if request.method == 'POST':
        team_id = request.POST.get('team_id')
        try:
            team = Teams.objects.get(team_id=team_id)
            if request.user in team.members.all():
                alert = {"type": "info", "message": "You are already a member of this team."}
            else:
                # Assuming this is a placeholder for confirming with existing members
                # Add a process here if you want actual confirmation from team members
                team.members.add(request.user)
                alert = {"type": "success", "message": f"Successfully joined team '{team.name}'."}
        except Teams.DoesNotExist:
            alert = {"type": "error", "message": "Invalid Team ID. Please try again."}
        return render(request, 'teams.html', {"alert": alert})
    return render(request, 'teams.html')

@login_required
def team_management(request):
    return render(request, 'teams.html')

@login_required
def leave_team(request, team_id):
    if request.method == "POST":
        # Get the team object
        team = get_object_or_404(Teams, team_id=team_id)
        
        # Check if the user is a member of the team
        if request.user in team.members.all():
            # Remove the user from the team
            team.members.remove(request.user)
            messages.success(request, 'You have left the team successfully.')
        else:
            messages.warning(request, 'You are not a member of this team.')
        
        return render(request, 'teams.html')  # Redirect to the teams page
    return render(request, 'teams.html') # Fallback redirect if not POST


@login_required
def submit_solution(request):
    alert = None

    if request.method == 'POST':
        team_id = request.POST.get('team')
        problem_id = request.POST.get('problem')
        file = request.FILES.get('file')

        try:
            team = Teams.objects.get(id=team_id)
            problem = Problem.objects.get(id=problem_id)
            submission = Submission.objects.create(team=team, problem=problem, file=file)
            alert = {"type": "success", "message": "Submission successful!"}
        
        except Teams.DoesNotExist:
            alert = {"type": "error", "message": "You are not in a team."}
        except Problem.DoesNotExist:
            alert = {"type": "error", "message": "Selected problem does not exist."}

    teams = Teams.objects.all()
    problems = Problem.objects.all()
    context = {"teams": teams, "problems": problems, "alert": alert}

    return render(request, 'submissions.html', context)


