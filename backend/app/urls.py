from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path("admin/", admin.site.urls),
    path("api/", include("orders.urls")),
    path("api/auth/", include("accounts.urls")),
    path("api/workout/", include("workout.urls")),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
