<template>
	<view class="container">
		<!-- 球队及教练信息 -->
		<view class="header">
			<view class="bg_header">
			    <view class="t_title">
			        Team Details
			    </view> 
			</view>
		</view>
		<view class="data_content">
			<view class="data_main">
				<view class="main_left fl">
					<view class="left_1 t_btn6">
						<!--左上边框-->
						<view class="t_line_box">
							<i class="t_l_line"></i> 
							<i class="l_t_line"></i> 
						</view> 
						<!--右上边框-->
						<view class="t_line_box">
							<i class="t_r_line"></i> 
							<i class="r_t_line"></i> 
						</view> 
						<!--左下边框-->
						<view class="t_line_box">
							<i class="l_b_line"></i> 
							<i class="b_l_line"></i> 
						</view> 
							<!--右下边框-->
						<view class="t_line_box">
							<i class="r_b_line"></i> 
							<i class="b_r_line"></i> 
						</view> 
						<view class="main_title">
							<img src="../../static/ct_1.png" alt="">
							Team Information
						</view>
						<view style="color: white; margin-top: 100upx; margin-left: 50upx; align-items: center;">
							<view style="font-size: 60upx; margin-top: 30upx;">{{team_name}}</view>
							<view style="font-size: 30upx; margin-top: 30upx;">{{team_name_cn}}</view>
							<view style="margin-top: 30upx; font-size: 30upx;">Address: {{team_city}}</view>
							<view style="margin-top: 30upx; font-size: 30upx;">Motto: {{team_info}}</view>
						</view>
					</view>
					<view class="left_2">
						<view class="t_line_box">
							<i class="t_l_line"></i> 
							<i class="l_t_line"></i> 
						</view> 
						<view class="t_line_box">
							<i class="t_r_line"></i> 
							<i class="r_t_line"></i> 
						</view> 
						<view class="t_line_box">
							<i class="l_b_line"></i> 
							<i class="b_l_line"></i> 
						</view> 
							<view class="t_line_box">
							<i class="r_b_line"></i> 
							<i class="b_r_line"></i> 
						</view>
						<view class="main_title">
							<img src="../../static/ct_1.png" alt="">
							Coach Information
						</view>
						<view class="coach_info">
							<view style="font-size: 50upx; color: white; margin-top: 100upx; margin-left: 300upx;">{{coach.name}}</view>
							<image class="coach_img" :src="coach.photo" @tap="to_coach_detail(coach.id)"></image>
						</view>
					</view>
				</view>
				<view class="main_center fl">
					<view class="center_text" style="position: relative;">
						<!--左上边框-->
						<view class="t_line_box">
							<i class="t_l_line"></i> 
							<i class="l_t_line"></i> 
						</view> 
						<!--右上边框-->
						<view class="t_line_box">
							<i class="t_r_line"></i> 
							<i class="r_t_line"></i> 
						</view> 
						<!--左下边框-->
						<view class="t_line_box">
							<i class="l_b_line"></i> 
							<i class="b_l_line"></i> 
						</view> 
						 <!--右下边框-->
						 <view class="t_line_box">
							<i class="r_b_line"></i> 
							<i class="b_r_line"></i> 
						</view> 
						<view class="main_title" style="width: 230px;">
							<img src="../../static/ct_2.png" alt="">
							Team Stat
						</view>
						<view style="color: white; font-size: 40upx; margin-top: 70upx; margin-left: 30%;">
							<picker @change="StatType" :range="StatTypeArray">
								<label>Stat type : </label>
								<label>{{StatTypeArrayType}}</label>
							</picker>
						</view>
						<canvas canvas-id="canvasLine" id="canvasLine" style="margin-left: 17%; height: 1000upx; width: 1000upx;"></canvas>
					</view>
				</view>
				<view class="main_right fr">
					<view class="right_1" style="height: 1220upx;">
						<!--左上边框-->
						<view class="t_line_box">
							<i class="t_l_line"></i> 
							<i class="l_t_line"></i> 
						</view> 
						<!--右上边框-->
						<view class="t_line_box">
							<i class="t_r_line"></i> 
							<i class="r_t_line"></i> 
						</view> 
						<!--左下边框-->
						<view class="t_line_box">
							<i class="l_b_line"></i> 
							<i class="b_l_line"></i> 
						</view> 
							<!--右下边框-->
							<view class="t_line_box">
							<i class="r_b_line"></i> 
							<i class="b_r_line"></i> 
						</view> 
						<view class="main_title" style="width:220px;">
							<img src="../../static/ct_4.png" alt="">
							Players
						</view>
						<view v-for="(item,index) in player" style="margin-left: 100upx; margin-top: 50upx;">
							<view style="display: flex; flex-direction: row; color: white;">
								<image :src="item.photo" class="player_img" @tap="to_player_detail(item.id)"></image>
								<view style="font-size: 50upx; margin-left: 40upx; margin-top: 50upx;">{{item.name}}</view>
								<view style="font-size: 40upx; margin-left: 40upx; margin-top: 50upx;">{{item.uniform_number}}</view>
							</view>
						</view>
					</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	import uCharts from '../../components/u-charts/u-charts.js';
	var	_self;
	var Line = null;
	export default{
		data() {
			return {
				StatTypeArray:['---Please select---', 'Win', 'Score', 'Rebounds', 'Assists', 'Hit Rate'],
				StatTypeIndex:0,
				StatTypeArrayType:'---Please select---',
				
				team_name : 'Golden State Warriors',
				team_name_cn : '金州勇士队',
				team_img: 'https://china.nba.com/media/img/teams/logos/GSW_logo.svg',
				team_city : 'San Francisco',
				team_info: 'The whole team is a city',
				coach : {
					id : 1,
					name : 'Steve Kerr',
					photo : 'https://www.basketball-reference.com/req/202106291/images/coaches/kerrst01c.png'
				},
				player: [
					{
						photo: 'https://cdn.nba.com/headshots/nba/latest/1040x760/201939.png',
						uniform_number : 30,
						name : 'Stephen Curry',
						id : 1
					},
					{
						photo: 'https://cdn.nba.com/headshots/nba/latest/1040x760/203110.png',
						uniform_number : 23,
						name : 'Draymond Green',
						id : 2,
					},
					{
						photo: 'https://cdn.nba.com/headshots/nba/latest/1040x760/202691.png',
						uniform_number : 11,
						name : 'Klay Thompson',
						id : 3,
					}
				],
				team_data : [
					{
						season : '20-21',
						match_number : 72,
						win : 40,
						lose : 32,
						hit_percentage : 50,
						three_point_hit_percentage : 30,
						penalty_hit_percentage : 70,
						total_rebounds : 40,
						assists : 30,
						snatch : 10,
						blocks : 10,
						miss : 14,
						foul : 18,
						score : 100,
					},
					{
						season : '19-20',
						match_number : 72,
						win : 40,
						lose : 32,
						hit_percentage : 50,
						three_point_hit_percentage : 30,
						penalty_hit_percentage : 70,
						total_rebounds : 40,
						assists : 30,
						snatch : 10,
						blocks : 10,
						miss : 14,
						foul : 18,
						score : 100,
					},
					{
						season : '18-19',
						match_number : 72,
						win : 40,
						lose : 32,
						hit_percentage : 50,
						three_point_hit_percentage : 30,
						penalty_hit_percentage : 70,
						total_rebounds : 40,
						assists : 30,
						snatch : 10,
						blocks : 10,
						miss : 14,
						foul : 18,
						score : 100,
					},
				]
			};
		},
		onLoad(team_id) {
			_self = this;
			console.log(team_id);
			/* uni.request({
				url: '/api/team_detail',
				method: 'GET',
				data: {},
				success: res => {
				var data = res.data;
				this.team_img = data.photo;
				this.team_name = data.name_e;
				this.team_name_cn = data.name_c;
				this.team_info = data.slogan;
				this.team_city = data.area;
				this.stadium = data.stadium;
				this.coach_img = data.coach.photo;
				this.coach_name = data.coach.name;
				this.player = data.player;
				this.team_data = data.teamdata;
				},
			fail: (err) => {console.log(err)},
			complete: () => {}
			});
			this.getServerData(); */
		},
		methods:{
			to_coach_detail(id){
				uni.navigateTo({
					url:'../coach_detail/coach_detail?id=' + id,
					fail(e){
						console.log(e)
					}
				})
			},
			to_player_detail(id){
				// console.log(id)
				uni.navigateTo({
					url : '../player_detail/player_detail?id=' + id,
					fail(e){
						console.log(e)
					}
				})
			},
			getServerData(){
				var StatType = this.StatTypeIndex;
				let Line = {categories:[], series:[]};
				var categories = [];
				var series = [];
				var win = [];
				var score = [];
				var rebounds = [];
				var assists = [];
				var two_rate = [];
				var three_rate = [];
				var one_rate = [];
				var teamdata = this.team_data;
				for(var i=0;i<teamdata.length;i++){
					categories.push(teamdata[i].season);
					win.push(teamdata[i].win);
					score.push(teamdata[i].score);
					rebounds.push(teamdata[i].total_rebounds);
					assists.push(teamdata[i].assists);
					one_rate.push(teamdata[i].penalty_hit_percentage);
					two_rate.push(teamdata[i].hit_percentage);
					three_rate.push(teamdata[i].three_point_hit_percentage);
				}
				if(StatType==1){ // win
					series.push({
						name : 'Win matches',
						data : win,
						color : "#ffaa7f"
					})
				}
				if(StatType==2){ // score
					series.push({
						name : 'Score',
						data : score,
						color : '#ff5500'
					})
				}
				if(StatType==3){ // rebounds
					series.push({
						name : 'Rebounds',
						data : rebounds,
						color : '#aaffff'
					})
				}
				if(StatType==4){ // assists
					series.push({
						name : 'Assists',
						data : assists,
						color : '#aaaa00',
					})
				}
				if(StatType==5){ // rate
					series.push({
						name : 'Total hit rate',
						data : two_rate,
						color : 'white',
					})
					series.push({
						name : 'Three point hit rate',
						data : three_rate,
						color : '#55aaff',
					})
					series.push({
						name : 'Penalty hit rate',
						data : one_rate,
						color : '#55ff00',
					})
				}
				Line.categories = categories;
				Line.series = series;
				_self.showLine('canvasLine', Line);
			},
			showLine(canvasId, chartData){
				Line = new uCharts({
					context : uni.createCanvasContext(canvasId, _self),
					$this : _self,
					canvasId : canvasId,
					type : 'line',
					legend : true,
					animation : true,
					dataLabel : true,
					categories : chartData.categories,
					series : chartData.series,
					width : 500,
					height : 500
				});
			},
			StatType(e) {
				this.StatTypeIndex = e.target.value;
				this.StatTypeArrayType=this.StatTypeArray[this.StatTypeIndex]
				this.getServerData()
			}
		}
	}
</script>


<style>
	page{
		width: 100%;
		height: auto;
		color:#333;
		background: url('../../static/bg.jpg') no-repeat;
		background-size: 100% 100%;
	}
	@-webkit-keyframes fadeIn{ 0%{opacity:0; } 100%{opacity:1;} }
	.container {
		/* padding: 20upx; */
		/* font-size: 14upx; */
		/* line-height: 24upx; */
		/* height: 100%; */
		/* width: 100%; */
		/* background: url("../../static/bg01warp.png") 50% 50% no-repeat; */
	}
	.coaches{
		flex-direction: column;
	}
	.coach_info{
		display: flex;
		flex-direction: column;
	}
	.coach_img{
		margin-left: 250upx;
		margin-top: -75upx;
		height: 300upx;
		width: 300upx;
	}
	.coach_img:hover{
		cursor: pointer;
		transform: scale(1.5, 1.5);
	}
	.team_name{
		font-size: 40upx;
	}
	.player_img{
		width: 150upx;
		height: 150upx;
	}
	.player_img:hover{
		cursor: pointer;
		transform: scale(2, 2);
	}
	.header{
	    width: 100%;
	    height: 80px;
	    padding:0 20px;
	    min-width: 1366px;
	}
	.bg_header{
	    width: 100%;
	    height: 80px;
	    background: url(../../static/title.png) no-repeat;
	    background-size: 100% 100%;
	}
	.t_title{
	    width: 100%;
	    height: 100%;
	    text-align: center;
	    font-size: 2.5em;
	    line-height: 80px;
	    color: #fff;
	}
	.data_content{
	    min-width: 1366px;
	    padding-top: 20px;
	    padding-bottom: 20px;
	}
	.data_content .data_main{
	    width: calc(100% - 40px);
	    margin-bottom: 40px;
	    height: 615px;
	    margin-left: 20px;
	}
	.data_content .data_main .main_left{
	    width: 24%;
	}
	.data_content .data_main .main_left>view{
	    width: 100%;
	    height: 280px;
	    box-sizing: border-box;
	    border: 1px solid #2C58A6;
	    position: relative;
	    box-shadow: 0 0 10px #2C58A6;
	}
	.data_content .data_main .main_left view:nth-child(1){
	    margin-bottom: 50px;
	}
	.data_content .data_main .main_left view .main_title{
	    width: 245px;
	    height: 35px;
	    line-height: 33px;
	    background-color: #2C58A6;
	    border-radius: 18px;
	    position: absolute;
	    top: -40px;
	    left: 40%;
	    margin-left: -90px;
	    color:#fff;
	    font-size: 18px;
	    font-weight: 600;
	    box-sizing: border-box;
	    padding-left: 45px;
	    z-index: 1000;
	    text-align: center;
	}
	.data_content .data_main .main_left view .main_title img{
	    position: absolute;
	    top: 8px;
	    left: 20px;
	}
	.data_content .data_main .main_center{
	    width: 52%;
	    height: 610px;
	}
	.data_content .data_main .main_center .center_text{
	    width: calc(100% - 50px);
	    height: 610px;
	    margin-left: 25px;
	    margin-right: 25px;
	    box-sizing: border-box;
	    border: 1px solid #2C58A6;
	    box-shadow: 0px 0px 6px #2C58A6;
	    position: relative;
	}
	.l_t_line{
	    width: 5px;
	    height: 24px;
	    left: -3px;
	    top: -3px;
	}
	.t_l_line{
	    height: 5px;
	    width: 26px;
	    left: -3px;
	    top: -3px;
	}
	.t_line_box {
	    position: absolute;
	    width: 100%;
	    height: 100%;
	}
	.t_line_box i{
	    background-color: #4788fb;
	    box-shadow: 0px 0px 10px #4788fb;
	    position: absolute;
	}
	.t_r_line{
	    height: 5px;
	    width: 26px;
	    right: -3px;
	    top: -3px;
	}
	.r_t_line{
	    width: 5px;
	    height: 24px;
	    right: -3px;
	    top: -3px;
	}
	.l_b_line{
	    width: 5px;
	    height: 24px;
	    left: -3px;
	    bottom: -3px;
	}
	.b_l_line{
	    height: 5px;
	    width: 26px;
	    left: -3px;
	    bottom: -3px;
	}
	.r_b_line{
	    width: 5px;
	    height: 24px;
	    right: -3px;
	    bottom: -3px;
	}
	.b_r_line{
	    height: 5px;
	    width: 26px;
	    right: -3px;
	    bottom: -3px;
	}
	.data_content .data_main .main_center .main_title{
	    width: 180px;
	    height: 35px;
	    line-height: 33px;
	    background-color: #2C58A6;
	    border-radius: 18px;
	    position: absolute;
	    top: -17px;
	    left:50%;
	    margin-left: -90px;
	    color:#fff;
	    font-size: 18px;
	    font-weight: 600;
	    box-sizing: border-box;
	    padding-left: 45px;
	    z-index: 1000;
		text-align: center;
	}
	.data_content .data_main .main_center .main_title img{
	    position: absolute;
	    top: 8px;
	    left: 20px;
	}
	.data_content .data_main .main_right{
	    width: 24%;
	}
	.data_content .data_main .main_right>view{
	    width: 100%;
	    height: 280px;
	    box-sizing: border-box;
	    border: 1px solid #2C58A6;
	    position: relative;
	    box-shadow: 0 0 10px #2C58A6;
	}
	.data_content .data_main .main_right view:nth-child(1){
	    margin-bottom: 50px;
	}
	.data_content .data_main .main_right view .main_title{
	    width: 180px;
	    height: 35px;
	    line-height: 33px;
	    background-color: #2C58A6;
	    border-radius: 18px;
	    position: absolute;
	    top: -17px;
	    left:50%;
	    margin-left: -90px;
	    color:#fff;
	    font-size: 18px;
	    font-weight: 600;
	    box-sizing: border-box;
	    padding-left: 45px;
		text-align: center;
	}
	.data_content .data_main .main_right view .main_title img{
	    position: absolute;
	    top: 8px;
	    left: 20px;
	}
	.t_btn8,.t_btn2,.t_btn3{
	    position: relative;
	    z-index: 100;
	    cursor: pointer;
	}
	.fl{
	    float: left;
	}
	.fr{
	    float: right;
	}
	.img{
		position: relative;
		float: left;
		width: 30px; 
		height: 40px; 
		margin: auto;
		left: -25px;
	}
	.img:hover{
		width: 50px;
		height: 40px;
	}
	.chart {
		position: relative;
		left: -15px; 
		top: 3px; 
		line-height: 1; 
		min-width: 818px; 
		height: 55px; 
		overflow: hidden;
	}
	.chart li {
		transition: all 0.1s ease;  
		cursor: pointer; 
		position: relative; 
		display: inline-block; 
		overflow: hidden; 
		width: 115px; 
		height: 44px; 
		padding: 10px 0 0 30px; 
		background: url(../../static/bg01bigindex.png) 0 0 no-repeat; 
		margin-right: 15px;
	}
	.chart li strong { 
		display: block; 
		color: #fff;
		position: relative;
		left: -10px;
		font-family:'electronicFont'; 
		font-size: 20px; 
		font-weight: normal;
	}
	@font-face { font-family:'electronicFont'; src: url("../../static/font/DS-DIGI.TTF"); }
	.chart li .animation-1 {
		-webkit-animation-iteration-count: infinite;   
		-webkit-animation-name:bounceInLeft1 ; 
		-webkit-animation-duration: 9000ms; 
		position: absolute; 
		left: 12px; 
		bottom:1px; 
		height: 3px;  
		width: 345px; 
		background: url(../../static/bg04bigindex.png) 0 0 repeat-x;
	}
	.chart li .animation-2 {
		position: absolute; 
		right:0; 
		top:1px; 
		height: 16px;  
		width: 15px; 
		background: url(../../static/bg02bigindex.png) 0 0 no-repeat;
	}
	.chart li .animation-3 {
		position: absolute; 
		right:-1px; 
		bottom:-1px; 
		height: 4px;  
		width: 4px; 
		background: url(../../static/bg03bigindex.png) 50% 50% no-repeat;
	}
	.chart li:hover .animation-2 { 
		background: url(../../static/bg02bigindex_.png) 0 0 no-repeat;
	}
	.chart li:hover .animation-3 {  
		background: url(../../static/bg03bigindex_.png) 50% 50% no-repeat;
	}
	.chart li:hover .animation-1 {
		-webkit-animation-iteration-count: infinite;   
		-webkit-animation-name:bounceInRight1 ; 
		-webkit-animation-duration:4000ms;
	}
	.chart li:hover .animation-2, .chart li:hover .animation-3{ 
		-webkit-animation:flash .2s .2s ease both; 
		-moz-animation:flash .2s .2s ease both;
	}
	@media screen and (max-width: 1366px) {
	   .chart li:nth-child(6) { display: none;}
	   .chart li { margin-right: 6px;}
	}
	@-webkit-keyframes bounceInLeft1{
	    0%{-webkit-transform:translateX(-115px)}
	    100%{-webkit-transform:translateX(0)}
	}
	@-webkit-keyframes bounceInRight1{
	    0%{-webkit-transform:translateX(0)}
	    100%{-webkit-transform:translateX(-115px)}
	}
	.chart{
	    -webkit-animation:fadeInDown 1s .2s ease both;
	    -moz-animation:fadeInDown 1s .2s ease both;}
	@-webkit-keyframes fadeInDown{
	    0%{opacity:0;
	        -webkit-transform:translateY(-20px)}
	    100%{opacity:1;
	        -webkit-transform:translateY(0)}
	}
	@-moz-keyframes fadeInDown{
	    0%{opacity:0;
	        -moz-transform:translateY(-20px)}
	    100%{opacity:1;
	        -moz-transform:translateY(0)}
	}
	.picker-view{
		display: block;
		width: 100px;
		height: 40px;
		margin-top: 5px;
	}
	.item {
		display: block;
		color: #fff;
		font-size: 18px; 
		height: 40px;
		align-items: center;
		justify-content: center;
		text-align: center;
	}
	.pandect-area-center { 
		display: block;
		margin-top: 20px; 
		overflow: hidden;
	}
	.charts{
		display: block;
		position: relative;
		float: left;
		margin: auto;
		top: 20px;
		left: 0;
		width: 170px;
		height: 230px;
	}
	.charts2{
		display: block;
		position: relative;
		float: left;
		margin: auto;
		top: 10px;
		left: 70px;
		width: 300px;
		height: 230px;
	}
	.te1{
		display: block;
		color: #fff;
		position: relative;
		float: left;
		left: 8%;
		height: 20px;
	}
	.te2{
		display: block;
		color: #fff;
		position: relative;
		float: left;
		left: 13%;
		height: 20px;
	}
	.te3{
		color: #fff;
		display: block;
		position: relative;
		float: left;
		left: 16%;
		height: 20px;
	}
	.te4{
		color: #fff;
		display: block;
		position: relative;
		float: left;
		left: 23%;
		height: 20px;
	}
	.te5{
		display: block;
		color: #fff;
		position: relative;
		float: left;
		left: 11%;
		height: 20px;
	}
	.te6{
		display: block;
		color: #fff;
		position: relative;
		float: left;
		left: 28%;
		height: 20px;
	}
	.te7{
		color: #fff;
		display: block;
		position: relative;
		float: left;
		left: 47%;
		height: 20px;
	}
	.te8{
		color: #fff;
		display: block;
		position: relative;
		float: left;
		left: 66%;
		height: 20px;
	}
</style>
