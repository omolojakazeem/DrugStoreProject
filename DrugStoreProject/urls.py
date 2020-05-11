from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('',include('store.urls')),
    path('drug/', include('drug.urls')),
    path('customer/', include('customer.urls')),
    path('sales/', include('sale.urls')),
    path('expenses/', include('expenses.urls')),
   # path('accounts/', include('django.contrib.auth.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
