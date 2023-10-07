from rest_framework import serializers

from BudgetApp.apps.core.models.user_model import UserModel

class UserSerializer(serializers.ModelSerializer):

    email    = serializers.EmailField(required = True)
    password = serializers.CharField(max_length = 100, required = True)
    name     = serializers.CharField(max_length = 100, required = True)
    upi      = serializers.CharField(max_length = 100, required = False)
    phone    = serializers.CharField(max_length = 30, required = False)

    def create(self, validated_data):
        return UserModel.objects.create_user(**validated_data)
    
    def to_representation(self, instance):
        data = super(UserSerializer, self).to_representation(instance)
        data.pop('password', None)
        return data


    class Meta:
        model = UserModel
        fields = '__all__'