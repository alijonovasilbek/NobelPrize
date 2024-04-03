from  django.urls import  path
from .views import *

urlpatterns=[
    path('articles/<int:pk>/edit/',ArticleUpdateView.as_view(),name='article_edit'),

    path('<int:pk>/delete/',ArticleDeleteView.as_view(),name='article_delete'),
    path('new/',ArticleCreateView.as_view(), name='article_new'),
    path('', ArticlesListView.as_view(),name='article_list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/comment/', AddCommentView.as_view(), name='add_comment_to_article'),


]