from django.db import models


class Player(models.Model):
    name_c = models.CharField(verbose_name='中文姓名', max_length=255)
    name_e = models.CharField(verbose_name='英文姓名', max_length=255)
    photo = models.CharField(verbose_name='球员照片', max_length=255)
    position = models.CharField(verbose_name='场上位置', max_length=255)
    height = models.FloatField(verbose_name='身高')
    weight = models.FloatField(verbose_name='体重')
    age = models.IntegerField(verbose_name='年龄')
    experience = models.CharField(verbose_name='经验', max_length=255)
    uniform_number = models.IntegerField(verbose_name='号码')
    objects = models.Manager()


class PlayerDetail(models.Model):
    player = models.ForeignKey(verbose_name='所属球员', to='Player', on_delete=models.CASCADE)
    match_type = models.CharField(verbose_name='比赛类型', max_length=255, default='regular')
    season = models.CharField(verbose_name='赛季', max_length=255)
    team = models.ForeignKey(verbose_name='球队', to='Team', on_delete=models.CASCADE)
    time = models.FloatField(verbose_name='出场时间')
    hit_percentage = models.FloatField(verbose_name='投篮命中率', default=0.0)
    shot_number = models.FloatField(verbose_name='投篮出手数', default=0.0)
    three_point_hit_percentage = models.FloatField(verbose_name='三分命中率', default=0.0)
    three_point_shot_number = models.FloatField(verbose_name='三分出手数', default=0.0)
    penalty_hit_percentage = models.FloatField(verbose_name='罚球命中率', default=0.0)
    penalty_shot_number = models.FloatField(verbose_name='罚球出手数', default=0.0)
    total_rebounds = models.FloatField(verbose_name='总篮板数', default=0.0)
    assists = models.FloatField(verbose_name='助攻数', default=0.0)
    snatch = models.FloatField(verbose_name='抢断数', default=0.0)
    blocks = models.FloatField(verbose_name='盖帽数', default=0.0)
    foul = models.FloatField(verbose_name='犯规数', default=0.0)
    score = models.FloatField(verbose_name='得分', default=0.0)
    win = models.IntegerField(verbose_name='胜利场数')
    loss = models.IntegerField(verbose_name='失败场数')
    objects = models.Manager()


class ShootingHotsPot(models.Model):
    player = models.ForeignKey(verbose_name='所属球员', to='Player', on_delete=models.CASCADE)
    season = models.CharField(verbose_name='赛季', max_length=255)
    penalty_hit_percentage = models.FloatField(verbose_name='罚球命中率')
    p1 = models.FloatField(verbose_name='p1')
    p2 = models.FloatField(verbose_name='p2')
    p3 = models.FloatField(verbose_name='p3')
    p4 = models.FloatField(verbose_name='p4')
    p5 = models.FloatField(verbose_name='p5')
    objects = models.Manager()


class Team(models.Model):
    name_c = models.CharField(verbose_name='中文球队名称', max_length=255)
    name_e = models.CharField(verbose_name='英文球队名称', max_length=255)
    slogan = models.CharField(verbose_name='球队口号', max_length=255)
    photo = models.CharField(verbose_name='球队照片', max_length=255)
    area = models.CharField(verbose_name='分区', max_length=255)
    stadium = models.CharField(verbose_name='球馆', max_length=255)
    objects = models.Manager()


class Coach(models.Model):
    name = models.CharField(verbose_name='教练姓名', max_length=255)
    photo = models.CharField(verbose_name='教练照片', max_length=255)
    date_of_birth = models.CharField(verbose_name='出生日期', max_length=255)
    city_of_birth = models.CharField(verbose_name='出生城市', max_length=255)
    senior_high_school = models.CharField(verbose_name='高中', max_length=255)
    university = models.CharField(verbose_name='大学', max_length=255)
    career_number = models.IntegerField(verbose_name='执教生涯年数')
    career_team_number = models.IntegerField(verbose_name='执教生涯球队数')
    career_teaching_number = models.IntegerField(verbose_name='执教生涯场数')
    career_win = models.IntegerField(verbose_name='执教生涯胜场')
    career_loss = models.IntegerField(verbose_name='执教生涯败场')
    career_win_rate = models.FloatField(verbose_name='执教生涯胜率')
    objects = models.Manager()


class CoachCareer(models.Model):
    coach = models.ForeignKey(verbose_name='所属教练', to='Coach', on_delete=models.CASCADE)
    team = models.ForeignKey(verbose_name='所属球队', to='Team', on_delete=models.CASCADE)
    season = models.CharField(verbose_name='赛季', max_length=255)
    teaching_number = models.IntegerField(verbose_name='执教数')
    win = models.IntegerField(verbose_name='胜场')
    loss = models.IntegerField(verbose_name='败场')
    win_rate = models.FloatField(verbose_name='胜率')
    objects = models.Manager()


class TeamData(models.Model):
    team = models.ForeignKey(verbose_name='所属球队', to='Team', on_delete=models.CASCADE)
    season = models.CharField(verbose_name='赛季', max_length=255)
    match_type = models.CharField(verbose_name='比赛类型', max_length=255)
    hit_percentage = models.FloatField(verbose_name='投篮命中率', default=0.0)
    three_point_hit_percentage = models.FloatField(verbose_name='三分命中率', default=0.0)
    penalty_hit_percentage = models.FloatField(verbose_name='罚球命中率', default=0.0)
    total_rebounds = models.FloatField(verbose_name='总篮板数', default=0.0)
    assists = models.FloatField(verbose_name='助攻数', default=0.0)
    snatch = models.FloatField(verbose_name='抢断数', default=0.0)
    blocks = models.FloatField(verbose_name='盖帽数', default=0.0)
    miss = models.FloatField(verbose_name='失误数', default=0.0)
    foul = models.FloatField(verbose_name='犯规数', default=0.0)
    score = models.FloatField(verbose_name='得分', default=0.0)
    objects = models.Manager()
