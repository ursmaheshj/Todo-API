from rest_framework import generics,permissions
from todo.models import Todo
from .serializers import TodoSerializers

# Create your views here.
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
    
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)