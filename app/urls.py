from django.urls import path
from .views import ProjectViewSet, TaskViewSet, UserViewSet

urlpatterns = [
    path(
        "projects/",
        ProjectViewSet.as_view({"get": "list", "post": "create"}),
        name="project-list",
    ),
    path(
        "projects/<int:pk>/",
        ProjectViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "delete": "destroy",
                "patch": "partial_update",
            }
        ),
        name="project-detail",
    ),
    path(
        "tasks/",
        TaskViewSet.as_view({"get": "list", "post": "create"}),
        name="task-list",
    ),
    path(
        "tasks/<int:pk>/",
        TaskViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="task-detail",
    ),
    path("login/", UserViewSet.as_view({"post": "login"}), name="login"),
]
