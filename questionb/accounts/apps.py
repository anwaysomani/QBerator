from django.apps import AppConfig
from suit.apps import DjangoSuitConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

class SuitConfig(DjangoSuitConfig):
    layout = 'horizaontal'
