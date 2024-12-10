from abc import ABC, abstractmethod
from users.domain.entities import UserEntity

class UserRepository(ABC):
    @abstractmethod
    def create_user(self, user: UserEntity) -> UserEntity:
        pass
