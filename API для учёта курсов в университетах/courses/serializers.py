from rest_framework import serializers
from .models import University, Course, UniversityCourse


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        read_only_fields = ["id"]
        fields = [
            "id",
            "name",
            "country"
        ]


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        read_only_fields = ["id"]
        fields = [
            "id",
            "title",
            "description"
        ]


class UniversityCourseSerializer(serializers.ModelSerializer):
    university = UniversitySerializer(read_only=True)
    course = CourseSerializer(read_only=True)
    university_id = serializers.PrimaryKeyRelatedField(
        source='university', queryset=University.objects.all(), write_only=True
    )

    course_id = serializers.PrimaryKeyRelatedField(
        source='course', queryset=Course.objects.all(), write_only=True
    )

    class Meta:
        model = UniversityCourse
        fields = [
            "id",
            "university",
            "course",
            "university_id",
            "course_id",
            'semester',
            'duration_weeks'
        ]
