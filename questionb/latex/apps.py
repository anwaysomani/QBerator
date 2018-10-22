from django.apps import AppConfig
from suit.app import DjangoSuitConfig


class LatexConfig(AppConfig):
    name = 'latex'
    verbose_name = 'Configuration Fields'

class SuitConfig(DjangoSuitConfig):
    layout = 'vertical'
