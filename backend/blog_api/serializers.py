from rest_framework import serializers
from blog.models import Post,Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name','titles']
class PostSerializer(serializers.ModelSerializer):
    #class meta su dung de cung cpa cac tham so tuy chon cho model
    category = CategorySerializer()
    class Meta:
        #model can chuyen doi du lieu
        model=Post
        #cac trg du lieu muon su dung
        fields=("id","slug","title","author","excerpt","content","status","category")