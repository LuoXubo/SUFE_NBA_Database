from rest_framework import serializers
from web import models
from rest_framework.exceptions import ValidationError
import re


class TeamShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Team
        fields = ['id', 'name_c', 'name_e', 'photo']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Team
        fields = '__all__'


class CoachCareerSerializer(serializers.ModelSerializer):
    team = serializers.CharField(source='team.name_e')

    class Meta:
        model = models.CoachCareer
        fields = '__all__'


class CoachShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Coach
        fields = ['id', 'name', 'photo']


class PlayerDetailToPlayerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='player.id')
    name = serializers.CharField(source='player.name_e')
    photo = serializers.CharField(source='player.photo')
    uniform_number = serializers.IntegerField(source='player.uniform_number')

    class Meta:
        model = models.PlayerDetail
        fields = ['id', 'name', 'photo', 'uniform_number']


class TeamDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TeamData
        fields = '__all__'


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Coach
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Player
        fields = '__all__'


class PlayerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PlayerDetail
        fields = '__all__'


class PlayerHotShotSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ShootingHotsPot
        fields = '__all__'


class PlayerRankSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='player.id')
    name = serializers.CharField(source='player.name_e')
    photo = serializers.CharField(source='player.photo')
    uniform_number = serializers.IntegerField(source='player.uniform_number')

    class Meta:
        model = models.PlayerDetail
        fields = [
            'id', 'photo', 'uniform_number',
            'name', 'score',
            'time', 'total_rebounds',
            'hit_percentage', 'three_point_hit_percentage',
            'penalty_hit_percentage', 'assists',
            'snatch', 'blocks', 'foul'
        ]


class PlayerComparisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Player
        fields = ['id', 'photo', 'name_e', 'uniform_number']
