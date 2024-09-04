from rest_framework import viewsets
from .models import School, Classroom, Student, Teacher
from .serializers import SchoolSerializer, ClassroomSerializer, StudentSerializer, TeacherSerializer
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filterset_fields = ['name']


class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    filterset_fields = ['school__name']

    def get_queryset(self):
        queryset = Classroom.objects.all()
        school_id = self.request.query_params.get('school', None)
        if school_id is not None:
            queryset = queryset.filter(school__id=school_id)
        return queryset


class TeacherFilter(filters.FilterSet):
    school = filters.CharFilter(field_name='classrooms__school__name')
    classroom = filters.NumberFilter(field_name='classrooms__id')
    firstname = filters.CharFilter(field_name='first_name', lookup_expr='icontains')
    lastname = filters.CharFilter(field_name='last_name', lookup_expr='icontains')
    gender = filters.CharFilter(field_name='gender', lookup_expr='iexact')

    class Meta:
        model = Teacher
        fields = ['school', 'classroom', 'firstname', 'lastname', 'gender']


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filterset_class = TeacherFilter
    search_fields = ['first_name', 'last_name', 'gender', 'classrooms__school__name', 'classrooms__grade']
    ordering_fields = ['first_name', 'last_name']

    def get_queryset(self):
        queryset = Teacher.objects.all()
        school = self.request.query_params.get('school', None)
        classroom = self.request.query_params.get('classroom', None)
        firstname = self.request.query_params.get('firstname', None)
        lastname = self.request.query_params.get('lastname', None)
        gender = self.request.query_params.get('gender', None)

        if school:
            queryset = queryset.filter(classrooms__school__name=school)
        if classroom:
            queryset = queryset.filter(classrooms__id=classroom)
        if firstname:
            queryset = queryset.filter(first_name__icontains=firstname)
        if lastname:
            queryset = queryset.filter(last_name__icontains=lastname)
        if gender:
            queryset = queryset.filter(gender__iexact=gender)
        return queryset


class StudentFilter(filters.FilterSet):
    school = filters.CharFilter(field_name='classroom__school__name')
    classroom = filters.NumberFilter(field_name='classroom__id')
    firstname = filters.CharFilter(field_name='first_name', lookup_expr='icontains')
    lastname = filters.CharFilter(field_name='last_name', lookup_expr='icontains')
    gender = filters.CharFilter(field_name='gender', lookup_expr='iexact')

    class Meta:
        model = Student
        fields = ['school', 'classroom', 'firstname', 'lastname', 'gender']

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StudentFilter
    search_fields = ['first_name', 'last_name', 'gender', 'classroom__school__name', 'classroom__grade']
    ordering_fields = ['first_name', 'last_name']

    def get_queryset(self):
        queryset = Student.objects.all()
        school = self.request.query_params.get('school', None)
        classroom = self.request.query_params.get('classroom', None)
        firstname = self.request.query_params.get('firstname', None)
        lastname = self.request.query_params.get('lastname', None)
        gender = self.request.query_params.get('gender', None)

        if school:
            queryset = queryset.filter(classroom__school__name=school)
        if classroom:
            queryset = queryset.filter(classroom__id=classroom)
        if firstname:
            queryset = queryset.filter(first_name__icontains=firstname)
        if lastname:
            queryset = queryset.filter(last_name__icontains=lastname)
        if gender:
            queryset = queryset.filter(gender__iexact=gender)
        return queryset