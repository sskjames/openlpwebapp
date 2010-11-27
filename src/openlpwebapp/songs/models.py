from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=255)
    alternate_title = models.CharField(max_length=255)
    lyrics = models.TextField()
    comments = models.TextField()
    search_title = models.CharField(max_length=255)
    search_lyrics = models.TextField()
    
    def __unicode__(self):
        return u'%s' % (self.title)
    
    class Meta:
        db_table = 'songs'
        ordering = ['title']
    
class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    display_name = models.CharField(max_length=128)
    
    def __unicode__(self):
        return u'%s' % (self.display_name)
    
    class Meta:
        db_table = "authors"

