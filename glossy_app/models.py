from django.db import models

from datetime import datetime

# Create your models here.

class Language(models.Model):
    language = models.CharField('language name', max_length=200, unique=True)
    author = models.CharField('author', max_length=200)
    silcode = models.CharField('silcode', max_length=3)
    notes = models.TextField('language notes')
    geolat = models.FloatField('location lat coordinate', default=0)
    geolon = models.FloatField('location lon coordinate', default=0)
    resources = models.TextField('language resources')
    def __unicode__(self):
        return self.language
    

class Language_version(models.Model):
    language = models.ForeignKey(Language, related_name='Version of')
    date = models.DateTimeField('revised date', default=datetime.now)
    notes = models.TextField('version notes')
    def __unicode__(self):
        return self.language.language + str(self.date)
    

class Word(models.Model):
    word = models.CharField('actual word', max_length=200)
    language = models.ForeignKey(Language, related_name='language in')
    def __unicode__(self):
        return self.word
    

class Definition(models.Model):
    word = models.ForeignKey(Word, related_name='definition of')
    definition = models.TextField('definition')
    image_url = models.CharField('related image', max_length=200, blank=True)
    part_of_speech = models.CharField('part of speech', max_length=50, blank=True)
    ipa = models.CharField(max_length=200, blank=True)
    example = models.TextField('example usage', blank=True)
    annotations = models.TextField('grammatical notes',)
    sound_file = models.CharField('sound file', max_length=200, blank=True)
    def __unicode__(self):
        return self.word.word + " " + self.definition
    

class Comment(models.Model):
    word = models.ForeignKey(Word, related_name='comment on')
    author = models.CharField('author of comment', max_length=200)
    date = models.DateTimeField('published time', default=datetime.now)
    comment = models.TextField('actual comment')
    approved = models.BooleanField('has been approved',default=False)
    def __unicode__(self):
        return "comment on " + self.word + " by " + self.author
    

