from rest_framework.serializers import ModelSerializer
from .models import Name


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Name
        fields = '__all__'