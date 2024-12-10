from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.application.serializer import UserRegistrationSerializer
from users.use_cases.register_user import RegisterUserUseCase
from users.application.repositories import DjangoUserRepository
from drf_yasg.utils import swagger_auto_schema

class UserView(APIView):

    @swagger_auto_schema(
            operation_description="Registra un nuevo usuario",
            request_body=UserRegistrationSerializer,
            responses={ 201: UserRegistrationSerializer, 
                        400: 'Invalid request data',
                        500: 'Internal server error'
                        }
    )

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user_repository = DjangoUserRepository()
            register_user_use_case = RegisterUserUseCase(user_repository)
            user_entity = register_user_use_case.execute(serializer.validated_data)
            return Response(
                { "message", f"Usuario {user_entity.username} registrado con éxito" },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)