from django.contrib import admin
from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from users.views.register_view.register_views import UserView
from users.views.login_view.login_view import LoginView
from catalogs.views.catalog_view.catalog_view import CatalogView
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Back End Saas",
        default_version="v1",
        description="Api documentation from saas"
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('api/register/', UserView.as_view(), name='user-registration'),
    path('api/login/', LoginView.as_view(), name="user-login"),
    path('api/create_catalog/', CatalogView.as_view(), name="catalog-create"),
    path('api/catalog/<str:catalog_id>', CatalogView.as_view())
]
