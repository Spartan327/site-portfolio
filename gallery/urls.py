from django.urls import path

from .views import image_id, VectorDrawingCreateView, GalleryView, GalleryByTagView

app_name = 'gallery'
urlpatterns = [
    #path('', index, name='index'),
    path('', GalleryView.as_view(), name='index'),
    path('add/', VectorDrawingCreateView.as_view(), name='add'),
    path('<int:pk>/', image_id, name='image_id'),
    path('<str:tag>/', GalleryByTagView.as_view(), name='by_tag')
    #path('<str:tag>/', by_tag, name='by_tag'),
]
