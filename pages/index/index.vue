<template>
	<view class="container">
		<uni-card>
			<view style="display: flex; flex-direction: row;">
				<view style="font-size: 50upx; color: #007AFF; margin-left: 700upx;">Home</view>
				<view style="font-size: 50upx; color: #ff00ff; margin-left: 700upx;" @tap="to_leaderboard">Leaderboard</view>
				<view style="font-size: 50upx; color: #ff00ff; margin-left: 700upx;" @tap="to_comparison">Player Comparison</view>
			</view>
		</uni-card>
		<uni-card>
			<view style="display: flex; flex-direction: row;">
				<view v-for="(item,index) in teams" :key="index" style="margin: 100upx;">
					<image :src="item.photo" class="team-img" @tap="to_team_detail(item.id)"></image>
					<view style="font-size: 30upx; margin-left: 20upx;">{{item.name_e}}</view>
				</view>
			</view>
		</uni-card>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				teams : [
					{
						id : 1,
						photo : 'https://china.nba.com/media/img/teams/logos/ATL_logo.svg',
						name_e : 'ATL'
					},
					{
						id : 2,
						photo : 'https://china.nba.com/media/img/teams/logos/CHA_logo.svg',
						name_e : 'CHA'
					},
					{
						id : 3,
						photo : 'https://china.nba.com/media/img/teams/logos/ORL_logo.svg',
						name_e : 'ORL'
					},
					{
						id : 4,
						photo : 'https://china.nba.com/media/img/teams/logos/WAS_logo.svg',
						name_e : 'WAS'
					},
					{
						id : 5,
						photo : 'https://china.nba.com/media/img/teams/logos/PHI_logo.svg',
						name_e : 'PHI',
					}
				]
			}
		},
		onLoad () {
			uni.request({
				url: '',
				method: 'GET',
				data: {},
				success: res => {
					// this.teams = res.data;
				},
				fail: () => {},
				complete: () => {}
			});
		},
		methods: {	
			to_team_detail(id){
				// console.log(id);
				uni.navigateTo({
					url:'../team_detail/team_detail?team_id=' + id,
					fail(e) {
						console.log(e)
					}
				})
			},
			to_leaderboard(e) {
				uni.navigateTo({
					url : '../',
					fail(e) {
						console.log(e)
					}
				})
			},
			to_comparison(e) {
				uni.navigateTo({
					url : '../',
					fail(e) {
						console.log(e)
					}
				})
			},
		}
	}
</script>

<style>
	.container {
		padding: 20upx;
		font-size: 14upx;
		line-height: 24upx;
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
</style>
