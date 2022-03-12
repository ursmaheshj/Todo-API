from rest_framework import serializers
from todo.models import Todo

class TodoSerializers(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    datecompleted = serializers.ReadOnlyField()

    class Meta:
        model = Todo
        fields = ['id','title','memo','created','datecompleted','important']

class TodoCompleteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id']
        read_only_fields = ['title','memo','created','datecompleted','important']
    