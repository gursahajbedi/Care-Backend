from rest_framework import serializers
from .models import Booking, RateNanny
from django.contrib.auth import get_user_model

user = get_user_model()

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class NannyGetBookings(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['user', 'domain_name', 'day', 'from_time', 'to_time', "no_of_pets","no_of_children","pet_types","child_types", 'price', 'address', 'district', 'postalcode', 'country', 'other_instructions']


class PostRatings(serializers.ModelSerializer):
    class Meta:
        model = RateNanny
        fields = '__all__'