from django.urls import path

from . import auth_backend, views

urlpatterns = [
    path("cas_login", auth_backend.return_from_sso, name="cas.response"),
    path(
        "control/organizer/<str:organizer>/teams/assignment_rules",
        views.AssignmentRulesList.as_view(),
        name="team_assignment_rules",
    ),
    path(
        "control/organizer/<str:organizer>/teams/assignment_rules/add",
        views.AssignmentRuleCreate.as_view(),
        name="team_assignment_rules.add",
    ),
    path(
        "control/organizer/<str:organizer>/teams/assignment_rules/<str:pk>/edit",
        views.AssignmentRuleEdit.as_view(),
        name="team_assignment_rules.edit",
    ),
    path(
        "control/organizer/<str:organizer>/teams/assignment_rules/<str:pk>/delete",
        views.AssignmentRuleDelete.as_view(),
        name="team_assignment_rules.delete",
    ),
]
