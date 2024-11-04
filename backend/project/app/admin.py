from django.contrib import admin

# Register your models here.
# admin.py

from django.contrib.auth.admin import UserAdmin
from .models import Problem, User, Teams, Submission

# Register the Problem model with custom display options
@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description','img')
    search_fields = ('name', 'category')
    list_filter = ('category',)

# Register the custom User model with extended UserAdmin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (  # Add custom fields to the admin panel
        (None, {'fields': ('date_of_birth', 'city', 'college')}),
    )
    list_display = ('username', 'email', 'date_of_birth', 'city', 'college', 'is_staff')
    search_fields = ('username', 'email', 'city', 'college')

# Register the Teams model with custom options
@admin.register(Teams)
class TeamsAdmin(admin.ModelAdmin):
    list_display = ('name', 'team_id', 'created_by')
    search_fields = ('name', 'team_id', 'created_by__username')
    filter_horizontal = ('members',)  # Allows a horizontal filter for members
    list_filter = ('created_by',)

# Register the Submission model with custom options
@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('team', 'problem', 'submission_time')
    search_fields = ('team__name', 'problem__name')
    list_filter = ('submission_time',)
    date_hierarchy = 'submission_time'  # Adds a time-based drill-down navigation
