from rest_framework import serializers
from .models import *

class Items_Serializers(serializers.ModelSerializer):

    class Meta:

        model = Items
        fields = '__all__'

class Items_Serializers2(serializers.ModelSerializer):

    class Meta:

        model=Items
        fields='__all__'