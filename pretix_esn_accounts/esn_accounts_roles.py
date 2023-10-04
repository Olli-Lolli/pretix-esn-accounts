from aenum import Enum
from django.utils.translation import gettext as _


class EsnAccountsRole(Enum):
    _init_ = "display cas"
    PRESIDENT = _("President"), "Local.president"
    VICE_PRESIDENT = _("Vice-President"), "Local.vicePresident"
    TREASURER = _("Treasurer"), "Local.treasurer"
    COMMUNICATION = _("Communication"), "Local.pr"
    BOARD_MEMBER = _("Board member"), "Local.regularBoardMember"
    SECRETARY = _("Secretary"), "Local.secretary"
    BOARD_SUPPORT = _("Board support"), "Local.boardSupport"
    WEBSITE_ADMIN = _("Website admin"), "Local.webmaster"
    PROJECTS_COORDINATOR = _("Projects Coordinator"), "Local.projectCoordinator"
    ESN_ACTIVITIES_MANAGER = _("ESN Activities manager"), "Local.activity"
    ESN_EVENT_MANAGER = _("ESN Events manager"), "Local.eventCoordinator"
    ESNCARD_MANAGER = _("ESNcard manager"), "Local.cardManager"
    ACTIVE_MEMBER = _("Active member"), "Local.activeMember"
    FORMER_MEMBER = _("Former member"), "Local.alumnus"

    @staticmethod
    def values():
        return [(e.name, e.display) for e in EsnAccountsRole]

    @staticmethod
    def from_cas_list(cas_list):
        return [role for role in EsnAccountsRole if role.cas in cas_list]
