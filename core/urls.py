from django.contrib import admin
from django.urls import path, include


from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
   openapi.Info(
      title="Project API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
  
    path('api/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('ckeditor/', include('ckeditor_uploader.urls')),


   path('', include('main.urls')),
]


if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL, document_root= settings.COMPRESS_ROOT if getattr(settings, 'COMPRESS_ENABLED', False) else settings.STATIC_ROOT,)

   urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)


