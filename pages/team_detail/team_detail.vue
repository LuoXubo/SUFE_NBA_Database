<template>
	<view class="container">
		<!-- 球队及教练信息 -->
		<uni-card>
			<view style="display: flex; flex-direction: row; margin-top: 100upx;">
				<view style="display: flex; flex-direction: column; margin-left: 400upx;">
					<view style="font-size: 60upx; margin-top: 10upx;">{{team_name}}</view>
					<view style="font-size: 30upx; margin-top: 30upx; color: gray;">{{team_name_cn}}</view>
					<view style="margin-top: 30upx; font-size: 30upx;">Address: {{team_city}}</view>
					<view style="margin-top: 30upx; font-size: 30upx;">Motto: {{team_info}}</view>
				</view>
				
				<image :src="team_img" style="margin-left: 550upx;"></image>
				<view class="coaches" style="position: absolute; right: 500upx;">
					<view class="coach_info">
						<image class="coach_img" :src="coach.photo" @tap="to_coach_detail(coach.id)"></image>
						<view style="font-size: 30upx;">{{coach.name}}</view>
					</view>
				</view>
			</view>
		</uni-card>
		
		<!-- 球队数据 -->
		<uni-card>
			<view>
				<picker @change="StatType" :range="StatTypeArray">
					<label>Stat type : </label>
					<label class="">{{StatTypeArrayType}}</label>
				</picker>
			</view>
		</uni-card>
		
		<!-- 球员信息 -->
		<uni-card>
			<view style="display: flex; flex-direction: row;">
				<canvas canvas-id="canvasLine" id="canvasLine"></canvas>
				<view style="margin-top: 100upx;">
					<view v-for="(item,index) in player" style="margin-left: 100upx; margin-top: 50upx;">
						<view style="display: flex; flex-direction: row;">
							<image :src="item.photo" class="player_img" @tap="to_player_detail(item.id)"></image>
							<view style="font-size: 40upx; margin-left: 40upx; margin-top: 50upx;">{{item.name}}</view>
							<view style="font-size: 30upx; margin-left: 40upx; margin-top: 50upx;">{{item.uniform_number}}</view>
						</view>
					</view>
				</view>
			</view>
		</uni-card>
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
			// console.log(team_id);
			// uni.request({
			// 	url: '',
			// 	method: 'GET',
			// 	data: {},
			// 	success: res => {
			// 		var data = res.data;
			// 		this.team_img = data.photo;
			// 		this.team_name = data.name_e;
			// 		this.team_name_cn = data.name_c;
			// 		this.team_info = data.slogan;
			// 		this.team_city = data.area;
			// 		this.stadium = data.stadium;
			// 		this.coach_img = data.coach.photo;
			// 		this.coach_name = data.coach.name;
			// 		this.player = data.player;
			// 		this.team_data = data.teamdata;
			// 	},
			// 	fail: (err) => {console.log(err)},
			// 	complete: () => {}
			// });
			this.getServerData();
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
				// console.log(teamdata[0].score)
				for(let i=0;i<teamdata.length;i++){
					// categories.push(this.team_data[i].season);
					// win.push(this.team_data[i].win);
					// score.push(this.team_data[i].score);
					// rebounds.push(this.team_data[i].total_rebounds);
					// assists.push(this.team_data[i].assists);
					// one_rate.push(this.team_data[i].penalty_hit_percentage);
					// two_rate.push(this.team_data[i].hit_percentage);
					// three_rate.push(this.team_data[i].three_point_hit_percentage);
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
						color : "#000000"
					})
				}
				if(StatType==2){ // score
					series.push({
						name : 'Score',
						data : score,
						color : '#000000'
					})
				}
				if(StatType==3){ // rebounds
					series.push({
						name : 'Rebounds',
						data : rebounds,
						color : '#000000'
					})
				}
				if(StatType==4){ // assists
					series.push({
						name : 'Assists',
						data : assists,
						color : '#000000',
					})
				}
				if(StatType==5){ // rate
					series.push({
						name : 'Total hit rate',
						data : two_rate,
						color : '#000000',
					})
					series.push({
						name : 'Three point hit rate',
						data : three_rate,
						color : '#000000',
					})
					series.push({
						name : 'Penalty hit rate',
						data : one_rate,
						color : '#000000',
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
	.container{
		padding: 20upx;
		font-size: 14upx;
		line-height: 24upx;
		
	}
	
	.coaches{
		flex-direction: column;
	}
	.coach_info{
		flex-direction: column;
		display: flex;
	}
	.coach_img{
		height: 150upx;
		width: 150upx;
	}
	.coach_img:hover{
		height: 300upx;
		width: 300upx;
	}
	.team_name{
		font-size: 40upx;
	}
	.player_img{
		width: 150upx;
		height: 150upx;
	}
	.player_img:hover{
		width: 300upx;
		height: 300upx;
	}
</style>
