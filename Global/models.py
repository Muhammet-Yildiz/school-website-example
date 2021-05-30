from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User 

# signals kullandık slug için 
from Main.utils import unique_slug_generator 
from django.db.models.signals import pre_save


class Banner(models.Model):
    image = models.ImageField( upload_to = "banner_imgs/",null = True,blank = True )
    title = models.CharField( max_length=300,verbose_name="title",default=" ")
    class Meta :
        verbose_name_plural = 'Afişler'
    def image_save(self):
        return mark_safe('<img src ="%s" width="50"  height ="50" /> ' % (self.image.url) )
    


class News(models.Model ) :  
    title = models.CharField(verbose_name="Haber Başlıgı ",max_length=100)
    content = models.TextField(max_length=10000) 
    image = models.ImageField( upload_to = "news_imgs/",null = True,blank = True )
    see = models.DecimalField(max_digits=7 ,decimal_places=2 ,verbose_name="Haberi Gören Kişi Sayısı")
    slug = models.SlugField(max_length=250,null=True , blank = True)  #url için urun adı gondermek için 
    created_date = models.DateTimeField(auto_now_add=True )
    class Meta :
        verbose_name_plural = 'Haberler'
    def __str__(self):
        return self.title
  
        
    def image_save(self):
        return mark_safe('<img src ="%s" width="50"  height ="50" /> ' % (self.image.url) )
    

def slug_generator(sender,instance, *args ,**kwargs ) : 
    if not instance.slug :
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator,sender =News)


class Announcements(models.Model ) :  
    title = models.CharField(verbose_name="Duyuru Başlıgı ",max_length=100)
    content = models.TextField(max_length=10000 ) 
    image = models.ImageField( upload_to = "news_imgs/",null = True,blank = True )
    see = models.DecimalField(max_digits=7 ,decimal_places=2 ,verbose_name="Duyuruyu Gören Kişi Sayısı")
    slug = models.SlugField(max_length=250,null=True , blank = True)  #url için urun adı gondermek için 
    created_date = models.DateTimeField(auto_now_add=True )
    class Meta :
        verbose_name_plural = 'Duyurular'
    def __str__(self):
        return self.title
    
    def image_save(self):
        return mark_safe('<img src ="%s" width="50"  height ="50" /> ' % (self.image.url) )
    
pre_save.connect(slug_generator,sender =Announcements)



class Students(models.Model ) :  
    title = models.CharField(verbose_name="Ögrenci Haber Başlıgı ",max_length=100)
    content = models.TextField(max_length=10000 ) 
    image = models.ImageField( upload_to = "news_imgs/",null = True,blank = True )
    see = models.DecimalField(max_digits=7 ,decimal_places=2 ,verbose_name="Ögrenci Haberi Gören Kişi Sayısı")
    slug = models.SlugField(max_length=250,null=True , blank = True)  #url için urun adı gondermek için 
    created_date = models.DateTimeField(auto_now_add=True )
    class Meta :
        verbose_name_plural = 'Ögrenci Haberleri'
    def __str__(self):
        return self.title
    
    def image_save(self):
        return mark_safe('<img src ="%s" width="50"  height ="50" /> ' % (self.image.url) )
    
pre_save.connect(slug_generator,sender =Students)


class Automatıons(models.Model ) :  
    title = models.CharField(verbose_name="Otomasyon Başlıgı ",max_length=100)
    image = models.ImageField( upload_to = "news_imgs/",null = True,blank = True )
    created_date = models.DateTimeField(auto_now_add=True )
    class Meta :
        verbose_name_plural = 'Otomasyonlar'
    def __str__(self):
        return self.title
    
    def image_save(self):
        return mark_safe('<img src ="%s" width="50"  height ="50" /> ' % (self.image.url) )
    




class Advertisementss(models.Model ) :  
    title = models.CharField(verbose_name="İlan Başlıgı ",max_length=100)
    content = models.TextField(max_length=10000 ) 
    image = models.ImageField( upload_to = "Advertisementss_imgs/",null = True,blank = True )
    see = models.DecimalField(max_digits=7 ,decimal_places=2 ,verbose_name="İlanı Haberi Gören Kişi Sayısı")
    slug = models.SlugField(max_length=250,null=True , blank = True)  #url için urun adı gondermek için 
    created_date = models.DateTimeField(auto_now_add=True )
    class Meta :
        verbose_name_plural = 'İLANLAR'
    def __str__(self):
        return self.title
    
    def image_save(self):
        return mark_safe('<img src ="%s" width="50"  height ="50" /> ' % (self.image.url) )
    
pre_save.connect(slug_generator,sender =Advertisementss)
