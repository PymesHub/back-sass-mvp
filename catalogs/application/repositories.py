from catalogs.models import Catalog
from catalogs.domain.entitites import CatalogEntity
from catalogs.domain.repositories import CatalogRepository
import uuid

class DjangoCatalogRepository(CatalogRepository):

    def catalog_exists_by_name(self, name: str) -> bool:
        return Catalog.objects.filter(name=name).exists()

    def create_catalog(self, name: str, user_id: str) -> CatalogEntity:

        django_catalog = Catalog.objects.create(
            id=str(uuid.uuid4()),
            name=name,
            user_id=user_id
        )

        return CatalogEntity(
            id=django_catalog.id,
            name=django_catalog.name,
            user_id=django_catalog.user.id
        )