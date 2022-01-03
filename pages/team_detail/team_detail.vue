<template>
	<view class="container">
		<!-- 球队及教练信息 -->
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
					<image class="coach_img" :src="coach_img" @tap="to_coach_detail"></image>
					<view style="font-size: 30upx;">{{coach_name}}</view>
				</view>
			</view>
		</view>
		
		<!-- 球员信息 -->
		<view style="margin-top: 100upx; margin-left: 1000upx;">
			<view v-for="(item,index) in player" style="margin-left: 100upx; margin-top: 50upx;">
				<view style="display: flex; flex-direction: row;">
					<image :src="item.img" class="player_img" @tap="to_player_detail"></image>
					<view style="font-size: 40upx; margin-left: 40upx; margin-top: 50upx;">{{item.name}}</view>
					<view style="font-size: 30upx; margin-left: 40upx; margin-top: 50upx;">{{item.number}}</view>
				</view>
			</view>
		</view>
		
		
	</view>
</template>

<script>
	export default{
		data() {
			return {
				team_name : 'Golden State Warriors',
				team_name_cn : '金州勇士队',
				team_img: 'https://china.nba.com/media/img/teams/logos/GSW_logo.svg',
				team_city : 'San Francisco',
				team_info: 'The whole team is a city',
				coach_img : 'https://www.basketball-reference.com/req/202106291/images/coaches/kerrst01c.png',
				coach_name : 'Steve Kerr',
				player: [
					{
						img: 'https://cdn.nba.com/headshots/nba/latest/1040x760/201939.png',
						number : 30,
						name : 'Stephen Curry'
					},
					{
						img: 'https://cdn.nba.com/headshots/nba/latest/1040x760/203110.png',
						number : 23,
						name : 'Draymond Green'
					},
					{
						img: 'https://cdn.nba.com/headshots/nba/latest/1040x760/202691.png',
						number : 11,
						name : 'Klay Thompson'
					}
				]
			}
		},
		methods:{
			to_coach_detail(e){
				uni.navigateTo({
					url:'../coach_detail/coach_detail',
					fail(e){
						console.log(e)
					}
				})
			},
			to_player_detail(e){
				uni.navigateTo({
					url : '../player_detail/player_detail',
					fail(e){
						console.log(e)
					}
				})
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
