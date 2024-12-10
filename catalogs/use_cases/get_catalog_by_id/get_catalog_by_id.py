from catalogs.domain.repositories import CatalogRepository
from catalogs.domain.entitites import CatalogEntity
from catalogs.application.exceptions import CatalogNotFoundException

class GetCatalogById:

    def __init__(self, catalog_repository: CatalogRepository):
        self.catalog_repository = catalog_repository

    def execute(self, catalog_id: str) -> CatalogEntity:
        
        try:
            catalog = self.catalog_repository.get_catalog_by_id(catalog_id=catalog_id)
            return catalog
        
        except CatalogNotFoundException as e:
            raise e