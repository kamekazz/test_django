from django.contrib import admin
from django.urls import include, path
from dotenv import load_dotenv
from django.conf import settings
from django.conf.urls.static import static
load_dotenv()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path('', include('users.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
