<template>
	<!-- 排名榜单：1得分、2出场时间、3总篮板数、4投篮命中率、5三分命中率、6罚球命中率、7助攻数、8抢断数、9盖帽数、10失误数、11犯规数
		（只根据本赛季排名）-->
	<view class="rank">
		<h1>Ranking List</h1>
		<!-- 榜单列表 -->
		<view class="big-index-1">
			<ul>
				<li>
					<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
					<strong @click="score">score</strong>
				</li>
				<li>
					<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
					<strong @click="time">number of time</strong>
				</li>
				<li>
					<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
					<strong @click="total_rebounds">rebounds</strong>
				</li>
				<li>
		            <b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
		            <strong @click="hit_percentage">shooting percentage</strong>
		        </li>
		        <li>
		            <b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
		            <strong @click="three_point_hit_percentage">three point hit rate</strong>
		        </li>
		        <li>
		            <b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
		            <strong @click="penalty_hit_percentage">free throw percentage</strong>
		        </li>
			</ul>
		</view>
		<view class="big-index-1">
		    <ul>
		        <li>
		            <b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
		            <strong @click="assists">number of assists</strong>
		        </li>
			    <li>
			        <b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
			        <strong @click="snatch">number of steal</strong>
			    </li>
			    <li>
			        <b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
			        <strong @click="blocks">number of caps</strong>
			    </li>
			    <li>
			        <b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
			        <strong @click="miss">number of errors</strong>
			    </li>
			    <li>
			        <b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
			        <strong @click="foul">number of fouls</strong>
			    </li>
			</ul>
		</view>
		<!-- 中间 -->
		<view class="center-area">
		    <view class="pandect-area">
		        <h3>
		            <p>SCORE</p>
		            <strong>CHART</strong>
		            <em>Histogram</em>
		        </h3>
		        <span class="pandect-area-left">
		            <b></b>
		        </span>
		        <view class="pandect-area-center">
					<canvas canvas-id="canvasColumn" id="canvasColumn" class="charts"></canvas>
		        </view>
		        <span class="pandect-area-right">
		            <b></b>
		        </span>
		    </view>
		    <view class="details1-area">
		        <span class="details1-area-left"></span>
		        <view class="details1-area-center">
		        <dl>
		            <dt @click="goto(player[0].id)">No.1 {{player[0].name}}</dt>
		            <dd>
		                {{player[0].uniform_number}}
		            </dd>
					<img :src="player[0].img" class="pic"/>	
					
		            <dt @click="goto(player[1].id)">No.2 {{player[1].name}}</dt>
		            <dd>
		                {{player[1].uniform_number}}
		            </dd>
					<img :src="player[1].img" class="pic"/>
					
		            <dt @click="goto(player[2].id)">No.3 {{player[2].name}} </dt>
		            <dd>
		                {{player[2].uniform_number}}
		            </dd>
					<img :src="player[2].img" class="pic"/>
					
					<dt @click="goto(player[3].id)">No.4 {{player[3].name}} </dt>
					<dd>
					    {{player[3].uniform_number}}
					</dd>
					<img :src="player[3].img" class="pic"/>
					
					<dt @click="goto(player[4].id)">No.5 {{player[4].name}} </dt>
					<dd>
					    {{player[4].uniform_number}}
					</dd>
					<img :src="player[4].img" class="pic"/>
		        </dl>
		        <b></b>
		        </view>
		        <span class="details1-area-right"></span>
		
		    </view>
		    <view class="details2-area">
		        <span class="details2-area-left"></span>
		        <view class="details2-area-center">
		            <dl>
		                <dt @click="goto(player[5].id)">No.6 {{player[5].name}}</dt>
		                <dd>
		                    {{player[5].uniform_number}}
		                </dd>
						<img :src="player[5].img" class="pic"/>
						
		                <dt @click="goto(player[6].id)">No.7 {{player[6].name}}</dt>
		                <dd>
		                    {{player[6].uniform_number}}
		                </dd>
						<img :src="player[6].img" class="pic"/>
						
		                <dt @click="goto(player[7].id)">No.8 {{player[7].name}} </dt>
		                <dd>
		                    {{player[7].uniform_number}}
		                </dd>
						<img :src="player[7].img" class="pic"/>
						
						<dt @click="goto(player[8].id)">No.9 {{player[8].name}} </dt>
						<dd>
						    {{player[8].uniform_number}}
						</dd>
						<img :src="player[8].img" class="pic"/>
						
						<dt @click="goto(player[9].id)">No.10 {{player[9].name}} </dt>
						<dd>
						    {{player[9].uniform_number}}
						</dd>
						<img :src="player[9].img" class="pic"/>
		            </dl>
		            <b></b>
		        </view>
		        <span class="details2-area-right"></span>
		    </view>
		</view>
	</view>
</template>

<script>
	import uCharts from '../../components/u-charts/u-charts.js';
	var _self;
	var canvaColumn = null;
	export default {
		data() {
			return {
				current: 1,
				player: [
					{
						img: 'https://cdn.nba.com/headshots/nba/latest/1040x760/201939.png',
						number: 30,
						uniform_number: 1,
						name: 'Stephen Curry',
						id: 1
					},
					{
						img: 'https://cdn.nba.com/headshots/nba/latest/1040x760/203110.png',
						number: 23,
						uniform_number: 1,
						name: 'Draymond Green',
						id: 2
					},
					{
						img: 'https://cdn.nba.com/headshots/nba/latest/1040x760/202691.png',
						number: 11,
						uniform_number: 1,
						name: 'Klay Thompson',
						id: 3
					},
					{
						img: 'https://cdn.nba.com/headshots/nba/latest/1040x760/201939.png',
						number: 30,
						uniform_number: 1,
						name: 'Stephen Curry',
						id: 4
					},
					{
						img: 'https://cdn.nba.com/headshots/nba/latest/1040x760/201939.png',
						number: 30,
						uniform_number: 1,
						name: 'Stephen Curry',
						id: 5
					},
					{
						img: 'https://cdn.nba.com/headshots/nba/latest/1040x760/201939.png',
						number: 30,
						uniform_number: 1,
						name: 'Stephen Curry',
						id: 6
					},
					{
						img: 'https://cdn.nba.com/headshots/nba/latest/1040x760/201939.png',
						number: 30,
						uniform_number: 1,
						name: 'Stephen Curry',
						id: 7
					},
					{
						img: 'https://cdn.nba.com/headshots/nba/latest/1040x760/201939.png',
						number: 30,
						uniform_number: 1,
						name: 'Stephen Curry',
						id: 8
					},
					{
						img: 'https://cdn.nba.com/headshots/nba/latest/1040x760/201939.png',
						number: 30,
						uniform_number: 1,
						name: 'Stephen Curry',
						id: 9
					},
					{
						img: 'https://cdn.nba.com/headshots/nba/latest/1040x760/201939.png',
						number: 30,
						uniform_number: 1,
						name: 'Stephen Curry',
						id: 10
					},
				],
				cWidth: '',
				cHeight: '',
				pixelRatio: 1,
			}
		},
		onLoad:function(r){
			_self = this;
			this.cWidth = uni.upx2px(750);
			this.cHeight = uni.upx2px(375);
			this.showColumn("canvasColumn");
			uni.request({
				url: "/api/rank/",
				method: "GET",
				data: {
					type: "score",
				},
				success(r) {
					console.log("yes");
					for (var i = 0; i < 10; i++) {
						var eachplayer = {id:'', img:'', name:'', number:'', uniform_number:''};
						eachplayer.id = r.data[i].id;
						eachplayer.img = r.data[i].photo;
						eachplayer.name = r.data[i].name;
						eachplayer.uniform_number = r.data[i].uniform_number;
						eachplayer.number = r.data[i].score;
						that.player.push(eachplayer);
					}
					console.log(r);
				}
			})
		},
		methods: {
			async showColumn(canvasId){
				var that = this;
				var name = "";
				if (that.current == 1) { name = "score";}
				if (that.current == 2) { name = "number of time";}
				if (that.current == 3) { name = "rebounds"}
				if (that.current == 4) { name = "shooting percentage";}
				if (that.current == 5) { name = "three point hit rate";}
				if (that.current == 6) { name = "free throw percentage";}
				if (that.current == 7) { name = "number of assists";}
				if (that.current == 8) { name = "number of steal";}
				if (that.current == 9) { name = "number of caps";}
				if (that.current == 10) { name = "number of errors";}
				if (that.current == 11) { name = "number of fouls";}
				console.log(name);
				canvaColumn = new uCharts({
					context: uni.createCanvasContext("canvasColumn", _self),
					$this: _self,
					canvasId: "canvasColumn",
					type: 'column',
					legend: true,
					fontSize: 11,
					background: '#ffffff',
					pixelRatio: _self.pixelRatio,
					animation: true,
					categories: ["No.1", "No.2", "No.3", "No.4", "No.5", "No.6","No.7","No.8","No.9","No.10"],
					series: [{
						"name": name,
						"color": "#0067e6",
						"textColor": "white",
						"data": [_self.player[0].number,
								_self.player[1].number,
								_self.player[2].number,
								_self.player[3].number,
								_self.player[4].number,
								_self.player[5].number,
								_self.player[6].number,
								_self.player[7].number,
								_self.player[8].number,
								_self.player[9].number]
					}],
					xAxis: {
						disableGrid:true,
					},
					yAxis: {
						data: [{
							min: 0,
							max: Math.max(_self.player[0].number,
							_self.player[1].number,
							_self.player[2].number,
							_self.player[3].number,
							_self.player[4].number,
							_self.player[5].number,
							_self.player[6].number,
							_self.player[7].number,
							_self.player[8].number,
							_self.player[9].number) + 2,
						}]
					},
					dataLabel: true,
					width: 650,
					height: 210,
					extra: {
						column: {
							type: 'group',
							width:  _self.cWidth*_self.pixelRatio*0.45/20
						}
					}
				});
			},
			score: function(r) {
				var that = this;
				that.current = 1;
				that.player = [];
				uni.request({
					url: "http://127.0.0.1:8000/api/rank/",
					method: "GET",
					data: {
						type: "score",
					},
					success(r) {
						for (var i = 0; i < 10; i++) {
							var eachplayer = {id:'', img:'', name:'', number:'', uniform_number:''};
							eachplayer.id = r.data[i].id;
							eachplayer.img = r.data[i].photo;
							eachplayer.name = r.data[i].name;
							eachplayer.uniform_number = r.data[i].uniform_number;
							eachplayer.number = r.data[i].score;
							that.player.push(eachplayer);
						}
						console.log(r);
					}
				});
				that.showColumn("canvasColumn");
			},
			time: function(r) {
				var that = this;
				that.current = 2;
				that.player = [];
				uni.request({
					url: "http://127.0.0.1:8000/api/rank/",
					method: "GET",
					data: {
						type: "time",
					},
					success(r) {
						for (var i = 0; i < 10; i++) {
							var eachplayer = {id:'', img:'', name:'', number:'', uniform_number:''};
							eachplayer.id = r.data[i].id;
							eachplayer.img = r.data[i].photo;
							eachplayer.name = r.data[i].name;
							eachplayer.uniform_number = r.data[i].uniform_number;
							eachplayer.number = r.data[i].time;
							that.player.push(eachplayer);
						}
						console.log(r);
					}
				});
				that.showColumn("canvasColumn");
			},
			total_rebounds: function(r) {
				var that = this;
				that.current = 3;
				that.player = [];
				uni.request({
					url: "http://127.0.0.1:8000/api/rank/",
					method: "GET",
					data: {
						type: "total_rebounds",
					},
					success(r) {
						for (var i = 0; i < 10; i++) {
							var eachplayer = {id:'', img:'', name:'', number:'', uniform_number:''};
							eachplayer.id = r.data[i].id;
							eachplayer.img = r.data[i].photo;
							eachplayer.name = r.data[i].name;
							eachplayer.uniform_number = r.data[i].uniform_number;
							eachplayer.number = r.data[i].total_rebounds;
							that.player.push(eachplayer);
						}
						console.log(r);
					}
				});
				that.showColumn("canvasColumn");
			},
			hit_percentage: function(r) {
				var that = this;
				that.current = 4;
				that.player = [];
				uni.request({
					url: "http://127.0.0.1:8000/api/rank/",
					method: "GET",
					data: {
						type: "hit_percentage",
					},
					success(r) {
						for (var i = 0; i < 10; i++) {
							var eachplayer = {id:'', img:'', name:'', number:'', uniform_number:''};
							eachplayer.id = r.data[i].id;
							eachplayer.img = r.data[i].photo;
							eachplayer.name = r.data[i].name;
							eachplayer.uniform_number = r.data[i].uniform_number;
							eachplayer.number = r.data[i].hit_percentage;
							that.player.push(eachplayer);
						}
						console.log(r);
					}
				});
				that.showColumn("canvasColumn");
			},
			three_point_hit_percentage: function(r) {
				var that = this;
				that.current = 5;
				that.player = [];
				uni.request({
					url: "http://127.0.0.1:8000/api/rank/",
					method: "GET",
					data: {
						type: "three_point_hit_percentage",
					},
					success(r) {
						for (var i = 0; i < 10; i++) {
							var eachplayer = {id:'', img:'', name:'', number:'', uniform_number:''};
							eachplayer.id = r.data[i].id;
							eachplayer.img = r.data[i].photo;
							eachplayer.name = r.data[i].name;
							eachplayer.uniform_number = r.data[i].uniform_number;
							eachplayer.number = r.data[i].three_point_hit_percentage;
							that.player.push(eachplayer);
						}
						console.log(r);
					}
				});
				that.showColumn("canvasColumn");
			},
			penalty_hit_percentage: function(r) {
				var that = this;
				that.current = 6;
				that.player = [];
				uni.request({
					url: "http://127.0.0.1:8000/api/rank/",
					method: "GET",
					data: {
						type: "penalty_hit_percentage",
					},
					success(r) {
						for (var i = 0; i < 10; i++) {
							var eachplayer = {id:'', img:'', name:'', number:'', uniform_number:''};
							eachplayer.id = r.data[i].id;
							eachplayer.img = r.data[i].photo;
							eachplayer.name = r.data[i].name;
							eachplayer.uniform_number = r.data[i].uniform_number;
							eachplayer.number = r.data[i].penalty_hit_percentage;
							that.player.push(eachplayer);
						}
						console.log(r);
					}
				});
				that.showColumn("canvasColumn");
			},
			assists: function(r) {
				var that = this;
				that.current = 7;
				that.player = [];
				uni.request({
					url: "http://127.0.0.1:8000/api/rank/",
					method: "GET",
					data: {
						type: "assists",
					},
					success(r) {
						for (var i = 0; i < 10; i++) {
							var eachplayer = {id:'', img:'', name:'', number:'', uniform_number:''};
							eachplayer.id = r.data[i].id;
							eachplayer.img = r.data[i].photo;
							eachplayer.name = r.data[i].name;
							eachplayer.uniform_number = r.data[i].uniform_number;
							eachplayer.number = r.data[i].assists;
							that.player.push(eachplayer);
						}
						console.log(r);
					}
				});
				that.showColumn("canvasColumn");
			},
			snatch: function(r) {
				var that = this;
				that.current = 8;
				that.player = [];
				uni.request({
					url: "http://127.0.0.1:8000/api/rank/",
					method: "GET",
					data: {
						type: "snatch",
					},
					success(r) {
						for (var i = 0; i < 10; i++) {
							var eachplayer = {id:'', img:'', name:'', number:'', uniform_number:''};
							eachplayer.id = r.data[i].id;
							eachplayer.img = r.data[i].photo;
							eachplayer.name = r.data[i].name;
							eachplayer.uniform_number = r.data[i].uniform_number;
							eachplayer.number = r.data[i].snatch;
							that.player.push(eachplayer);
						}
						console.log(r);
					}
				});
				that.showColumn("canvasColumn");
			},
			blocks: function(r) {
				var that = this;
				that.current = 9;
				that.player = [];
				uni.request({
					url: "http://127.0.0.1:8000/api/rank/",
					method: "GET",
					data: {
						type: "blocks",
					},
					success(r) {
						for (var i = 0; i < 10; i++) {
							var eachplayer = {id:'', img:'', name:'', number:'', uniform_number:''};
							eachplayer.id = r.data[i].id;
							eachplayer.img = r.data[i].photo;
							eachplayer.name = r.data[i].name;
							eachplayer.uniform_number = r.data[i].uniform_number;
							eachplayer.number = r.data[i].blocks;
							that.player.push(eachplayer);
						}
						console.log(r);
					}
				});
				that.showColumn("canvasColumn");
			},
			miss: function(r) {
				var that = this;
				that.current = 10;
				that.player = [];
				uni.request({
					url: "http://127.0.0.1:8000/api/rank/",
					method: "GET",
					data: {
						type: "miss",
					},
					success(r) {
						for (var i = 0; i < 10; i++) {
							var eachplayer = {id:'', img:'', name:'', number:'', uniform_number:''};
							eachplayer.id = r.data[i].id;
							eachplayer.img = r.data[i].photo;
							eachplayer.name = r.data[i].name;
							eachplayer.uniform_number = r.data[i].uniform_number;
							eachplayer.number = r.data[i].miss;
							that.player.push(eachplayer);
						}
						console.log(r);
					}
				});
				that.showColumn("canvasColumn");
			},
			foul: function(r) {
				var that = this;
				that.current = 11;
				that.player = [];
				uni.request({
					url: "http://127.0.0.1:8000/api/rank/",
					method: "GET",
					data: {
						type: "foul",
					},
					success(r) {
						for (var i = 0; i < 10; i++) {
							var eachplayer = {id:'', img:'', name:'', number:'', uniform_number:''};
							eachplayer.id = r.data[i].id;
							eachplayer.img = r.data[i].photo;
							eachplayer.name = r.data[i].name;
							eachplayer.uniform_number = r.data[i].uniform_number;
							eachplayer.number = r.data[i].foul;
							that.player.push(eachplayer);
						}
						console.log(r);
					}
				});
				that.showColumn("canvasColumn");
			},
			goto: function(id) {
				var iid = id;
				uni.navigateTo({
					url: "../player_detail/player_detail?id=" + iid,
				})
			}
		}
	}
</script>

<style>
	page{
		background: #000; 
		height: 100%; 
		color:#fff;
		font-family: "microsoft yahei", simhei; 
		moz-user-select: -moz-none; 
		moz-user-select: none;  
		-o-user-select:none;  
		-khtml-user-select:none;  
		-webkit-user-select:none; 
		-ms-user-select:none; 
		user-select:none;
		overflow-x: hidden; 
		-webkit-animation:fadeIn 1s .2s ease both;  
		-moz-animation:fadeIn 1s .2s ease both;
	}
	@-webkit-keyframes fadeIn{ 0%{opacity:0; } 100%{opacity:1;} }
	.rank{
		float: left; 
		width:100%; 
		height: 100%;  
		background: url("../../static/bg01warp.png") 50% 50% no-repeat; 
		background-size: 100%;
	}
	h1 { 
		font-family: "microsoft yahei"; 
		font-size: 20px; 
		color: #fff;
		text-align: center;  
		padding: 12px 0 16px 0; 
		display: block; 
		background: url("../../static/bg01top.png") center bottom no-repeat;
		-webkit-animation:fadeInDownBig .8s .2s ease both;
		-moz-animation:fadeInDownBig .8s .2s ease both;
	}
	@-webkit-keyframes fadeInDownBig{
		0%{opacity:0; -webkit-transform:translateY(-2000px)}
		100%{opacity:1; -webkit-transform:translateY(0)}
	}
	@-moz-keyframes fadeInDownBig{
		0%{opacity:0; -moz-transform:translateY(-2000px)}
		100%{opacity:1; -moz-transform:translateY(0)}
	}
	.big-index-1 { 
		position: relative;
		left: 267px; 
		top: 20px; 
		line-height: 1; 
		min-width: 818px; 
		height:55px; 
		overflow: hidden;
	}
	.big-index-1 li {
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
	.big-index-1 li strong { 
		display: block; 
		color: #fff;
		font-family:'electronicFont'; 
		font-size: 22px; 
		font-weight: normal;
	}
	@font-face { font-family:'electronicFont'; src: url("../../static/font/DS-DIGI.TTF"); }
	.big-index-1 li .animation-1 {
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
	.big-index-1 li .animation-2 {
		position: absolute; 
		right:0; 
		top:1px; 
		height: 16px;  
		width: 15px; 
		background: url(../../static/bg02bigindex.png) 0 0 no-repeat;
	}
	.big-index-1 li .animation-3 {
		position: absolute; 
		right:-1px; 
		bottom:-1px; 
		height: 4px;  
		width: 4px; 
		background: url(../../static/bg03bigindex.png) 50% 50% no-repeat;
	}
	.big-index-1 li:hover .animation-2 { 
		background: url(../../static/bg02bigindex_.png) 0 0 no-repeat;
	}
	.big-index-1 li:hover .animation-3 {  
		background: url(../../static/bg03bigindex_.png) 50% 50% no-repeat;
	}
	.big-index-1 li:hover .animation-1 {
		-webkit-animation-iteration-count: infinite;   
		-webkit-animation-name:bounceInRight1 ; 
		-webkit-animation-duration:4000ms;
	}
	.big-index-1 li:hover .animation-2, .big-index-1 li:hover .animation-3{ 
		-webkit-animation:flash .2s .2s ease both; 
		-moz-animation:flash .2s .2s ease both;
	}
	@media screen and (max-width: 1366px) {
	   .big-index-1 li:nth-child(6) { display: none;}
	   .big-index-1 li { margin-right: 6px;}
	}
	@-webkit-keyframes bounceInLeft1{
	    0%{-webkit-transform:translateX(-115px)}
	    100%{-webkit-transform:translateX(0)}
	}
	@-webkit-keyframes bounceInRight1{
	    0%{-webkit-transform:translateX(0)}
	    100%{-webkit-transform:translateX(-115px)}
	}
	.big-index-1{
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
	.center-area { 
		margin: 50px 350px 0 300px ;
		position: relative; 
	}
	.charts{
		margin: auto;
		top: 20px;
		width: 700px;
		height: 220px;
	}
	.pandect-area {
		background: url(../../static/bg02pandect.png) center top no-repeat; 
		height: 292px; 
		margin: 0 68px; 
		position: relative;
	}
	.pandect-area .pandect-area-left {
		position: absolute; 
		left:-68px; 
		top: 0; 
		display: block; 
		width: 68px; 
		height: 292px; 
		background: url(../../static/bg01pandect.png) center top no-repeat;
	}
	.pandect-area .pandect-area-right { 
		position: absolute; 
		right:-68px; 
		top: 0; 
		display: block; 
		width:68px; 
		height: 292px; 
		background: url(../../static/bg03pandect.png) center top no-repeat;
	}
	
	.pandect-area .pandect-area-left b { 
		-webkit-animation-iteration-count: infinite;  
		-webkit-animation-name:flash1 ; 
		-webkit-animation-duration:.2ms; 
		position: absolute; 
		left:-5px; 
		top: -5px; 
		display: block; 
		width:16px; 
		height: 22px; 
		background: url(../../static/bg04pandect.png) center top no-repeat;
	}
	.pandect-area .pandect-area-right b { 
		-webkit-animation-iteration-count: infinite;
		-webkit-animation-name:flash1 ; 
		-webkit-animation-duration:.2ms;
		position: absolute; 
		right:-7px; 
		top:-5px; 
		display: block; 
		width:16px; 
		height: 22px; 
		background: url(../../static/bg05pandect.png) center top no-repeat;
	}
	
	.pandect-area h3 { 
		font-weight: normal; 
		text-align: center; 
		position: relative; 
		top:10px;  
		z-index: 1; 
		border-bottom: 1px solid #666; 
		margin:0 -55px;
	}
	.pandect-area h3 p { 
		position: absolute; 
		left: 0; 
		top: 0; 
		background: #000;
		font-family:'electronicFont'; 
		color: rgba(255,255,255,.8)
	}
	.pandect-area h3 p sub { 
		display: block; 
		color: rgba(255,255,255,.3)
	}
	.pandect-area h3 strong { 
		border:1px solid #ababab; 
		padding: 1px 14px; 
		line-height: 1; 
		position: relative; 
		bottom: -8px; 
		z-index: 1; 
		background: #000;
	}
	.pandect-area h3 em { 
		position: absolute; 
		right: 0; 
		top: 0;
		font-family:'electronicFont'; 
		font-size: 14px; 
		color: #ff3114;
	}
	.pandect-area-center { 
		margin-top: 20px; 
		overflow: hidden;
	}
	
	.details1-area { 
		position: absolute; 
		left:10px; 
		margin-top: 15px; 
		text-align: center; 
		height: 220px; 
	}
	.details1-area-left { 
		display: block; 
		width: 122px; 
		height: 220px; 
		position: absolute; 
		left: -122px; 
		top: 0;  
		background: url(../../static/bg01details03.png) center bottom no-repeat; 
	}
	.details1-area-right {
		display: block; 
		width: 121px; 
		height: 220px; 
		position: absolute; 
		right: -121px; 
		top: 0;  
		background: url(../../static/bg01details05.png) center bottom no-repeat; 
	}
	.details1-area-center { 
		height: 220px; 
		float: left; 
		background: url(../../static/bg01details04.png) center bottom repeat-x;
	}
	
	.details2-area { 
		position: absolute; 
		right:10px; 
		margin-top: 15px;  
		height: 220px; 
		text-align: center;
	}
	.details2-area h3, .details2-area dl { 
		margin-left: 40px!important;
	}
	.details2-area-left { 
		display: block; 
		width: 122px; 
		height: 220px;
		position: absolute; 
		left: -122px; 
		top: 0;  
		background: url(../../static/bg01details01.png) center bottom no-repeat; 
	}
	.details2-area-right {
		display: block; 
		width: 121px; 
		height: 220px; 
		position: absolute; 
		right: -121px; 
		top: 0;  
		background: url(../../static/bg01details02.png) center bottom no-repeat; 
	}
	.details2-area-center { 
		height: 220px; 
		float: left; 
		background: url(../../static/bg01details06.png) center bottom repeat-x;
	}
	@media screen and (max-width: 1600px) {
	    .details1-area-center { width: 390px;}
	    .details2-area-center { width: 390px;}
	}
	
	@media screen and (max-width: 1366px) {
	    .details1-area-center { width: auto;}
	    .details2-area-center { width: auto;}
	}
	
	.details1-area b, .details2-area b { 
		position: absolute;  
		left:0; 
		bottom:12px; 
		display:block; 
		width:100%; 
		height: 55px; 
		background: url(../../static/bg03details.png) center top no-repeat; 
		background-size:100%; 
	}
	.details1-area h3, .details2-area h3 { 
		text-align: left; 
		margin-top: 15px; 
		font-size: 14px;
	}
	.details1-area b, .details2-area b {
		-webkit-animation: bounce-up1 5s linear infinite; 
		animation: bounce-up1 5s linear infinite;
	}
	.details1-area dl, .details2-area dl { margin:40px 0 0 40px;}
	.details2-area dl {margin-left: 0px;}
	.details1-area dl dt, .details2-area dl dt { 
		float: left; 
		clear: left; 
		width: 200px; 
		text-align: center; 
		margin: 6px 0;
		font-size: 10px;
	}
	.pic{
		display: flex;
		border-radius: 50%;
		margin: 6px 0;
		height: 30px;
		width: 30px;
	}
	.pic:hover{
		height: 70px;
		width: 70px;
	}
	.details1-area dl dd, .details2-area dl dd { 
		width: 20px;
		float: left;
		margin: 6px 0; 
		font-family:'electronicFont'; 
		font-size: 14px;
	}
	@keyframes bounce-up1 {
	    25% {
	        transform: translateY(5px);
	    }
	    50%, 100% {
	        transform: translateY(0);
	    }
	    75% {
	        transform: translateY(-5px);
	    }
	}
	@-webkit-keyframes bounce-up1 {
	    25% {
	        -webkit-transform: translateY(5px);
	    }
	    50%, 100% {
	        -webkit-transform: translateY(0);
	    }
	    75% {
	        -webkit-transform: translateY(-5px);
	    }
	}
	
	.details1-area, .details2-area, .pandect-area{
	    -webkit-animation:fadeInUp 1s 1s ease both;
	    -moz-animation:fadeInUp 1s 1s ease both;
	}
	@-webkit-keyframes fadeInUp{
	    0%{opacity:0; -webkit-transform:translateY(20px)}
	    100%{opacity:1; -webkit-transform:translateY(0)}
	}
	
	
</style>
