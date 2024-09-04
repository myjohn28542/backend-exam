from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SchoolViewSet, ClassroomViewSet, TeacherViewSet, StudentViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'school', SchoolViewSet, basename='school')
router.register(r'classroom', ClassroomViewSet, basename='classroom')
router.register(r'teacher', TeacherViewSet, basename='teacher')
router.register(r'student', StudentViewSet, basename='student')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
