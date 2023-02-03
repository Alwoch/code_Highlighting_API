from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

#format_suffix_patterns provide a clean way of referring to a specific format eg the API willnow be able to handleAPI URLs such as http://example.com/api/items/4.json
urlpatterns = format_suffix_patterns(urlpatterns)