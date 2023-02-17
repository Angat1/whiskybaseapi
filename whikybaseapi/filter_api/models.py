from django.db import models

class Whiskybase(models.Model):
    """
    This class represents the Whiskybase model. 
    Each instance of the model represents a single whisky record in the database.
    """
    bottling_serie = models.CharField(max_length=255, blank=True, null=True)
    stated_age = models.CharField(max_length=255, blank=True, null=True)
    bottled = models.CharField(max_length=255, blank=True, null=True)
    added_on = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    distillery = models.CharField(max_length=255, blank=True, null=True)
    casknumber = models.CharField(max_length=255, blank=True, null=True)
    Title = models.CharField(max_length=255, blank=True, null=True)
    bottled_for = models.CharField(max_length=255, blank=True, null=True)
    bottler = models.CharField(max_length=255, blank=True, null=True)
    distilleries = models.CharField(max_length=255, blank=True, null=True)
    casktype = models.CharField(max_length=255, blank=True, null=True)
    market = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    strength = models.CharField(max_length=255, blank=True, null=True)
    vintage = models.CharField(max_length=255, blank=True, null=True)
    whiskybase_id = models.CharField(max_length=255, blank=True, null=True)
    calculated_age = models.CharField(max_length=255, blank=True, null=True)
    bottle_code = models.CharField(max_length=255, blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    number_of_bottles = models.CharField(max_length=255, blank=True, null=True)
    size = models.CharField(max_length=255, blank=True, null=True)
    barcode = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['bottling_serie','stated_age','bottled','added_on','url','image','distillery','casknumber','Title','bottled_for','bottler','distilleries','casktype','market','category','strength','vintage','whiskybase_id','calculated_age','bottle_code','label','number_of_bottles','size','barcode'])
        ]
