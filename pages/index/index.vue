<template>
	<view class="container" style="flex-direction: row; ">
		<view class="display-flex">
			<view v-for="(item,index) in imgs" :key="index" style="margin: 100upx;">
				<image :src="item.src" class="team-img" @tap="to_team_detail"></image>
				<view style="font-size: 30upx; margin-left: 20upx;">{{item.name}}</view>
			</view>
		</view>
	</view>
	
</template>

<script>
	export default {
		data() {
			return {
				imgs : [
					{
						src : 'https://china.nba.com/media/img/teams/logos/ATL_logo.svg',
						name : 'ATL'
					},
					{
						src : 'https://china.nba.com/media/img/teams/logos/CHA_logo.svg',
						name : 'CHA'
					},
					{
						src : 'https://china.nba.com/media/img/teams/logos/ORL_logo.svg',
						name : 'ORL'
					},
					{
						src : 'https://china.nba.com/media/img/teams/logos/WAS_logo.svg',
						name : 'WAS'
					},
					{
						src : 'https://china.nba.com/media/img/teams/logos/PHI_logo.svg',
						name : 'PHI',
						
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
					console.log(res)
				},
				fail: () => {},
				complete: () => {}
			});
		},
		methods: {	
			to_team_detail(e){
				uni.navigateTo({
					url:'../team_detail/team_detail',
					fail(e) {
						console.log(e)
					}
				})
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
