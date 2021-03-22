from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    rollno = serializers.IntegerField()
    name   = serializers.CharField(max_length=264)
    clas   = serializers.CharField(max_length=264)
    