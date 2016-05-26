from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse

def upload_location(instance, filename):                                        #tells me where files are going
    return "%s/%s.%s" %(instance.id, filename)

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=140)
    image = models.FileField(upload_to="upload_location", null=True, blank=True)
    text = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)           #updated time
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)         #created time

    def __unicode__(self):                                                      #python best practice
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})
        #return "/blog/%s/" %(self.id)

    class Meta:
        ordering = ["-timestamp", "-updated"]
