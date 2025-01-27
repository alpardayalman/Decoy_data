from rest_framework.views import APIView
from rest_framework.response import Response
from .models import SampleData
from .serializers import SampleDataSerializer

class SampleDataView(APIView):
    def get(self, request):
        data = SampleData.objects.all()
        serializer = SampleDataSerializer(data, many=True)
        return Response(serializer.data)