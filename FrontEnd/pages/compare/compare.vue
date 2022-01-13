<template>
	<view class="compare">
		<view class="header">
		    <view class="bg_header">
		        <view class="t_title">
		            Player Comparison
		        </view> 
		    </view>
		</view>
		<view class="data_content">
			<view class="data_main">
				<view class="main_left fl">
					<view class="left_1 t_btn6" style="cursor: pointer;">
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
							20 players
						</view>
						<view class="chart">
							<ul>
								<li>
									<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
									<image class="img" :src="player[0].img"></image>
									<strong @click="sel">{{player[0].name}}</strong>
								</li>
								<li>
									<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
									<image class="img" :src="player[1].img"></image>
									<strong @click="sel">{{player[1].name}}</strong>
								</li>
							</ul>
						</view>
						<view class="chart">
							<ul>
								<li>
									<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
									<image class="img" :src="player[2].img"></image>
									<strong @click="sel">{{player[2].name}}</strong>
								</li>
								<li>
									<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
									<image class="img" :src="player[3].img"></image>
									<strong @click="sel">{{player[3].name}}</strong>
								</li>
							</ul>
						</view>
						<view class="chart">
							<ul>
								<li>
									<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
									<image class="img" :src="player[4].img"></image>
									<strong @click="sel">{{player[4].name}}</strong>
								</li>
								<li>
									<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
									<image class="img" :src="player[5].img"></image>
									<strong @click="sel">{{player[5].name}}</strong>
								</li>
							</ul>
						</view>
						<view class="chart">
							<ul>
								<li>
									<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
									<image class="img" :src="player[6].img"></image>
									<strong @click="sel">{{player[6].name}}</strong>
								</li>
								<li>
									<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
									<image class="img" :src="player[7].img"></image>
									<strong @click="sel">{{player[7].name}}</strong>
								</li>
							</ul>
						</view>
						<view class="chart">
							<ul>
								<li>
									<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
									<image class="img" :src="player[8].img"></image> 
									<strong @click="sel">{{player[8].name}}</strong>
								</li>
								<li>
									<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
									<image class="img" :src="player[9].img"></image>
									<strong @click="sel">{{player[9].name}}</strong>
								</li>
							</ul>
						</view>
					</view>
					<view class="left_2" style="cursor: pointer;">
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
						<view class="chart">
							<ul>
								<li>
									<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
									<image class="img" :src="player[10].img"></image>
									<strong @click="sel">{{player[10].name}}</strong>
								</li>
								<li>
									<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
									<image class="img" :src="player[11].img"></image>
									<strong @click="sel">{{player[11].name}}</strong>
								</li>
							</ul>
						</view>
						<view class="chart">
							<ul>
								<li>
									<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
									<image class="img" :src="player[12].img"></image>
									<strong @click="sel">{{player[12].name}}</strong>
								</li>
								<li>
									<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
									<image class="img" :src="player[13].img"></image>
									<strong @click="sel">{{player[13].name}}</strong>
								</li>
							</ul>
						</view>
						<view class="chart">
							<ul>
								<li>
									<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
									<image class="img" :src="player[14].img"></image>
									<strong @click="sel">{{player[14].name}}</strong>
								</li>
								<li>
									<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
									<image class="img" :src="player[15].img"></image>
									<strong @click="sel">{{player[15].name}}</strong>
								</li>
							</ul>
						</view>
						<view class="chart">
							<ul>
								<li>
									<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
									<image class="img" :src="player[16].img"></image>
									<strong @click="sel">{{player[16].name}}</strong>
								</li>
								<li>
									<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
									<image class="img" :src="player[17].img"></image>
									<strong @click="sel">{{player[17].name}}</strong>
								</li>
							</ul>
						</view>
						<view class="chart">
							<ul>
								<li>
									<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
									<image class="img" :src="player[18].img"></image>
									<strong @click="sel">{{player[18].name}}</strong>
								</li>
								<li>
									<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
									<image class="img" :src="player[19].img"></image>
									<strong @click="sel">{{player[19].name}}</strong>
								</li>
							</ul>
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
							select & compare
						</view>
						<view class="blank" style="height: 30px;"></view>
						<view class="chart">
							<ul>
								<li>
									<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
									<picker-view :indicator-style="indicatorStyle" class="picker-view" @change="change1">
										<picker-view-column>
											<view class="item" v-for="(item, index) in player" :key="player.id">{{player[index].name}}</view>
										</picker-view-column>
									</picker-view>
								</li>
								<li>
									<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
									<picker-view :indicator-style="indicatorStyle" class="picker-view" @change="change2">
										<picker-view-column>
											<view class="item" v-for="(item, index) in player" :key="player.id">{{player[index].name}}</view>
										</picker-view-column>
									</picker-view>
								</li>
								<li @click="ok">
									<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
									<view class="item">compare!</view>
								</li>
							</ul>
						</view>
						<view class="pandect-area-center">
							<canvas canvas-id="canvasPie1" id="canvasPie" class="charts" ></canvas>
							<canvas canvas-id="canvasPie2" id="canvasPie" class="charts" ></canvas>
							<canvas canvas-id="canvasPie3" id="canvasPie" class="charts" ></canvas>
							<canvas canvas-id="canvasPie4" id="canvasPie" class="charts" ></canvas>
						</view>
						<view class="te1">
							hit_percentage 
						</view>
						<view class="te2">
							three_point_hit_percentage 
						</view>
						<view class="te3">
							total_rebounds 
						</view>
						<view class="te4">
							penalty_hit_percentage
						</view>
						<view class="pandect-area-center">
							<canvas canvas-id="canvasPie5" id="canvasPie" class="charts" ></canvas>
							<canvas canvas-id="canvasPie6" id="canvasPie" class="charts" ></canvas>
							<canvas canvas-id="canvasPie7" id="canvasPie" class="charts" ></canvas>
						</view>
						<view class="te5">
							assists 
						</view>
						<view class="te6">
							snatch 
						</view>
						<view class="te7">
							blocks 
						</view>
					</view>
				</view>
				<view class="main_right fr">
					<view class="right_1">
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
							score
						</view>
						<view class="pandect-area-center">
							<canvas canvas-id="canvasPie9" id="canvasPie" class="charts2" ></canvas>
						</view>
					</view>
					<view class="right_2">
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
						<view class="main_title" style="width:200px;">
							<img src="../../static/ct_5.png" alt="">
							foul
						</view>
						<view class="pandect-area-center">
							<canvas canvas-id="canvasPie10" id="canvasPie" class="charts2" ></canvas>
						</view>
					</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	import uCharts from '../../components/u-charts/u-charts.js';
	var _self;
	var canvaPie = null;
	export default {
		data () {
			return {
				sel1: 0,
				sel2: 0,
				indicatorStyle: 'height: 40px',
				pixelRatio: 1,
				player1: [{
					/* hit_percentage: 0.3,
					three_point_hit_percentage: 0.4,
					penalty_hit_percentage: 0.6,
					total_rebounds: 100,
					assists: 90,
					snatch: 80,
					blocks: 70,
					miss: 60,
					foul: 50,
					score: 40,
					id: 1,
					name: 'Stephen Curry', */
				}],
				player2: [{
					/* hit_percentage: 0.3,
					three_point_hit_percentage: 0.4,
					penalty_hit_percentage: 0.6,
					total_rebounds: 100,
					assists: 90,
					snatch: 80,
					blocks: 70,
					miss: 60,
					foul: 50,
					score: 40,
					id: 2,
					name: 'Draymond Green', */
				}],
				player: [
					/* {
						img: 'https://cdn.nba.com/headshots/nba/latest/1040x760/201939.png',
						name: 'Stephen Curry',
						id: 1
					},
					{
						img: 'https://cdn.nba.com/headshots/nba/latest/1040x760/203110.png',
						name: 'Draymond Green',
						id: 2
					},
					{
						img: 'https://cdn.nba.com/headshots/nba/latest/1040x760/202691.png',
						name: 'Klay Thompson',
						id: 3
					},
					{
						img: 'https://cdn.nba.com/headshots/nba/latest/1040x760/201939.png',
						name: 'Stephen Curry',
						id: 4
					},
					{
						img: 'https://cdn.nba.com/headshots/nba/latest/1040x760/201939.png',
						name: 'Stephen Curry',
						id: 5
					},
					{
						img: 'https://cdn.nba.com/headshots/nba/latest/1040x760/201939.png',
						name: 'Stephen Curry',
						id: 6
					},
					{
						img: 'https://cdn.nba.com/headshots/nba/latest/1040x760/201939.png',
						name: 'Stephen Curry',
						id: 7
					},
					{
						img: 'https://cdn.nba.com/headshots/nba/latest/1040x760/201939.png',
						name: 'Stephen Curry',
						id: 8
					},
					{
						img: 'https://cdn.nba.com/headshots/nba/latest/1040x760/201939.png',
						name: 'Stephen Curry',
						id: 9
					},
					{
						img: 'https://cdn.nba.com/headshots/nba/latest/1040x760/201939.png',
						name: 'Stephen Curry',
						id: 10
					},
					{
						img: 'https://cdn.nba.com/headshots/nba/latest/1040x760/201939.png',
						name: 'Stephen Curry',
						id: 11
					},
					{
						img: 'https://cdn.nba.com/headshots/nba/latest/1040x760/203110.png',
						name: 'Draymond Green',
						id: 12
					},
					{
						img: 'https://cdn.nba.com/headshots/nba/latest/1040x760/202691.png',
						name: 'Klay Thompson',
						id: 13
					},
					{
						img: 'https://cdn.nba.com/headshots/nba/latest/1040x760/201939.png',
						name: 'Stephen Curry',
						id: 14
					},
					{
						img: 'https://cdn.nba.com/headshots/nba/latest/1040x760/201939.png',
						name: 'Stephen Curry',
						id: 15
					},
					{
						img: 'https://cdn.nba.com/headshots/nba/latest/1040x760/201939.png',
						name: 'Stephen Curry',
						id: 16
					},
					{
						img: 'https://cdn.nba.com/headshots/nba/latest/1040x760/201939.png',
						name: 'Stephen Curry',
						id: 17
					},
					{
						img: 'https://cdn.nba.com/headshots/nba/latest/1040x760/201939.png',
						name: 'Stephen Curry',
						id: 18
					},
					{
						img: 'https://cdn.nba.com/headshots/nba/latest/1040x760/201939.png',
						name: 'Stephen Curry',
						id: 19
					},
					{
						img: 'https://cdn.nba.com/headshots/nba/latest/1040x760/201939.png',
						name: 'Stephen Curry',
						id: 20
					},
					 */
				],
			}
		},
		onLoad:function(r){
			var _self = this;
			var that = this;
			uni.request({
				url: "/api/player_comparison/",
				method: "GET",
				data: {},
				success(r) {
					console.log(r);
					for (var i = 0; i < 20; i++) {
						var eachplayer = {id:'', img:'', name:''};
						eachplayer.id = r.data.data[i].id;
						eachplayer.img = r.data.data[i].photo;
						eachplayer.name = r.data.data[i].name_e;
						that.player.push(eachplayer);
					}
					/* that.showColumn("canvasPie1", _self.player1[0].name, _self.player2[0].name, _self.player1[0].hit_percentage, _self.player2[0].hit_percentage);
					that.showColumn("canvasPie2", _self.player1[0].name, _self.player2[0].name, _self.player1[0].three_point_hit_percentage, _self.player2[0].three_point_hit_percentage);
					that.showColumn("canvasPie3", _self.player1[0].name, _self.player2[0].name, _self.player1[0].penalty_hit_percentage, _self.player2[0].penalty_hit_percentage);
					that.showColumn("canvasPie4", _self.player1[0].name, _self.player2[0].name, _self.player1[0].total_rebounds, _self.player2[0].total_rebounds);
					that.showColumn("canvasPie5", _self.player1[0].name, _self.player2[0].name, _self.player1[0].assists, _self.player2[0].assists);
					that.showColumn("canvasPie6", _self.player1[0].name, _self.player2[0].name, _self.player1[0].snatch, _self.player2[0].snatch);
					that.showColumn("canvasPie7", _self.player1[0].name, _self.player2[0].name, _self.player1[0].blocks, _self.player2[0].blocks);
					that.showColumn("canvasPie8", _self.player1[0].name, _self.player2[0].name, _self.player1[0].miss, _self.player2[0].miss);
					that.showColumn("canvasPie9", _self.player1[0].name, _self.player2[0].name, _self.player1[0].score, _self.player2[0].score);
					that.showColumn("canvasPie10", _self.player1[0].name, _self.player2[0].name, _self.player1[0].foul, _self.player2[0].foul); */
				}
			});
			console.log(that.player);
		},
		methods: {
			change1: function(e) {
				var that = this;
				that.player1 = [];
				that.sel1 = that.player[e.detail.value[0]].id;
				console.log(that.player[e.detail.value[0]].id);
				uni.request({
					url: "/api/player_comparison_detail/",
					method: "GET",
					data: {
						id: that.player[e.detail.value[0]].id,
					},
					success(r) {
						var eachplayer1 = {id:'', name:'', hit_percentage: 0, three_point_hit_percentage: 0, penalty_hit_percentage: 0, total_rebounds: 0, assists: 0, snatch: 0, blocks: 0, miss: 0, foul: 0, score: 0};
						eachplayer1.id = r.data.data.id;
						eachplayer1.name = r.data.data.name;
						eachplayer1.hit_percentage = r.data.data.hit_percentage;
						eachplayer1.three_point_hit_percentage = r.data.data.three_point_hit_percentage;
						eachplayer1.penalty_hit_percentage = r.data.data.penalty_hit_percentage;
						eachplayer1.total_rebounds = r.data.data.total_rebounds;
						eachplayer1.assists = r.data.data.assists;
						eachplayer1.snatch = r.data.data.snatch;
						eachplayer1.blocks = r.data.data.blocks;
						eachplayer1.miss = r.data.data.miss;
						eachplayer1.score = r.data.data.score;
						eachplayer1.foul = r.data.data.foul;
						that.player1.push(eachplayer1);
						console.log("okokoo");
						console.log(r);
						console.log("11111111");
						console.log(that.player1);
					}
				});
			},
			change2: function(e) {
				var that = this;
				that.player2 = [];
				that.sel2 = that.player[e.detail.value[0]].id
				console.log(that.player[e.detail.value[0]].id);
				uni.request({
					url: "/api/player_comparison_detail/",
					method: "GET",
					data: {
						id: that.player[e.detail.value[0]].id,
					},
					success(r) {
						var eachplayer2 = {id:'', name:'', hit_percentage: 0, three_point_hit_percentage: 0, penalty_hit_percentage: 0, total_rebounds: 0, assists: 0, snatch: 0, blocks: 0, miss: 0, foul: 0, score: 0};
						eachplayer2.id = r.data.data.id;
						eachplayer2.name = r.data.data.name;
						eachplayer2.hit_percentage = r.data.data.hit_percentage;
						eachplayer2.three_point_hit_percentage = r.data.data.three_point_hit_percentage;
						eachplayer2.penalty_hit_percentage = r.data.data.penalty_hit_percentage;
						eachplayer2.total_rebounds = r.data.data.total_rebounds;
						eachplayer2.assists = r.data.data.assists;
						eachplayer2.snatch = r.data.data.snatch;
						eachplayer2.blocks = r.data.data.blocks;
						eachplayer2.miss = r.data.data.miss;
						eachplayer2.score = r.data.data.score;
						eachplayer2.foul = r.data.data.foul;
						that.player2.push(eachplayer2);
						console.log(r);
						console.log("2222222");
						console.log(that.player2);
					}
				});
			},
			showColumn(canvasId, data1, data2, data3, data4){
				canvaPie=new uCharts({
					$this:_self,
					context: uni.createCanvasContext(canvasId, _self),
					canvasId: canvasId,
					type: 'pie',
					fontSize: 11,
					legend: true,
					background:'#FFFFFF',
					pixelRatio: 1,
					series: [{
								"name": data1,
								"data": data3,
								"textColor": "white",
								}, {
								"name": data2,
								"data": data4,
								"textColor": "white",
							}],
					animation: true,
					width: 190,
					height: 230,
					dataLabel: true,
					extra: {
						pie: {
						  lableWidth: 15
						}
					},
				});
			},
			ok: function(e) {
				console.log("compare");
				var that = this;
				that.showColumn("canvasPie1", that.player1[0].name, that.player2[0].name, that.player1[0].hit_percentage, that.player2[0].hit_percentage);
				that.showColumn("canvasPie2", that.player1[0].name, that.player2[0].name, that.player1[0].three_point_hit_percentage, that.player2[0].three_point_hit_percentage);
				that.showColumn("canvasPie3", that.player1[0].name, that.player2[0].name, that.player1[0].penalty_hit_percentage, that.player2[0].penalty_hit_percentage);
				that.showColumn("canvasPie4", that.player1[0].name, that.player2[0].name, that.player1[0].total_rebounds, that.player2[0].total_rebounds);
				that.showColumn("canvasPie5", that.player1[0].name, that.player2[0].name, that.player1[0].assists, that.player2[0].assists);
				that.showColumn("canvasPie6", that.player1[0].name, that.player2[0].name, that.player1[0].snatch, that.player2[0].snatch);
				that.showColumn("canvasPie7", that.player1[0].name, that.player2[0].name, that.player1[0].blocks, that.player2[0].blocks);
				that.showColumn("canvasPie9", that.player1[0].name, that.player2[0].name, that.player1[0].score, that.player2[0].score);
				that.showColumn("canvasPie10", that.player1[0].name, that.player2[0].name, that.player1[0].foul, that.player2[0].foul);
			}
		},
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
	/* .data_content .data_main .main_right view.right_1 .choice{
	    position: absolute;
	    top: 25px;
	    right: 30px;
	    z-index: 1000;
	}
	.data_content .data_main .main_right view.right_1 .choice label{
	    color:#fff;
	}
	.data_content .data_main .main_right view.right_2 .chart_text {
	    width: 18%;
	    color:#fff;
	    text-align: center;
	    margin-top: 12px;
	}
	.data_content .data_main .main_right view.right_2 .chart_text p{
	    margin-top: 21px;
	}
	.data_content .data_main .main_right view.right_2 .chart_text p img{
	    margin-right: 5px;
	    margin-top: -4px;
	}
	.data_content .data_main .main_right view.right_2 .chart_text p:nth-child(1){
	    font-size: 14px;
	    font-weight: 600;
	}
	.data_content .data_main .main_right view.right_2 .text_sum{
	    text-align: center;
	    color:#ffff43;
	    font-weight: 600;
	}
	.data_content .data_main .main_right view.right_2 .text_sum view:nth-child(2){
	    font-size: 18px;
	    font-weight: 600;
	} */
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
		left: 5%;
		height: 20px;
	}
	.te2{
		display: block;
		color: #fff;
		position: relative;
		float: left;
		left: 8%;
		height: 20px;
	}
	.te3{
		color: #fff;
		display: block;
		position: relative;
		float: left;
		left: 10%;
		height: 20px;
	}
	.te4{
		color: #fff;
		display: block;
		position: relative;
		float: left;
		left: 13%;
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
</style>
