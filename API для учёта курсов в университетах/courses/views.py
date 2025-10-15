from rest_framework.viewsets import ModelViewSet
from .serializers import UniversitySerializer, CourseSerializer, UniversityCourseSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import University, Course, UniversityCourse
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg


class UniversityViewSet(ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    http_method_names = ["get", "delete", "post", "patch"]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = [
        "name",
        "university_courses__course__title"
    ]
    filtered_fields = {
        'university_courses__course__title': ['icontains'],
        'university_courses__semester': ['exact', 'icontains'],
    }
    ordering_fields = ["university_courses__duration_weeks"]


    @action(detail=True, methods=["get"],url_path="course_stats")
    def course_stats(self, request, pk=None):
        university = self.get_object()
        courses = university.university_courses.all()

        total_courses = courses.count()
        if total_courses > 0:
            avg_duration = courses.aggregate(avg_duration=Avg('duration_weeks'))
        else:
            avg_duration = 0

        return Response({
            'total_courses': total_courses,
            'average_duration_weeks': avg_duration,
        })

    @action(detail=True, methods=['get'])
    def courses(self, request, pk=None):
        university = self.get_object()
        courses_qs = university.university_courses.all()

        serializer = UniversityCourseSerializer(courses_qs, many=True)
        return Response(serializer.data)


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    http_method_names = ["get", "delete", "post", "patch"]
    filter_backends = [SearchFilter]
    search_fields = ['title']


class UniversityCourseViewSet(ModelViewSet):
    queryset = UniversityCourse.objects.all()
    serializer_class = UniversityCourseSerializer
    http_method_names = ["get", "delete", "post", "patch"]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['semester', 'course__title']
    ordering_fields = ['duration_weeks']
