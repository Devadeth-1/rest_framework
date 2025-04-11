from rest_framework import serializers
from study.models import Students

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

    def validate(self, data):
        spl_chars = "!@#$%^&*()-+?_=,<>/"
        
        if any(c in spl_chars for c in data['name']):
            raise serializers.ValidationError("Name should not have special characters")
        
        if data['age'] < 18:
            raise serializers.ValidationError("Age should not be less than 18")
        
        return data