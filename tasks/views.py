from rest_framework import serializers
from rest_framework.views import APIView
from tasks.models import Task
from tasks.serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status

class TaskAPIView(APIView):

    def get(self, request):
        tasks = Task.objects.all()

        serializer = TaskSerializer(tasks, many = True)

        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            body = serializer.validated_data.get('body')
            estimated_finish_time  = serializer.validated_data.get('estimated_finish_time')
            task = Task.objects.create(body=body, estimated_finish_time=estimated_finish_time)
            serializer = TaskSerializer(instance=task)
            return Response(serializer.data)

        return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)