from catalogs.models import Catalog
from catalogs.domain.entitites import CatalogEntity
from catalogs.domain.repositories import CatalogRepository
from catalogs.application.exceptions import CatalogNotFoundException
import uuid

class DjangoCatalogRepository(CatalogRepository):

    def catalog_exists_by_name(self, name: str) -> bool:
        return Catalog.objects.filter(name=name).exists()

    def get_catalog_by_id(self, catalog_id: str) -> CatalogEntity:
        try:
            catalog = Catalog.objects.get(id=catalog_id)
            return CatalogEntity(id= catalog.id, name= catalog.name, user_id= catalog.user_id)
        
        except  Catalog.DoesNotExist:
            raise CatalogNotFoundException(f"Catalog wit ID {catalog_id} not found.")

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