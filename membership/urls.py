# membership/urls.py
from django.urls import path, include

urlpatterns = [
    path('membership/', include('membership.urls')),
    path('exclusive_content/', include('exclusive_content.urls'))
    # other URL patterns...
]
