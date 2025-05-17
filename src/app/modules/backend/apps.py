from django.apps import AppConfig


class BackendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.app.modules.backend'

    def ready(self):
        from .infrastructure.medications.models.medications_model import MedicationsModel
        from .infrastructure.laboratory.models.laboratory_model import LaboratoryModel
        from .infrastructure.provider.models.provider_model import ProviderModel
        from .infrastructure.lot.models.lot_model import LotModel
