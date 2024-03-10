from django.urls import path
from . import views
from .views import HomeView, \
    ArticleDetailView, AddPostView, \
    EditPostView, DeletePostView, \
    CategoryView, AddCategoryView, EditCategoryView, \
    CategoryHomeView, DeleteCategoryView

urlpatterns = [
   path('', views.homeblog, name='home2'),
   path('', ArticleDetailView.as_view(), name='article-detail'),
   path('home/', HomeView.as_view(), name="home"),
   path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
   path('add_post/', AddPostView.as_view(), name='add-post'),
   path('article/edit/<int:pk>/', EditPostView.as_view(), name='edit-post'),
   path('article/<int:pk>/remove/', DeletePostView.as_view(), name='delete-post'),
   path('add_category/', AddCategoryView.as_view(), name='add-category'),
   path('category/edit/<int:pk>/', EditCategoryView.as_view(), name='edit-category'),
   path('category/', CategoryHomeView.as_view(), name='category-list'),
   path('category/<int:pk>/remove/', DeleteCategoryView.as_view(), name='delete-category'),
   path('category/<str:cats>/', CategoryView, name='category'),
]
