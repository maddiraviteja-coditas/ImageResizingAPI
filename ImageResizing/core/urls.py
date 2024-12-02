from django.urls import path
from .views import HomeView, ImageResizingView


urlpatterns = [
    path("home", HomeView.as_view()),
    path("image-resizing", ImageResizingView.as_view())
]
