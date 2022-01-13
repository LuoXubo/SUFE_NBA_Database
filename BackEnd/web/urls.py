from django.conf.urls import url
from web.views import *


urlpatterns = [
    url(r'^team/$', TeamView.as_view()),
    url(r'^team_detail/$', TeamDetailView.as_view()),
    url(r'^coach_detail/$', CoachDetailView.as_view()),
    url(r'^player_detail/$', PlayerDetailView.as_view()),
    url(r'^player_career/$', PlayerCareerView.as_view()),
    url(r'^rank/$', RankView.as_view()),
    url(r'^player_comparison/$', PlayerComparisonView.as_view()),
    url(r'^player_comparison_detail/$', PlayerComparisonDetailView.as_view())
]
