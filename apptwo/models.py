from django.db import models
# Create your models here.
class usernames(models.Model):
    real_name = models.CharField(max_length=255, unique=True)
    fieldid = models.CharField(unique=True,max_length=1000,)
    tz = models.TextField(blank=True, default='')

    class meta:
        db_table = "usernames"


class activity_periods1(models.Model):
    activity_periods = models.ForeignKey(usernames,on_delete=models.CASCADE,related_name="activity_periods1")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class meta:
          db_table = "activity_periods1"
