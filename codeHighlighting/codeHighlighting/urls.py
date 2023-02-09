from django.contrib import admin
from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')), #The 'api-auth' pattern of the url can be anything we want it to be
    path('', include('snippets.urls')),
]
