from django.urls import path
from .views import NewsListView, NewsCreate, NewsUpdate, NewsDelete, NewsSearchView

urlpatterns = [
    path('news/', NewsListView.as_view(), name='news-list'),
    path('news/create/', NewsCreate.as_view(), name='news-create'),
    path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news-update'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news-delete'),
    path('news/search/', NewsSearchView.as_view(), name='news-search'), 
]