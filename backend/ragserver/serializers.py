from rest_framework import serializers
from .models import Conversation

class ConvSerializer(serializers.ModelSerializer):
  class Meta:
    model = Conversation
    fields = '__all__'