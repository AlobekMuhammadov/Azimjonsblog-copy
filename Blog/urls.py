from django.contrib import admin
from django.urls import path
from asosiy.views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('blog/', blog),
    # path('maqola/', maqola),
    path('blog/<int:son>/', bitta_blog),
    path('about/', about),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




