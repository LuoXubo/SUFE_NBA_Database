<template>
	<view class="container">
		<uni-card>
			<view style="flex-direction: row; display: flex;">
				<image :src="player_img_full" class="player_img_full"></image>
				<view style="margin-left: 900upx; margin-top: 100upx; text-align: center;">
					<view style="font-size: 40upx;">{{name}}</view>
					<view style="font-size: 30upx;">{{number}}</view>
					<view style="font-size: 30upx;">{{position}}</view>
					<view style="font-size: 30upx;">{{height}}, {{weight}}</view>
				</view>
				<image :src="player_img" class="player_img"></image>
			</view>
		</uni-card>
		<uni-card>
			<view style="flex-direction: row; display: flex; height:800upx; margin-left: 100upx;">
				<canvas canvas-id="ScoreCanva" id="ScoreCanva"></canvas>
				<view style="margin-left: 950upx; margin-right: 700upx; margin-top: 300upx; font-size: 40upx;">
					Score : {{detail.score}}
				</view>
				<canvas canvas-id="OtherCanva" id="OtherCanva"></canvas>
			</view>
		</uni-card>
		<button @click="to_career_detail(id)" class="to_career_button">Career Data</button>
	</view>
</template>

<script>
	import uCharts from '../../components/u-charts/u-charts.js';
	var	_self;
	var ScoreCanva = null;
	var OtherCanva = null;
	export default {
		data (){
			return{
				cWidth : '',
				cHeight : '',
				pixelRatio : 1,
				name : 'Stephen Curry',
				number : '30',
				position : 'Guard',
				height : '191cm',
				weight : '84kg',
				player_img : 'https://cdn.nba.com/headshots/nba/latest/1040x760/201939.png',
				player_img_full : 'https://marstranslator-images-sz.oss-cn-shenzhen.aliyuncs.com/cover_images/15849649128543.jpg',
				id : 100,
				detail : {
					season : '20-21',
					team : 'Warriors',
					number_of_states : 40,
					time : 100,
					win : 27,
					lose : 13,
					hit_percentage : 40,
					three_point_hit_percentage : 40,
					penalty_hit_percentage : 92,
					total_rebounds : 6,
					assists : 6,
					snatch : 3,
					blocks : 4,
					miss : 3,
					foul : 3,
					score : 27,
				}
			}
		},
		onLoad(option){
			this.id = option.id;
			this.cWidth = uni.upx2px(500);
			this.cHeight = uni.upx2px(500);
			// uni.request({
			// 	url: '',
			// 	method: 'GET',
			// 	data: {
			// 		id : this.id
			// 	},
			// 	success: res => {
			// 		let data = res.data;
			// 		this.player_img = data.photo;
			// 		this.name = data.name;
			// 		this.position = data.position;
			// 		this.height = datllla.height;
			// 		this.weight = data.weight;
			// 		this.birthday = data.date_of_birth;
			// 		this.detail = data.detail;
			// 	},
			// 	fail: (err) => {
			// 		console.log(err);
			// 	},
			// 	complete: () => {}
			// });
			_self = this;
			
			this.getServerData();
		},
		methods:{
			to_career_detail(id) {
				uni.navigateTo({
					url: './career_detail?id='+id,
					success: res => {},
					fail: () => {},
					complete: () => {}
				});
			},
			getServerData(){
				var scoreCat = ['Hit Rate', 'Three Point Rate', 'Penalty Rate'];
				var otherCat = ['Rebound', 'Assist', 'Block', 'Steal'];
				var scoreSe = [{
					name : this.name,
					data : [this.detail.hit_percentage, this.detail.three_point_hit_percentage, this.detail.penalty_hit_percentage]
				}];
				var otherSe = [{
					name : this.name,
					data : [this.detail.total_rebounds, this.detail.assists, this.detail.blocks, this.detail.snatch]
				}];
				let ScoreRadar = {categories:scoreCat, series:scoreSe};
				let OtherRadar = {categories:otherCat, series:otherSe};
				_self.showRadar('ScoreCanva', ScoreRadar);
				_self.showRadar('OtherCanva', OtherRadar);
			},
			showRadar(canvasId, chartData){
				ScoreCanva = new uCharts({
					$this : _self,
					canvasId : canvasId,
					context : uni.createCanvasContext(canvasId, _self),
					type : 'radar',
					fontSize : 11,
					legend : true,
					animation : true,
					dataLabel : true,
					categories : chartData.categories,
					series : chartData.series,
					// pixelRatio : _self.pixelRatio,
					// width : _self.cWidth * _self.pixelRatio,
					// height : _self.cHeight * _self.pixelRatio,
					width : 300,
					height : 300
				});
				
			}
		}
	}
</script>

<style>
	.container {
		padding: 20upx;
		font-size: 14upx;
		line-height: 24upx;
	}
	.to_career_button{
		width: 400upx; 
		height: 100upx; 
		font-size: 40upx; 
		border-radius: 20upx;
		background-color: #18BC37;
		color: white;
	}
	.player_img{
		width: 300upx; 
		height: 300upx; 
		margin-left: 800upx; 
		margin-top: 150upx;
	}
	.player_img:hover{
		width: 600upx;
		height: 600upx; 
	}
	.player_img_full{
		width: 600upx; 
		height: 600upx; 
		margin-left: 200upx; 
		border-radius: 20upx;
	}
</style>
