from django.db import models

class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class Entry(models.Model):

    title = models.CharField(max_length = 200)
    subtitle = models.CharField(max_length = 200)
    body = models.TextField()
    publish = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    slug = models.CharField(max_length = 200, unique=True, default="")

    objects = EntryQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]
