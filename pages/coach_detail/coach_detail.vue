<template>
	<view class="container">
		<uni-card>
			<view style="flex-direction: row; display: flex;">
				<image :src="coach_full_img" style="height: 400upx; width: 400upx; margin-left: 500upx;"></image>
				<view style="margin-left: 830upx; text-align: center;">
					<view style="font-size: 40upx;">{{coach_name}}</view>
					<view style="margin-top: 40upx; font-size: 30upx;">{{birthday}}</view>
					<view style="margin-top: 40upx; font-size: 30upx;">{{birthcity}}</view>
				</view>
				<image :src="coach_img" style="margin-left: 900upx; height: 200upx; width: 200upx; margin-top: 100upx;"></image>
			</view>
		</uni-card>
		<uni-card>
			<view style="display: flex; flex-direction: row;">
				<canvas canvas-id="canvasLine" id="canvasLine" style="margin-left: 400upx; margin-top: 100upx; height: 600upx; width: 600upx;"></canvas>
				<canvas canvas-id="canvasPie" id="canvasPie" style="margin-left: 1600upx; margin-top: 100upx; height: 600upx; width: 600upx;"></canvas>
			</view>
			
		</uni-card>
		
	</view>
</template>

<script>
	import uCharts from '../../components/u-charts/u-charts.js';
	var canvaLine = null;
	var canvaPie = null;
	var _self;
	export default {
		data() {
			return {
				coach_name : 'Steve Kerr',
				coach_img : 'https://www.basketball-reference.com/req/202106291/images/coaches/kerrst01c.png',
				coach_full_img : 'https://images2.minutemediacdn.com/image/fetch/w_850,h_560,c_fill,g_auto,f_auto/https%3A%2F%2Fgoldengatesports.com%2Fwp-content%2Fuploads%2Fgetty-images%2F2018%2F08%2F1214343539-850x560.jpeg',
				birthday : '1966-9-1',
				birthcity : 'New York',
				categories : ['2016', '2017', '2018', '2019', '2020', '2021'],
				series : [{
					name : 'win rate(%)',
					data : [81.7, 89.0, 81.7, 70.7, 69.5, 23.1],
					color : '#000000'
				}],
				coach_data : [
					{
						win_rate : 81.7
					},
					{
						win_rate : 89.0
					},
					{
						win_rate : 81.7
					},
					{
						win_rate : 70.7
					},
					{
						win_rate : 69.5
					},
					{
						win_rate : 23.1
					},
				],
				avg_data : {
					win_rate : 70.9,
					win : 337,
					lose : 138
				}
			}
		},
		
		onLoad() {
			uni.request({
				url: '',
				method: 'GET',
				data: {},
				success: res => {},
				fail: () => {},
				complete: () => {}
			});
			_self = this;
			let Line = {categories:[], series:[]};
			Line.categories = _self.categories;
			Line.series = _self.series;
			
			let Pie = {series:[]};
			let avg_data = _self.avg_data;
			Pie.series.push({
				"name" : "Win",
				"data" : avg_data.win
			});
			Pie.series.push({
				"name" : "Lose",
				"data" : avg_data.lose 
			});
			this.showLine("canvasLine", Line);
			this.showPie("canvasPie", Pie);
		},
		methods: {
			 showLine(canvasId,chartData){
				canvaLine=new uCharts({
					context: uni.createCanvasContext(canvasId, _self),
					$this:_self,
					canvasId: canvasId,
					type: 'line',
					fontSize:11,
					legend:true,
					dataLabel:false,
					dataPointShape:true,
					background:'#FFFFFF',
					pixelRatio:_self.pixelRatio,
					categories: chartData.categories,
					series: chartData.series,
					animation: true,
					xAxis: {
						type : 'grid',
						gridColor : '#CCCCCC',
						gridType : 'dash',
						dashLength : 8
					},
					yAxis : {
						gridType : 'dash',
						gridColor : '#CCCCCC',
						dashLength: 8,
					},
					width: 300,
					height: 300,
					extra: {
						line:{
							type: 'straight'
						}
					}
				});
			},
			showPie(canvasId, chartData){
				canvaPie = new uCharts({
					$this : _self,
					canvasId : canvasId,
					context: uni.createCanvasContext(canvasId, _self),
					type : 'pie',
					fontSize : 11,
					legend : true,
					background : '#FFFFFF',
					series : chartData.series,
					animation : true,
					width : 300,
					height : 300,
					dataLabel : true,
					extra : {
						pie : {
							labelWidth : 20
						}
					},
				});
			}
		}
	}
</script>

<style>
	.container {
		/* padding: 20upx;
		font-size: 14upx;
		line-height: 24upx; */
	}
	.charts {
		width: 750upx; 
		height:500upx;
		background-color: #FFFFFF;
		margin-top: 100upx;
	}
</style>
