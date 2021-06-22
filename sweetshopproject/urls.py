from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sweets/', include('sweets.urls')), 
    path('', RedirectView.as_view(url="sweets/")),    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
