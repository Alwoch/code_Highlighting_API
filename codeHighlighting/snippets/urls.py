from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.api_root),
    path('snippets/', views.SnippetList.as_view(),name='snippet-list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(),name='snippet-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(),name='user-detail'),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(),name='snippet-highlight'),
]

#format_suffix_patterns provide a clean way of referring to a specific format eg the API will now be able to handleAPI URLs such as http://example.com/api/items/4.json
urlpatterns = format_suffix_patterns(urlpatterns)