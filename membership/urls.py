# membership/urls.py
from django.urls import path, include

urlpatterns = [
    path('membership/', include('membership.urls'))
    # other URL patterns...
]
