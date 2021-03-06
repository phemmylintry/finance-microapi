from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import permissions
from drf_yasg.views import get_schema_view, SwaggerUIRenderer
from drf_yasg import openapi

SwaggerUIRenderer.template = 'drf-yasg.html'

API_TITLE = 'Finance API'
API_DESCRIPTION = 'A Web API for list of available Locations'
#re-push
schema_view = get_schema_view(
   openapi.Info(
      title="Currency Convert API",
      default_version='v1',
      description="An API that works as a currency converter",
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   url='https://finance.microapi.dev/v1/',
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('documentation/', schema_view.as_view(), {'format': '.json'}, name='schema-json'),
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION, permission_classes=(permissions.AllowAny,))),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('v1/', include('currency_converter.urls')),
]
