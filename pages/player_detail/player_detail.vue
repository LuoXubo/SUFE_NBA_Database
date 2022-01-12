<template>
	<view class="container">
		<view class="header">
			<view class="bg_header">
			    <view class="t_title">
			        Player Stat
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
							Player Photo
						</view>
						<image :src="player_img" class="player_img"></image>
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
							Player Stat
						</view>
						<view style="display: flex; flex-direction: row;">
							<canvas canvas-id="ScoreCanva" id="ScoreCanva" style="height: 500px; width: 400px; float: left;"></canvas>
							<canvas canvas-id="OtherCanva" id="OtherCanva" style="height: 500px; width: 400px; float: right;"></canvas>
						</view>
						<button @click="to_career_detail(id)" class="to_career_button">Career Data</button>
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
							Information
						</view>
						<view style=" margin-top: 100upx; text-align: center; color: white;">
							<view style="font-size: 50upx;">{{name}}</view>
							<view style="font-size: 40upx; margin-top: 20upx;">{{number}}</view>
							<view style="font-size: 40upx; margin-top: 20upx;">{{position}}</view>
							<view style="font-size: 40upx; margin-top: 20upx;">{{height}}</view>
							<view style="font-size: 40upx; margin-top: 20upx;">{{weight}}</view>
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
					width : 380,
					height : 400
				});
				
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
		padding: 20upx;
		/* font-size: 14upx; */
		line-height: 24upx;
	}
	.to_career_button{
		width: 400upx; 
		height: 100upx; 
		font-size: 40upx; 
		border-radius: 20upx;
		background-color: #18BC37;
		margin-top: 100upx;
		color: white;
	}
	.player_img{
		width: 300upx; 
		height: 300upx; 
		margin-left: 250upx;
		margin-top: 100upx;
	}
	.player_img:hover{
		transform: scale(1.5, 1.5); 
	}
	.player_img_full{
		width: 600upx; 
		height: 600upx; 
		margin-left: 200upx; 
		border-radius: 20upx;
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
