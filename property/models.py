from django.db import models

class Property(models.Model):
    url = models.URLField(max_length=1024)
    seo_title = models.CharField(max_length=255)
    seo_description = models.TextField()
    url_image = models.URLField(max_length=1024)
    data_price = models.CharField(max_length=255)
    data_room = models.IntegerField()
    data_area = models.FloatField()
    data_bath = models.IntegerField()
    data_type = models.CharField(max_length=100)
    in_visit = models.BooleanField(default=False)
    need_call = models.BooleanField(default=False)
    visit_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.seo_title
