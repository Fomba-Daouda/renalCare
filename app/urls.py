
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import PatientViewSet
from app.views import MedecinViewSet
from app.views import ProfileViewSet
from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register(r"patients", PatientViewSet)
router.register(r"medecins", MedecinViewSet)
router.register(r"profiles", ProfileViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
