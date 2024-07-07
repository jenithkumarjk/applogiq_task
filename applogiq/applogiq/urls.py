
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.views import *

urlpatterns = [
    path('', error_cards_view),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
