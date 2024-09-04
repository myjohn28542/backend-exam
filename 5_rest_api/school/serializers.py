from rest_framework import serializers
from .models import School, Classroom, Teacher, Student

class SchoolSerializer(serializers.ModelSerializer):
    classroom_count = serializers.SerializerMethodField()
    teacher_count = serializers.SerializerMethodField()
    student_count = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = ['id', 'name', 'abbreviation', 'address', 'classroom_count', 'teacher_count', 'student_count']

    def get_classroom_count(self, obj):
        return obj.classrooms.count()

    def get_teacher_count(self, obj):
        # Count unique teachers across all classrooms in the school
        return Teacher.objects.filter(classrooms__school=obj).distinct().count()

    def get_student_count(self, obj):
        # Count students in all classrooms in the school
        return Student.objects.filter(classroom__school=obj).count()



class ClassroomSerializer(serializers.ModelSerializer):
    school = serializers.CharField(source='school.name')
    teachers = serializers.StringRelatedField(many=True, read_only=True)
    students = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Classroom
        fields = ['id', 'grade', 'section', 'school', 'teachers', 'students']


class TeacherSerializer(serializers.ModelSerializer):
    classroom_id = serializers.PrimaryKeyRelatedField(queryset=Classroom.objects.all(), source='classroom')
    classroom_list = ClassroomSerializer(source='classrooms', many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'gender', 'classroom_list', 'classroom_id']


class StudentSerializer(serializers.ModelSerializer):
    classroom_id = serializers.PrimaryKeyRelatedField(queryset=Classroom.objects.all(), source='classroom')
    classroom = ClassroomSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'gender', 'classroom', 'classroom_id']