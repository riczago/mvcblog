from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
    title = models.CharField(max_length=140)
    text = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)           #updated time
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)         #created time

    def __unicode__(self):                                                      #python best practice
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})
        #return "/blog/%s/" %(self.id)
