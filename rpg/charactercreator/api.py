from rest_framework import serializers, viewsets
from rpg.charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer, Walker, Runner, Berzerker

# Serializers define the API representation.
class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = ('name', 'level', 'inventory', 'exp', 'hp', 'strength', 'intelligence', 'dexterity', 'wisdom')

# ViewSets define the view behavior.
class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
