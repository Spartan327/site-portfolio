from django.urls import path

from .views import by_tag, index, image_id, image_id_delete, VectorDrawingCreateView

urlpatterns = [
    path('', index, name='index'),
    path('add/', VectorDrawingCreateView.as_view(), name='add'),
    path('<int:pk>/delete', image_id_delete, name='image_id_delete'),
    path('<int:pk>/', image_id, name='image_id'),
    path('<str:tag>/', by_tag, name='by_tag'),
]
