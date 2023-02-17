from rest_framework import serializers
from .models import Whiskybase

class WhiskybaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Whiskybase
        fields = ('bottling_serie', 'stated_age', 'bottled', 'added_on', 'url', 'image', 'distillery', 'casknumber', 'Title', 'bottled_for', 'bottler', 'distilleries', 'casktype', 'market', 'category', 'strength', 'vintage', 'whiskybase_id', 'calculated_age', 'bottle_code', 'label', 'number_of_bottles', 'size', 'barcode')
