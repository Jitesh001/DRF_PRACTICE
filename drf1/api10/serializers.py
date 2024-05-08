from rest_framework import serializers
from .models import Singer, Song 

# #serializer relation example
# class SongSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Song
#         fields = '__all__'

# class SingerSerializer(serializers.ModelSerializer):
#     song = serializers.StringRelatedField(many=True, read_only=True) 
#     #list of songs related to singer, with string related field as a list (here song names list)
#     class Meta:
#         model = Singer
#         fields = '__all__'
#         # fields = ['id', 'name', 'age', 'song'] 
#         #'song' is related filed name used in Song model, it shows list of song with 'IDs' related to singer in API response


#nested serializer relation example
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

class SingerSerializer(serializers.ModelSerializer):
    song = SongSerializer(many=True, read_only=True)
    class Meta:
        model = Singer
        fields = '__all__'
    #gives response will full song details list for each singer