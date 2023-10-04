from django.forms import ModelForm

from .models import EsnAccountsTeamAssignmentRule


class TeamAssignmentRuleForm(ModelForm):
    def __init__(self, organizer, *args, **kwargs):
        super(TeamAssignmentRuleForm, self).__init__(*args, **kwargs)
        self.fields["team"].queryset = self.fields["team"].queryset.filter(
            organizer=organizer
        )

    class Meta:
        model = EsnAccountsTeamAssignmentRule
        fields = ["team", "esn_section", "local_roles"]
