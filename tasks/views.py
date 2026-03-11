from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Task, Category
from .models import Task
from .serializers import TaskSerializer
from .models import Category
from .serializers import CategorySerializer
from rest_framework.generics import RetrieveUpdateAPIView
from .models import Profile
from .serializers import ProfileSerializer

class TaskListCreateView(ListCreateAPIView):

    # كل المهام
    queryset = Task.objects.all()

    # serializer المستخدم
    serializer_class = TaskSerializer

    # لازم المستخدم يكون عامل login
    permission_classes = [IsAuthenticated]

    # filtering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # search
    search_fields = ['title', 'description']

    # filtering fields
    filterset_fields = ['completed']

    # sorting
    ordering_fields = ['created_at']
    
    # API لتعديل أو حذف مهمة
@api_view(['PUT', 'DELETE'])
def task_detail(request, id):

    # البحث عن المهمة بواسطة id
    task = get_object_or_404(Task, id=id)

    # تعديل المهمة
    if request.method == 'PUT':

        # إرسال البيانات الجديدة لل serializer
        serializer = TaskSerializer(task, data=request.data)

        # التحقق من صحة البيانات
        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # حذف المهمة
    elif request.method == 'DELETE':

        task.delete()

        return Response({"message": "Task deleted successfully"})
    
    # API لإنشاء حساب جديد
# API لإنشاء حساب جديد
@api_view(['POST'])
@permission_classes([AllowAny])  # السماح لأي شخص يعمل register
def register_user(request):

    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryListCreateView(ListCreateAPIView):

    queryset = Category.objects.all()

    serializer_class = CategorySerializer

    permission_classes = [IsAuthenticated]

class ProfileView(RetrieveUpdateAPIView):

    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Profile.objects.get(user=self.request.user)