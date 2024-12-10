from dataclasses import dataclass
import uuid

@dataclass
class CatalogEntity:
    id: uuid.UUID
    name: str
    user_id: uuid.UUID

@dataclass
class Category:
    id: uuid.UUID
    name: str
    catalog_id: uuid.UUID