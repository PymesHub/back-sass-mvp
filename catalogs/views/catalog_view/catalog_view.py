from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from catalogs.application.repositories import DjangoCatalogRepository
from catalogs.application.serializer import CatalogSerializer
from catalogs.use_cases.catalog import CreateCatalogUseCase
from drf_yasg.utils import swagger_auto_schema


class CatalogView(APIView):
    permission_classes = [IsAuthenticated]


    @swagger_auto_schema(
            operation_description="Crear un nuevo cátalogo",
            request_body=CatalogSerializer
    )
    def post(self, request, *args, **kwargs):
        
        serializer = CatalogSerializer(data=request.data)

        if serializer.is_valid():
            validated_data = serializer.validated_data

            catalog_repository = DjangoCatalogRepository()
            create_catalog_use_case = CreateCatalogUseCase(catalog_repository)
            user = request.user
            
            catalog_entity = create_catalog_use_case.execute(validated_data, user.id)
            return Response(
                {"message": f"Cátalogo {catalog_entity.name} creado"},
                status=status.HTTP_201_CREATED
            )
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)