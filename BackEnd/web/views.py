from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from web import models
from rest_framework.throttling import AnonRateThrottle
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from django.db.models import F
from web import serializer
from web.utils import predict


# 球队首页接口逻辑
class TeamView(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = [AnonRateThrottle, ]

    def get(self, request, *args, **kwargs):
        result = {'data': None, 'status': None, 'errors': None}
        queryset = models.Team.objects.all()
        ser = serializer.TeamShowSerializer(instance=queryset, many=True)
        result['data'] = ser.data
        result['status'] = status.HTTP_200_OK
        return Response(result)


# 球队详情接口逻辑
class TeamDetailView(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = [AnonRateThrottle, ]

    def get(self, request, *args, **kwargs):
        result = {'data': None, 'status': None, 'errors': None}
        team_id = request.query_params.get('id')
        if team_id is None:
            result['status'] = status.HTTP_400_BAD_REQUEST
            result['errors'] = "未传递参数id或参数传递错误"
            return Response(result)
        team_obj = models.Team.objects.filter(id=team_id).first()
        if not team_obj:
            result['status'] = status.HTTP_400_BAD_REQUEST
            result['errors'] = "没有该球队信息"
            return Response(result)
        ser_team = serializer.TeamSerializer(instance=team_obj)
        coach_career_obj = models.CoachCareer.objects.filter(team=team_id, season='19-20').first()
        ser_coach_career = serializer.CoachCareerSerializer(instance=coach_career_obj)
        coach_obj = models.Coach.objects.filter(id=ser_coach_career.data.get('coach')).first()
        ser_coach = serializer.CoachShowSerializer(instance=coach_obj)
        player_queryset = models.PlayerDetail.objects.filter(team=team_id, season='21-22', match_type='常规赛')
        ser_player = serializer.PlayerDetailToPlayerSerializer(instance=player_queryset, many=True)
        team_queryset = models.TeamData.objects.filter(team=team_id)
        ser_team_data = serializer.TeamDataSerializer(instance=team_queryset, many=True)
        data = {
            'coach': ser_coach.data,
            'player': ser_player.data,
            'teamdata': ser_team_data.data,
            **ser_team.data
        }
        result['data'] = data
        result['status'] = status.HTTP_200_OK
        return Response(result)


# 教练详情接口逻辑
class CoachDetailView(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = [AnonRateThrottle, ]

    def get(self, request, *args, **kwargs):
        result = {'data': None, 'status': None, 'errors': None}
        coach_id = request.query_params.get('id')
        if coach_id is None:
            result['status'] = status.HTTP_400_BAD_REQUEST
            result['errors'] = "未传递参数id或参数传递错误"
            return Response(result)
        coach_obj = models.Coach.objects.filter(id=coach_id).first()
        if not coach_obj:
            result['status'] = status.HTTP_400_BAD_REQUEST
            result['errors'] = "没有教练信息"
            return Response(result)
        ser_coach = serializer.CoachSerializer(instance=coach_obj)
        coach_career_queryset = models.CoachCareer.objects.filter(coach=coach_id)
        ser_coach_career = serializer.CoachCareerSerializer(instance=coach_career_queryset, many=True)
        data = {
            'career': ser_coach_career.data,
            **ser_coach.data
        }
        result['data'] = data
        result['status'] = status.HTTP_200_OK
        return Response(result)


# 球员详情接口逻辑
class PlayerDetailView(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = [AnonRateThrottle, ]

    def get(self, request, *args, **kwargs):
        result = {'data': None, 'status': None, 'errors': None}
        player_id = request.query_params.get('id')
        if player_id is None:
            result['status'] = status.HTTP_400_BAD_REQUEST
            result['errors'] = "参数id未传递或参数传递错误"
            return Response(result)
        player_obj = models.Player.objects.filter(id=player_id).first()
        if not player_obj:
            result['status'] = status.HTTP_400_BAD_REQUEST
            result['errors'] = "没有该运动员信息"
            return Response(result)
        ser_player = serializer.PlayerSerializer(instance=player_obj)
        player_detail_obj = models.PlayerDetail.objects.filter(player=player_obj, season='21-22', match_type='常规赛').first()
        ser_player_detail = serializer.PlayerDetailSerializer(instance=player_detail_obj)
        hot_shot = models.ShootingHotsPot.objects.filter(player=player_obj, season='21-22').first()
        ser_hot_shot = serializer.PlayerHotShotSerializer(instance=hot_shot)
        data = {
            'detail': ser_player_detail.data,
            'shooting_hots_pot': ser_hot_shot.data,
            **ser_player.data
        }
        result['data'] = data
        result['status'] = status.HTTP_200_OK
        return Response(result)


# 球员生涯接口逻辑
class PlayerCareerView(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = [AnonRateThrottle, ]

    def get(self, request, *args, **kwargs):
        result = {'data': None, 'status': None, 'errors': None}
        player_id = request.query_params.get('id')
        if player_id is None:
            result['status'] = status.HTTP_400_BAD_REQUEST
            result['errors'] = "未传递参数id或者参数传递错误"
            return Response(result)
        player_obj = models.Player.objects.filter(id=player_id).first()
        if not player_obj:
            result['status'] = status.HTTP_400_BAD_REQUEST
            result['errors'] = "没有该球员信息"
            return Response(result)
        ser_player = serializer.PlayerComparisonSerializer(instance=player_obj)
        player_detail_queryset = models.PlayerDetail.objects.filter(player=player_obj)
        ser_player_detail = serializer.PlayerDetailSerializer(instance=player_detail_queryset, many=True)
        pre = predict.predictAll(ser_player_detail.data)
        data = {
            'detail': ser_player_detail.data,
            'predict': pre,
            **ser_player.data
        }
        result['data'] = data
        result['status'] = status.HTTP_200_OK
        return Response(result)


# 排行榜接口逻辑
class RankView(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = [AnonRateThrottle, ]

    def get(self, request, *args, **kwargs):
        result = {'data': None, 'status': None, 'errors': None}
        typ = request.query_params.get('type')
        if not typ:
            result['status'] = status.HTTP_400_BAD_REQUEST
            result['errors'] = "未传递参数type或参数传递错误"
            return Response(result)
        queryset = None
        if typ == 'score':
            queryset = models.PlayerDetail.objects.all().order_by('-score')
        elif typ == 'time':
            queryset = models.PlayerDetail.objects.all().order_by('-time')
        elif typ == 'total_rebounds':
            queryset = models.PlayerDetail.objects.all().order_by('-total_rebounds')
        elif typ == 'hit_percentage':
            queryset = models.PlayerDetail.objects.all().order_by('-hit_percentage')
        elif typ == 'three_point_hit_percentage':
            queryset = models.PlayerDetail.objects.all().order_by('-three_point_hit_percentage')
        elif typ == 'penalty_hit_percentage':
            queryset = models.PlayerDetail.objects.all().order_by('-penalty_hit_percentage')
        elif typ == 'assists':
            queryset = models.PlayerDetail.objects.all().order_by('-assists')
        elif typ == 'snatch':
            queryset = models.PlayerDetail.objects.all().order_by('-snatch')
        elif typ == 'blocks':
            queryset = models.PlayerDetail.objects.all().order_by('-blocks')
        elif typ == 'foul':
            queryset = models.PlayerDetail.objects.all().order_by('-foul')
        ser = serializer.PlayerRankSerializer(instance=queryset, many=True)
        data = ser.data[:10]
        result['data'] = data
        result['status'] = status.HTTP_200_OK
        return Response(result)


# 球员比较首页接口
class PlayerComparisonView(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = [AnonRateThrottle, ]

    def get(self, request, *args, **kwargs):
        result = {'data': None, 'status': None, 'errors': None}
        queryset = models.Player.objects.all()
        if not queryset:
            result['status'] = status.HTTP_400_BAD_REQUEST
            result['errors'] = "没有任何球员"
            return Response(result)
        ser = serializer.PlayerComparisonSerializer(instance=queryset, many=True)
        result['data'] = ser.data[:20]
        result['status'] = status.HTTP_200_OK
        return Response(result)


# 球员比较详情接口
class PlayerComparisonDetailView(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = [AnonRateThrottle, ]

    def get(self, request, *args, **kwargs):
        result = {'data': None, 'status': None, 'errors': None}
        player_id = request.query_params.get('id')
        if player_id is None:
            result['status'] = status.HTTP_400_BAD_REQUEST
            result['errors'] = "未传递参数id或参数传递错误"
            return Response(result)
        player_obj = models.PlayerDetail.objects.filter(player=player_id, season='21-22', match_type='常规赛').first()
        if not player_obj:
            result['status'] = status.HTTP_400_BAD_REQUEST
            result['errors'] = "没有该球员信息"
            return Response(result)
        ser = serializer.PlayerRankSerializer(instance=player_obj)
        result['data'] = ser.data
        result['status'] = status.HTTP_200_OK
        return Response(result)

