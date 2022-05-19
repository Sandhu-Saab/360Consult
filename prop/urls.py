from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = "prop"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    # path("okk", views.okk),
    path(r"okk", views.okk, name='okk'),
    path("service", views.service, name="service"),
    path("contact", views.contact, name="contact")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)