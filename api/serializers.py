from rest_framework import serializers
from todo.models import Todo

class TodoSerializers(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    datecompleted = serializers.ReadOnlyField()
    
    class Meta:
        model = Todo
        fields = ['id','title','memo','created','datecompleted','important']
    