from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone




class GpuStatus(models.Model):
    create_date= models.DateTimeField(default=timezone.now)
    server_name= models.CharField(max_length=30,default=None)
    server_group= models.CharField(max_length=30,default=None)
    label_gpu= models.CharField(max_length=30,default=None)
    index_gpu= models.CharField(max_length=10,default='')
    util_gpu= models.IntegerField(default=0)


class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_heading = models.CharField(max_length=250)
    article_body = models.TextField()


class Video(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(max_length=300)
    url = models.URLField()
    category = models.CharField(max_length=50)
    subcategory = models.TextField(max_length=50)
    author = models.TextField(max_length=50)

    # 함수형 컬럼
    def rating_average(self):
        sum = 0
        # 해당 video에 대한 rating에 대해서만
        ratings = Rating.objects.filter(video=self)
        for rating in ratings:
            sum = sum + rating.stars
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0

    # 함수형 컬럼
    def comments_list(self):
        allcomments = Rating.objects.filter(video=self)
        listallcomments = []
        for comment in allcomments:
            print(comment.comments)
            listallcomments.append(comment.comments)
        return listallcomments


class Rating(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField()
    comments = models.TextField(max_length=300)

    class Meta:
        # unique 설
        unique_together = (('user', 'video'),)
        # index 설정
        index_together = (('user', 'video'),)
