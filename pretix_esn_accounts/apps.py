from django.utils.translation import gettext_lazy

from . import __version__

try:
    from pretix.base.plugins import PluginConfig
except ImportError:
    raise RuntimeError("Please use pretix 2.7 or above to run this plugin!")


class PluginApp(PluginConfig):
    default = True
    name = "pretix_esn_accounts"
    verbose_name = "Pretix ESN Accounts SSO Plugin"

    class PretixPluginMeta:
        name = gettext_lazy("Pretix ESN Accounts SSO Plugin")
        author = "Oliver Fuhr"
        description = gettext_lazy(
            "This is a plugin for pretix that provides an authentication backend for ESN "
            "Accounts SSO and allows to define rules to assign users automatically to teams "
            "based on their role in ESN"
        )
        visible = False
        version = __version__
        category = "INTEGRATION"
        compatibility = "pretix>=2.7.0"

    def ready(self):
        from . import signals  # NOQA
