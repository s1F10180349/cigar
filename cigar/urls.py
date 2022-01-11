from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('today/', views.index1, name='index1'),
    path('redirect/', views.redirect_t, name='redirect_t'),
    path('<int:article_id>/delete', views.delete, name='delete'),
    path('<int:atrticle_id>/update', views.update, name='update')
]