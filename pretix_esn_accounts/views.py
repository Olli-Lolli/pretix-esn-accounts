from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from pretix.base.models import Team
from pretix.control.permissions import OrganizerPermissionRequiredMixin

from .forms import TeamAssignmentRuleForm
from .models import EsnAccountsTeamAssignmentRule


class AssignmentRulesList(TemplateView, OrganizerPermissionRequiredMixin):
    """
    This view renders the team assignment rules settings page.
    """

    template_name = "pretix_esn_accounts/team_assignment_rules.html"
    permission = "can_change_organizer_settings"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        organizer = self.request.organizer
        context["teams"] = Team.objects.filter(organizer=organizer)
        context["assignmentRules"] = EsnAccountsTeamAssignmentRule.objects.filter(
            team__organizer=organizer
        )
        return context


class AssignmentRuleEditMixin(OrganizerPermissionRequiredMixin):
    model = EsnAccountsTeamAssignmentRule
    permission = "can_change_organizer_settings"

    def get_success_url(self):
        return reverse(
            "plugins:pretix_esn_accounts:team_assignment_rules",
            kwargs={"organizer": self.request.organizer.slug},
        )


class AssignmentRuleUpdateMixin(AssignmentRuleEditMixin):
    template_name = "pretix_esn_accounts/team_assignment_rule_edit.html"

    def get_form(self, form_class=None):
        return TeamAssignmentRuleForm(
            organizer=self.request.organizer, **self.get_form_kwargs()
        )

    def form_valid(self, form):
        super().form_valid(form)
        messages.success(self.request, _("The new assignment rule has been created."))
        return redirect(self.get_success_url())

    def form_invalid(self, form):
        messages.error(self.request, _("The assignment rule could not be created."))
        return super().form_invalid(form)


class AssignmentRuleCreate(AssignmentRuleUpdateMixin, CreateView):
    """
    This view enables the organizer to add a new team assignment rule.
    """


class AssignmentRuleEdit(AssignmentRuleUpdateMixin, UpdateView):
    """
    This view enables the organizer to update an existing team assignment rule.
    """


class AssignmentRuleDelete(AssignmentRuleEditMixin, DeleteView):
    """
    This view enables the organizer to delete an existing team assignment rule.
    """

    template_name = "pretix_esn_accounts/team_assignment_rule_delete.html"
