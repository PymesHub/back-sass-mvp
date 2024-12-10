from abc import ABC, abstractmethod
from catalogs.domain.entitites import CatalogEntity

class CatalogRepository(ABC):

    @abstractmethod
    def create_catalog(self, name= str, user_id= str) -> CatalogEntity:
        pass

    @abstractmethod
    def catalog_exists_by_name(self, name: str) -> bool:
        pass