from django.db import models
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
from pretix.base.models import Team

from pretix_esn_accounts.esn_accounts_roles import EsnAccountsRole


class EsnAccountsTeamAssignmentRule(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    esn_section = models.CharField(max_length=100, verbose_name=_("ESN section"))
    local_roles = MultiSelectField(
        max_length=300,
        choices=EsnAccountsRole.values(),
        verbose_name=_("Local section role"),
    )

    class Meta:
        verbose_name = _("Team assignment rule")
