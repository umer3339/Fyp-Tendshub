from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index,name="home"),
    path('fashion/<type>/<filename>/', views.fashion, name='fashion-page'),
    path('news/<type>/<filename>/', views.news, name='news-page'),
    path('tourism/<type>/<filename>/', views.tourism, name='tourism-page'),
    path('health/<type>/<filename>/', views.health, name='health-page'),

    path('about/', views.about, name='about-page'),
    path('contact/', views.contact, name='contact-page'),
    path('feedback/', views.feedback, name='feedback'),
    path('reddit/<filename>/',views.reddit,name="reddit"),
    path('error/', views.error, name='error'),
    path('search/', views.search, name='search')

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)