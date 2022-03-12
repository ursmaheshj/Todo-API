from telnetlib import STATUS
from rest_framework import generics,permissions
from rest_framework.parsers import JSONParser
from todo.models import Todo
from .serializers import TodoCompleteSerializers, TodoSerializers
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token 
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate

# Create your views here.
@api_view(['POST'])
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = request.data
            user = User.objects.create_user(data['username'], password=data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)},status=201)
        except IntegrityError:
            return JsonResponse({'error':'That username has already been taken. Please choose a new username'},status=400)

@api_view(['POST'])
@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = request.data
        user = authenticate(request,username=data['username'], password=data['password'])
        if user is None:
            return JsonResponse({'error':'Username or Password wrong'},status=401)
        else:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)},status=200)
    

class TodoCompletedList(generics.ListAPIView):
    serializer_class = TodoSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        return Todo.objects.filter(user=user,datecompleted__isnull=False).order_by('-datecompleted')
    
class TodoListCreate(generics.ListCreateAPIView):
    serializer_class = TodoSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        return Todo.objects.filter(user=user,datecompleted__isnull=True)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        return Todo.objects.filter(user=user)
    
class TodoUpdate(generics.UpdateAPIView):
    serializer_class = TodoCompleteSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        return Todo.objects.filter(user=user)

    def perform_update(self, serializer):
        serializer.instance.datecompleted=timezone.now()
        serializer.save()

