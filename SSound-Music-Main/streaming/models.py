from django.db import models
from django.contrib.auth.models import User #login/ logout 
# Create your models here.

class Music(models.Model):
    music_number = models.IntegerField()
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE) # fk 지정방법? 
    album = models.IntegerField()
    title = models.CharField(max_length=30)
    genre = models.IntegerField() 
    Release_Date = models.DateField(auto_now=False,auto_now_add=True) 
    songwriting = models.CharField('작사가',max_length=30)  
    composer = models.CharField('작곡가',max_length=30)      
    music_arranger = models.CharField('편곡가',max_length=30) 
    music_length = models.IntegerField()
    sound_quality = models.CharField(max_length=10)  # charField 인가 Int인가 
    music_images_url = models.CharField('이미지 경로',max_length=30)
    video_path = models.CharField('파일 경로',max_length=40) # 테스트용으로 체크 
    total_streaming = models.IntegerField('총 재생수')
    music_price = models.IntegerField('음원가격')
    total_profit = models.IntegerField('총 음원수익')
    entainment = models.CharField('기획사',max_length=30)

class Artist(models.Model):
    email = models.EmailField(max_length=254)
    user_password = models.CharField('패스워드',max_length=40)
    authority_code = models.IntegerField("권한부여코드")
    nickname = models.CharField("닉네임",max_length=30)
    profile_url = models.CharField('이미지 경로',max_length=50)
    own_coin = models.IntegerField('소유하고 있는 코인')
    country_code = models.IntegerField('국적코드')

class Company(models.Model):
    email = models.ForeignKey('Artist',on_delete=models.CASCADE)
    company = models.IntegerField()  #pk 설정 
    company_name = models.IntegerField()
    compnay_representation = models.IntegerField() 

class Code(models.Model): 
    group_code = models.IntegerField()
    more_code = models.IntegerField()
    code_label = models.IntegerField() # 코드레이블 아직 파악 못함. 
       

    
