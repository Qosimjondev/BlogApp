from django.urls import path
from .views import Home, About, Detail, Create, Update, Delete
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
path('', Home.as_view(), name='home'),
path('about/', About.as_view(), name='about'),
path('post/<int:pk>/', Detail.as_view(), name='detail'),
path('post/create/', Create.as_view(), name='create'),
path('post/<int:pk>/edit/', Update.as_view(), name='edit'),
path('post/<int:pk>/delete/', Delete.as_view(), name='delete'),
]

if settings.DEBUG:
	urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)