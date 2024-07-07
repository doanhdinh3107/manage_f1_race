from rest_framework import serializers
from rank.models import GrandAustralia,GrandJapan,GrandBahrain,Team,Racer
class GrandAustraliaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrandAustralia
        fields = ['team','point']
class GrandJapanSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrandJapan
        fields = ['team','point']
class GrandBahrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrandBahrain
        fields = ['team','point']               
class TeamSerializer(serializers.ModelSerializer):
    #class meta su dung de cung cpa cac tham so tuy chon cho model
    grandaustralia=GrandAustraliaSerializer()
    grandjapan=GrandJapanSerializer()
    grandbahrain=GrandBahrainSerializer()
    class Meta:
        #model can chuyen doi du lieu
        model=Team
        #cac trg du lieu muon su dung
        fields=("id","name","point",'grandjapan','grandaustralia','grandbahrain','logo',"image","description")
class RacerSerializer(serializers.ModelSerializer):
    #class meta su dung de cung cpa cac tham so tuy chon cho model
    team=TeamSerializer()
    class Meta:
        #model can chuyen doi du lieu
        model=Racer
        #cac trg du lieu muon su dung
        fields=("id","avatar","name","birth","team","bio",'point')