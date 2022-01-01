
<template>
	<view class="container">
		<view style="flex-direction: row; ">
			
			
		</view>
		<canvas canvas-id="canvasColumn" id="canvasColumn" class="charts"></canvas>
	</view>
</template>

<script>
	import uCharts from '../../components/u-charts/u-charts.js';
	var canvasColumn = null;
	var _self;
	data() {
		return {
			coach_name : 'Steve Kerr',
			coach_img : 'https://www.basketball-reference.com/req/202106291/images/coaches/kerrst01c.png',
			coach_data : [
				{
					win_rate : 81.7%
				},
				{
					win_rate : 89.0%
				},
				{
					win_rate : 81.7%
				},
				{
					win_rate : 70.7%
				},
				{
					win_rate : 69.5%
				},
				{
					win_rate : 23.1%
				},
			],
			avg_data : {
				win_rate : 70.9%,
				win : 337,
				lose : 138
			}
		}
	},
	
	onLoad() {
		_self = this;
		this.showLine("canvasColumn", Line)
	},
	methods: {
		
	}
	
</script>

<style>
	.container {
		padding: 20upx;
		font-size: 14upx;
		line-height: 24upx;
	}
	.charts {
		width: 750upx; 
		height:500upx;
		background-color: #FFFFFF;
		}
</style>
