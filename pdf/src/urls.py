from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import ImportPdf, TestApi, ImportSeptemberPdf

app_name = 'src'

urlpatterns = [
                  path('import-pdf/', ImportPdf.as_view(), name='import-pdf'),
                  path('september/', ImportSeptemberPdf.as_view(), name='september'),
                  path('test/', TestApi.as_view(), name='test')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
