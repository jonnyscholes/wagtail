from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class WagtailSnippetsTestsAppConfig(AppConfig):
    name = 'wagtail.tests.snippets'
    label = 'snippetstests'
    verbose_name = _("Wagtail snippets tests")
