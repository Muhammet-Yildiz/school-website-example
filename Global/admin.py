from django.contrib import admin

# Register your models here.
from .models import * 

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display= ["image_save","content","title","slug","see"]
    list_display_links = ["image_save" ,"title"]
    list_editable = ["see"]
 
@admin.register(Announcements)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display= ["image_save","content","title","slug","see"]
    list_display_links = ["image_save" ,"title"]
    list_editable = ["see"]
 
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display= ["image_save","title"]
    list_display_links = ["title"]
 

@admin.register(Automatıons)
class AutomatıonsAdmin(admin.ModelAdmin):
    list_display= ["image_save","title"]
    list_display_links = ["title"]
  

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display= ["image_save","title"]
    list_display_links = ["title"]
 


@admin.register(Advertisementss)
class AdvertisementssAdmin(admin.ModelAdmin):
    list_display= ["image_save","title"]
    list_display_links = ["title"]
  