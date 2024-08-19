from rest_framework import serializers
from api.models import Student


'''
Validation priority : Validators > Field Level > Object Level validation
'''
# Validators
def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Name should start with r')

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[start_with_r]) 
    # Multiple functions can be used using comma like: [a,b, ... , c]
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        # print(instance.name)
        instance.name = validated_data.get('name', instance.name)
        # print(instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
    
    # Field Level Validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value
    
    # Object lave validation
    # Validating using multiple fields
    # Here data is a python dictionary
    def validate(self, data):
        city = data.get('city')
        name = data.get('name')
        if name.lower() == 'rafi' and city.lower() != 'dhaka' :
                raise serializers.ValidationError('City must be Dhaka')
        return data
    