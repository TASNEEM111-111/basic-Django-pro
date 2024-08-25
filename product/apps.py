from django.apps import AppConfig
from suit.apps import DjangoSuitConfig


class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product'
    
class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'
