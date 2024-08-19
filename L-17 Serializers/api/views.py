from api.models import Song, Singer, Student

from  api.serializers import SongSerializer, SingerSerializer, StudentSerializer

from rest_framework.viewsets import ModelViewSet
# Create your views here.

class SongAPI(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    
    
class SingerAPI(ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    
class StudentAPI(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer