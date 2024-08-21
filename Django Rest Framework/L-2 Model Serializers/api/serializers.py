from rest_framework import serializers

from api.models import Student


'''
Validation priority : Validators > Field Level > Object Level validation

'''


class StudentSerializer(serializers.ModelSerializer):
    
    # Validators
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name should start with r')
    
    # When we use read_only=True we cannot update it
    name = serializers.CharField(validators=[start_with_r])
    class Meta:
        model = Student
        # fields = '__all__'
        fields = ['name', 'roll', 'city']
        # exclude = ['id']
        # read_only_fields = ['name', 'roll']
        # extra_kwargs = {'name': {'read_only': True}, 'roll': {'read_only': True}}
    
    # Field Level validation
    def validate_roll(self, value):
        if value >=200:
            raise serializers.ValidationError('Seat Full')
        return value
    
    # object level validation
    def validate(self, data):
        # name = data.get('name')
        city = data.get('city')
        if city.lower() != 'dhaka':
            raise serializers.ValidationError('City must be Dhaka')
        # Any vlidation logic
        return data
    
    