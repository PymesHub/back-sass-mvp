from django.contrib.auth import get_user_model
from users.domain.repositories import UserRepository
from users.domain.entities import UserEntity

User = get_user_model()


class DjangoUserRepository(UserRepository):
    
    def user_exists_by_email(self, email: str) -> bool:
        return User.objects.filter(email=email).exists()

    def create_user(self, user: UserEntity) -> UserEntity:
        
        django_user = User.objects.create_user(
            username=user.email,
            email=user.email,
            password=user.password,
            first_name=user.first_name,
            last_name=user.last_name,
            telephone=user.telephone,
            country=user.country
        )

        return UserEntity(
            username=django_user.username,
            email=django_user.email,
            password="",
            first_name=django_user.first_name,
            last_name=django_user.last_name,
            telephone=django_user.telephone,
            country=django_user.country
        )