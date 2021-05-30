from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views 

from Global import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home ,name ="home" ),
    path('auth/login',views.loginuser ,name ="loginuser" ),
    path('logout/', views.logoutUser ,name ="logout"),

    path('Haberler/<slug:slug_text>',views.newsDetail ,name ="newsDetail" ),
    path('Duyurular/<slug:slug_text>',views.announcementDetail ,name ="announcementDetail" ),
    path('Ögrenci-haberler/<slug:slug_text>',views.studentNewsDetail ,name ="studentNewsDetail" ),
    path('İlanlar/<slug:slug_text>',views.advertisementsDetail ,name ="advertisementsDetail" ),
]


# file upload için python dosyalarından media rootumuza erişmek için 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_title = "Mersin Üniversitesi Admin Paneli "
admin.site.site_header = "Mersin Üniversitesi Admin Paneli "
admin.site.index_title = "Mersin Üniversitesi Admin Paneli'ne Hoşgeldiniz "
