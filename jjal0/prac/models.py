from django.db import models

# Create your models here.

class Jjal(models.Model):
  jjal_text = models.CharField(max_length=200)
  cnt = models.IntegerField(default=0)
  pub_date = models.DateTimeField(auto_now_add=True)
  files = models.ImageField(upload_to='images/')
  def __unicode__(self):
            return u"%s" % self.jjal_text