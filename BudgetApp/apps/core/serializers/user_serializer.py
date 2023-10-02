from rest_framework import serializers

from BudgetApp.apps.core.models.user_model import UserModel

class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField()
    password = serializers.CharField(max_length = 100)
    name = serializers.CharField(max_length = 100)
    upi = serializers.CharField(max_length = 100)
    phone = serializers.CharField(max_length = 30)

    def create(self, validated_data):
        return UserModel.objects.create(**validated_data)


    class Meta:
        model = UserModel
        fields = '__all__'