from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Project, Task, CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "office", "date_created", "date_updated", "active")
    list_filter = ("active", "date_created", "date_updated", "office")
    search_fields = ("name", "office")
    ordering = ("-date_created",)
    readonly_fields = ("date_created", "date_updated")


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", "responsible", "priority", "status", "start_date", "due_date", "project"
    )
    list_filter = ("priority", "status", "start_date", "due_date")
    search_fields = ("name", "responsible", "project__name")
    ordering = ("-start_date",)
    autocomplete_fields = ("project",)
    readonly_fields = ("id",)
