from catalogs.domain.repositories import CatalogRepository
from catalogs.domain.entitites import CatalogEntity
from catalogs.application.exceptions import CatalogAlreadyExistsException


class CreateCatalogUseCase:

    def __init__(self, catalog_repository: CatalogRepository):
        self.catalog_repository = catalog_repository
    
    def execute(self, data: dict, user_id: str) -> CatalogEntity:

        if self.catalog_repository.catalog_exists_by_name(name=data["name"]):
            raise CatalogAlreadyExistsException("Este nombre de cátalogo existe")

        catalog_entity = { "name": data["name"], "user_id": user_id }

        return self.catalog_repository.create_catalog(catalog_entity["name"], catalog_entity["user_id"])