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
			<picker @change="StatType" :range="StatTypeArray" style="margin-left: 1700upx; font-size: 40upx;">
				<label>Stat type : </label>
				<label class="">{{StatTypeArrayType}}</label>
			</picker>
			<canvas canvas-id="canvasLine" id="canvasLine" @touchstart="touchLine" style="height: 750upx; width: 1000upx; margin-top: 100upx; margin-left: 1300upx;"></canvas>
		</uni-card>
	</view>
</template>

<script>
	import uCharts from '../../components/u-charts/u-charts.js';
	var	_self;
	var canvaLine = null;
	export default {
		data() {
			return {
				StatTypeArray:['---Please select---','Score','Basket','Assist'],
				StatTypeIndex:0,
				StatTypeArrayType:'---Please select---',
				
				cWidth:'',
				cHeight:'',
				pixelRatio:1,
				name : 'Stephen Curry',
				number : '30',
				position : 'Guard',
				height : '191cm',
				weight : '84kg',
				player_img : 'https://cdn.nba.com/headshots/nba/latest/1040x760/201939.png',
				player_img_full : 'https://marstranslator-images-sz.oss-cn-shenzhen.aliyuncs.com/cover_images/15849649128543.jpg',
				season_data : [
					{
						season : '2021-2022',
						score : 27.7,
						scoring_rate : '43.4%',
						three_rate : '40.0%',
						freethrow_rate : '92.0%',
						basket : 5.3,
						assist : 6.0,
						steal : 1.5,
						block : 0.5
					},
					{
						season : '2020-2021',
						score : 32.0,
						scoring_rate : '48.2%',
						three_rate : '42.1%',
						freethrow_rate : '91.6%',
						basket : 5.5,
						assist : 5.8,
						steal : 1.2,
						block : 0.1
					},
					{
						season : '2019-2020',
						score : 20.8,
						scoring_rate : '40.2%',
						three_rate : '24.5',
						freethrow_rate : '100.0%',
						basket : 5.2,
						assist : 6.6,
						steal : 1.0,
						block : 0.4
					},
				]
			};
		},
		
		onLoad(id){
			this.id = id;
			uni.request({
				url: '',
				method: 'GET',
				data: {
					id : id
				},
				success: res => {
					let data = res.data;
					this.name = data.name;
					this.player_img = data.photo;
					
				},
				fail: () => {},
				complete: () => {}
			});
			_self = this;
			this.cWidth=uni.upx2px(750);
			this.cHeight=uni.upx2px(500);
			this.getServerData();
		},
		
		methods:{
			getServerData(){
				var StatType = this.StatTypeIndex; 
				var season_data = this.season_data;
				var categories = [];
				var score = [];
				var basket = [];
				var assist = [];
				for(let i=0;i<season_data.length;i++){
					categories.push(season_data[i].season);
					score.push(season_data[i].score);
					basket.push(season_data[i].basket);
					assist.push(season_data[i].assist);
				}
				
				var series = [];
				series.push({
					name : 'Score',
					data : score,
					color : '#aa0000'
				});
				series.push({
					name : 'Basket',
					data : basket,
					color : '#00007f'
				});
				series.push({
					name : 'Assist',
					data : assist,
					color : '#55007f'
				});
				
				let Line = {categories:[], series:[]};
				Line.categories = categories;
				if(StatType == 1){
					Line.series = [series[0]];
				}
				if(StatType == 2){
					Line.series = [series[1]];
				}
				if(StatType == 3){
					Line.series = [series[2]];
				}
				_self.showLine('canvasLine', Line);
			},
			showLine(canvasId, chartData){
				canvaLine = new uCharts({
					$this : _self,
					canvasId : canvasId,
					context : uni.createCanvasContext(canvasId, _self),
					type : 'line',
					categories : chartData.categories,
					series : chartData.series,
					fontSize:11,
					legend:true,
					dataLabel:false,
					dataPointShape:true,
					background:'#FFFFFF',
					pixelRatio:_self.pixelRatio,
					
					animation : true,
					xAxis : {
						type : 'grid',
						gridColor : '#CCCCCC',
						gridType : 'dash',
						dashLength : 8
					},
					yAxis: {
					    gridType:'dash',
					    gridColor:'#CCCCCC',
					    dashLength:8,
					    // splitNumber:5,
					    min:0,
					    max:40,
					},
					// width: _self.cWidth*_self.pixelRatio,
					// height: _self.cHeight*_self.pixelRatio,
					width : 500,
					height : 500,
					
					extra: {
					    line:{
					        type: 'straight'
					    }
					}
				});
			},
			touchLine(e){
				canvaLine.showToolTip(e, {
					format : function (item, category) {
						return category + ' ' + item.name + ':' + item.data 
					}
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
	.container {
		padding: 20upx;
		font-size: 14upx;
		line-height: 24upx;
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
