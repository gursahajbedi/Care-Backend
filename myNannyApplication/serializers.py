
from rest_framework import serializers
from .models import Domain, Service, AdditionalService, Language, Profile, AgeRange, WorkExperience, DaySchedule, PetType

class AgeRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeRange
        fields = ['range_name']

class PetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetType
        fields = ['pet_name']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['name']

class AdditionalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalService
        fields = ['name']

class DayScheduleSerializer(serializers.ModelSerializer):
    day = serializers.CharField()
    from_time = serializers.TimeField(source='start_time')
    to_time = serializers.TimeField(source='end_time')
    class Meta:
        model = DaySchedule
        fields = ['day', 'from_time', 'to_time']

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['name']

class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ['start_year', 'end_year', 'job_place']

class DomainSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True)
    additional_services = AdditionalServiceSerializer(many=True)
    schedules = DayScheduleSerializer(many=True)
    work_experiences = WorkExperienceSerializer(many=True)
    age_ranges = AgeRangeSerializer(many=True, required=False)
    pet_types = PetTypeSerializer(many=True, required=False)

    class Meta:
        model = Domain
        fields = ['name', 'services', 'additional_services', 'work_experiences', 'one_time_price', 'recurring_price', 'increment', 'schedules', 'age_ranges', 'pet_types', 'domin_about', 'years_of_experience', 'no_of_child']

# class VerificationSerializer(serializers.ModelSerializer):
#     domains = DomainSerializer(many=True, required=False)
#     languages = LanguageSerializer(many=True)
    
#     class Meta:
#         model = Profile
#         fields = ['id','user', 'display_name', 'user_type',  'organisation_url', 'organisation_name', 'refrence1_name', 'refrence1_phone', 'refrence2_name', 'refrence2_phone', 'address_proof', 'police_certificate', 'driving_license_proof', 'status', 'age', 'state', 'pincode', 'gender', 'general_about', 'languages', 'domains']

#     def create(self, validated_data):
#         languages_data = validated_data.pop('languages', [])
#         domains_data = validated_data.pop('domains', [])
        

#         profile = Profile.objects.create(**validated_data)
#         for language_data in languages_data:
#             language, _ = Language.objects.get_or_create(name=language_data['name'])
#             profile.languages.add(language)

#         # for domain_data in domains_data:
#         #     services_data = domain_data.pop('services', [])
#         #     additional_services_data = domain_data.pop('additional_services', [])
#         #     work_experiences_data = domain_data.pop('work_experiences', [])
#         #     age_ranges_data = domain_data.pop('age_ranges', [])
#         #     pet_types_data = domain_data.pop('pet_types', [])
#         #     schedule_data = domain_data.pop('schedules', [])
            
#         #     domain = Domain.objects.create(**domain_data)
            
#         #     for service_data in services_data:
#         #         service, _ = Service.objects.get_or_create(name=service_data['name'])
#         #         domain.services.add(service)
            
#         #     for additional_service_data in additional_services_data:
#         #         additional_service, _ = AdditionalService.objects.get_or_create(name=additional_service_data['name'])
#         #         domain.additional_services.add(additional_service)

#         #     for schedule_item in schedule_data:
#         #         schedule, _ = DaySchedule.objects.get_or_create(**schedule_item)
#         #         domain.schedules.add(schedule)

#         #     for work_experience_data in work_experiences_data:
#         #         work_experience, _ = WorkExperience.objects.get_or_create(**work_experience_data)
#         #         domain.work_experiences.add(work_experience)

#         #     for age_range_data in age_ranges_data:
#         #         age_range, _ = AgeRange.objects.get_or_create(range_name=age_range_data['range_name'])
#         #         domain.age_ranges.add(age_range)

#         #     for pet_type_data in pet_types_data:
#         #         pet_type, _ = PetType.objects.get_or_create(pet_name=pet_type_data['pet_name'])
#         #         domain.pet_types.add(pet_type)

#         #     profile.domains.add(domain)
            

#         return profile


class VerificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = [
            'id', 'user', 'display_name', 'user_type', 'organisation_url', 
            'organisation_name', 'reference1_name', 'reference1_phone', 
            'reference2_name', 'reference2_phone', 'identity_proof', 
            'police_certificate', 'driving_license_proof', 'status', 
            'age', 'state', 'pincode', 'gender', 'general_about', 
            'domains'
        ]

    def create(self, validated_data):
        
        profile = Profile.objects.create(**validated_data)

        # You can handle the domains data as per your requirement here
        # This is a placeholder for any custom logic you want to add

        return profile

class ProfilePatchSerializer(serializers.ModelSerializer):


    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ['user']

    def update(self, instance, validated_data):
        
        # Update the instance with the validated data
        instance = super().update(instance, validated_data)

        # Handle languages
        # Handle domains data
        # This is a placeholder for any custom logic you want to add

        return instance