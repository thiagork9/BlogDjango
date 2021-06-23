from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='list'), #não passando argumento nenhum, cai na listagem dos posts (list view)
    path('<slug:slug>/', views.PostDetalView.as_view(), name='detail'), #passando o argumento (slug), cai no post correspondente
]