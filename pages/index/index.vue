<template>
	<view class="container">
		<view class="header">
			<view class="bg_header">
			    <view class="t_title">
			        Player Stat
			    </view> 
			</view>
		</view>
		<view class="topindex">
			<view style="display: flex; flex-direction: row;">
				<view style="font-size: 50upx; color: #007AFF; margin-left: 20%;">Home</view>
				<view style="font-size: 50upx; color: #ff00ff; margin-left: 20%;" @tap="to_leaderboard">Leaderboard</view>
				<view style="font-size: 50upx; color: #ff00ff; margin-left: 20%;" @tap="to_comparison">Player Comparison</view>
			</view>
		</view>
		
		<view class="big-index-1">
			<ul>
				<image :src="teams[0].photo" class="team-img1" @tap="to_team_detail(teams[0].id)"></image>
				<image :src="teams[1].photo" class="team-img2" @tap="to_team_detail(teams[1].id)"></image>
				<image :src="teams[2].photo" class="team-img3" @tap="to_team_detail(teams[2].id)"></image>
				<image :src="teams[3].photo" class="team-img4" @tap="to_team_detail(teams[3].id)"></image>
				<image :src="teams[4].photo" class="team-img5" @tap="to_team_detail(teams[4].id)"></image>
				<image :src="teams[5].photo" class="team-img6" @tap="to_team_detail(teams[5].id)"></image>
				</br>
				<li @tap="to_team_detail(teams[0].id)">
					<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
					<strong>{{teams[0].name_e}}</strong>
				</li>
				<li @tap="to_team_detail(teams[1].id)">
					<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
					<strong>{{teams[1].name_e}}</strong>
				</li>
				<li @tap="to_team_detail(teams[2].id)">
					<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
					<strong>{{teams[2].name_e}}</strong>
				</li>
				<li @tap="to_team_detail(teams[3].id)">
		            <b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
		            <strong>{{teams[3].name_e}}</strong>
		        </li>
		        <li @tap="to_team_detail(teams[4].id)">
		            <b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
		            <strong>{{teams[4].name_e}}</strong>
		        </li>
		        <li @tap="to_team_detail(teams[5].id)">
		            <b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
		            <strong>{{teams[5].name_e}}</strong>
		        </li>
			</ul>
		</view>
		<view class="big-index-1">
			<ul>
				<image :src="teams[6].photo" class="team-img1" @tap="to_team_detail(teams[6].id)"></image>
				<image :src="teams[7].photo" class="team-img2" @tap="to_team_detail(teams[7].id)"></image>
				<image :src="teams[8].photo" class="team-img3" @tap="to_team_detail(teams[8].id)"></image>
				<image :src="teams[9].photo" class="team-img4" @tap="to_team_detail(teams[9].id)"></image>
				<image :src="teams[10].photo" class="team-img5" @tap="to_team_detail(teams[10].id)"></image>
				<image :src="teams[11].photo" class="team-img6" @tap="to_team_detail(teams[11].id)"></image>
				</br>
				<li @tap="to_team_detail(teams[6].id)">
					<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
					<strong>{{teams[6].name_e}}</strong>
				</li>
				<li @tap="to_team_detail(teams[7].id)">
					<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
					<strong>{{teams[7].name_e}}</strong>
				</li>
				<li @tap="to_team_detail(teams[8].id)">
					<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
					<strong>{{teams[8].name_e}}</strong>
				</li>
				<li @tap="to_team_detail(teams[9].id)">
		            <b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
		            <strong>{{teams[9].name_e}}</strong>
		        </li>
		        <li @tap="to_team_detail(teams[10].id)">
		            <b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
		            <strong>{{teams[10].name_e}}</strong>
		        </li>
		        <li @tap="to_team_detail(teams[11].id)">
		            <b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
		            <strong>{{teams[11].name_e}}</strong>
		        </li>
			</ul>
		</view>
		<view class="big-index-1">
			<ul>
				<image :src="teams[12].photo" class="team-img1" @tap="to_team_detail(teams[12].id)"></image>
				<image :src="teams[13].photo" class="team-img2" @tap="to_team_detail(teams[13].id)"></image>
				<image :src="teams[14].photo" class="team-img3" @tap="to_team_detail(teams[14].id)"></image>
				<image :src="teams[15].photo" class="team-img4" @tap="to_team_detail(teams[15].id)"></image>
				<image :src="teams[16].photo" class="team-img5" @tap="to_team_detail(teams[16].id)"></image>
				<image :src="teams[17].photo" class="team-img6" @tap="to_team_detail(teams[17].id)"></image>
				</br>
				<li @tap="to_team_detail(teams[12].id)">
					<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
					<strong>{{teams[12].name_e}}</strong>
				</li>
				<li @tap="to_team_detail(teams[13].id)">
					<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
					<strong>{{teams[13].name_e}}</strong>
				</li>
				<li @tap="to_team_detail(teams[14].id)">
					<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
					<strong>{{teams[14].name_e}}</strong>
				</li>
				<li @tap="to_team_detail(teams[15].id)">
		            <b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
		            <strong>{{teams[15].name_e}}</strong>
		        </li>
		        <li @tap="to_team_detail(teams[16].id)">
		            <b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
		            <strong>{{teams[16].name_e}}</strong>
		        </li>
		        <li @tap="to_team_detail(teams[17].id)">
		            <b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
		            <strong>{{teams[17].name_e}}</strong>
		        </li>
			</ul>
		</view>
		<view class="big-index-1">
			<ul>
				<image :src="teams[18].photo" class="team-img1" @tap="to_team_detail(teams[18].id)"></image>
				<image :src="teams[19].photo" class="team-img2" @tap="to_team_detail(teams[19].id)"></image>
				<image :src="teams[20].photo" class="team-img3" @tap="to_team_detail(teams[20].id)"></image>
				<image :src="teams[21].photo" class="team-img4" @tap="to_team_detail(teams[21].id)"></image>
				<image :src="teams[22].photo" class="team-img5" @tap="to_team_detail(teams[22].id)"></image>
				<image :src="teams[23].photo" class="team-img6" @tap="to_team_detail(teams[23].id)"></image>
				</br>
				<li @tap="to_team_detail(teams[18].id)">
					<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
					<strong>{{teams[18].name_e}}</strong>
				</li>
				<li @tap="to_team_detail(teams[19].id)">
					<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
					<strong>{{teams[19].name_e}}</strong>
				</li>
				<li @tap="to_team_detail(teams[20].id)">
					<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
					<strong>{{teams[20].name_e}}</strong>
				</li>
				<li @tap="to_team_detail(teams[21].id)">
		            <b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
		            <strong>{{teams[21].name_e}}</strong>
		        </li>
		        <li @tap="to_team_detail(teams[22].id)">
		            <b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
		            <strong>{{teams[22].name_e}}</strong>
		        </li>
		        <li @tap="to_team_detail(teams[23].id)">
		            <b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
		            <strong>{{teams[23].name_e}}</strong>
		        </li>
			</ul>
		</view>
		<view class="big-index-1">
			<ul>
				<image :src="teams[24].photo" class="team-img1" @tap="to_team_detail(teams[24].id)"></image>
				<image :src="teams[25].photo" class="team-img2" @tap="to_team_detail(teams[25].id)"></image>
				<image :src="teams[26].photo" class="team-img3" @tap="to_team_detail(teams[26].id)"></image>
				<image :src="teams[27].photo" class="team-img4" @tap="to_team_detail(teams[27].id)"></image>
				<image :src="teams[28].photo" class="team-img5" @tap="to_team_detail(teams[28].id)"></image>
				<image :src="teams[29].photo" class="team-img6" @tap="to_team_detail(teams[29].id)"></image>
				</br>
				<li @tap="to_team_detail(teams[24].id)">
					<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
					<strong>{{teams[24].name_e}}</strong>
				</li>
				<li @tap="to_team_detail(teams[25].id)">
					<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
					<strong>{{teams[25].name_e}}</strong>
				</li>
				<li @tap="to_team_detail(teams[26].id)">
					<b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
					<strong>{{teams[26].name_e}}</strong>
				</li>
				<li @tap="to_team_detail(teams[27].id)">
		            <b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
		            <strong>{{teams[27].name_e}}</strong>
		        </li>
		        <li @tap="to_team_detail(teams[28].id)">
		            <b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
		            <strong>{{teams[28].name_e}}</strong>
		        </li>
		        <li @tap="to_team_detail(teams[29].id)">
		            <b class="animation-1"></b><b class="animation-2"></b><b class="animation-3"></b>
		            <strong>{{teams[29].name_e}}</strong>
		        </li>
			</ul>
		</view>
	</view>
	
</template>

<script>
	export default {
		data() {
			return {
				teams : []
			}
		},
		onLoad () {
			var that = this;
			uni.request({
				url: "/api/team",
				//url: 'http://121.4.230.11:8002/api/team/',
				method: 'GET',
				data: {},
				success(r) {
					console.log(r.data);
					console.log("======");
					console.log(r);
					for (var i = 0; i < 30; i++) {
						var eachteam = {id:'', photo:'', name_e:''};
						eachteam.id = r.data.data[i].id;
						eachteam.photo = r.data.data[i].photo;
						eachteam.name_e = r.data.data[i].name_e;
						that.teams.push(eachteam);
					}
					
					// this.teams = res.data;
				},
				fail: () => {},
				complete: () => {}
			});
		},
		methods: {	
			to_team_detail(id){
				var iid = id;
				uni.navigateTo({
					url:'../team_detail/team_detail?team_id=' + iid,
					fail(e) {
						console.log(e)
					}
				})
			},
			to_leaderboard(e) {
				uni.navigateTo({
					url: "../ranking_list/rankinglist",
					fail(e) {
						console.log(e)
					}
				})
			},
			to_comparison(e) {
				uni.navigateTo({
					url: "../compare/compare",
					fail(e) {
						console.log(e)
					}
				})
			},
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
	.container {
		/* padding: 20upx; */
		/* font-size: 14upx; */
		line-height: 24upx;
		height: 100%;
		width: 100%;
		background: url("../../static/bg01warp.png") 50% 50% no-repeat; 
		background-size: 100% 100%;
	}
	.team-img{
		width: 100upx;
		height: 100upx;
	}
	.team-img:hover{
		width: 200upx;
		height: 200upx;
	}
	.display-flex{
		display: flex;
	}
	.team{
		background-color: #fff;
		display: block;
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
	.big-index-1 {
		position: relative;
		left: 15%;  
		line-height: 1; 
		min-width: 818upx; 
		height:300upx; 
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
		font-size: 16px; 
		font-weight: normal;
	}
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
	.team-img1{
		width: 100upx;
		height: 100upx;
		position: relative;
		margin-left: 100upx;
	}
	.team-img2{
		width: 100upx;
		height: 100upx;
		position: relative;
		margin-left: 230upx;
	}
	.team-img3{
		width: 100upx;
		height: 100upx;
		position: relative;
		margin-left: 230upx;
	}
	.team-img4{
		width: 100upx;
		height: 100upx;
		position: relative;
		margin-left: 200upx;
	}
	.team-img5{
		width: 100upx;
		height: 100upx;
		position: relative;
		margin-left: 230upx;
	}
	.team-img6{
		width: 100upx;
		height: 100upx;
		position: relative;
		margin-left: 200upx;
	}
	.topindex{
		display: block;
		height: 50px;
	}
</style>