from django.db import models
from django.contrib.auth.models import User #login/ logout 
# Create your models here.

class Music(models.Model):
    music = models.AutoField()
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE) # fk 지정방법? 
    album = models.IntegerField()
    title = models.CharField()
    genre = models.IntergerField() 
    Release Date = models.DateField(auto_now=False,auto_now_add=True) 
    songwriting = models.CharField('작사가')  
    composer = models.CharField('작곡가')      
    music_arranger = models.CharField('편곡가') 
    music_length = models.IntegerField()
    sound_quality = models.CharField()  # charField 인가 Int인가 
    music_images_url = models.CharField('이미지 경로')
    video_path = models.CharField('파일 경로') # 테스트용으로 체크 
    total_streaming = models.IntergerField('총 재생수')
    music_price = models.IntegerField('음원가격')
    total_profit = models.IntergerField('총 음원수익')
    entainment = models.CharField('기획사',max_length="40")

class Artist(model.Model):
    email = models.EmailField(max_length=254)
    user_password = models.CharField('패스워드')
    authority_code = models.IntegerField("권한부여코드")
    nickname = models.CharField("닉네임")
    profile_url = models.CharField('이미지 경로')
    own_coin = models.IntegerField('소유하고 있는 코인')
    country_code = models.IntegerField('국적코드')

class Company(model.Model):
    email = models.ForeignKey('Artist',on_delete=models.CASCADE)
    company = models.IntegerField()  #pk 설정 
    company_name = models.IntegerField()
    compnay_representation = models.IntegerField() 

class Code(model.Model): 
    group_code = models.IntegerField()
    more_code = models.IntegerField()
    code_label = models.IntegerField() # 코드레이블 아직 파악 못함. 
       

    
