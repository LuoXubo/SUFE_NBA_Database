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
		<button @click="to_career_detail(id)" class="to_career_button">Career Data</button>
	</view>
</template>

<script>
	export default {
		data (){
			return{
				name : 'Stephen Curry',
				number : '30',
				position : 'Guard',
				height : '191cm',
				weight : '84kg',
				player_img : 'https://cdn.nba.com/headshots/nba/latest/1040x760/201939.png',
				player_img_full : 'https://marstranslator-images-sz.oss-cn-shenzhen.aliyuncs.com/cover_images/15849649128543.jpg',
				id : 100,
			}
		},
		onLoad(option){
			// console.log(option.id)
			this.id = option.id;
			
		},
		methods:{
			to_career_detail(id) {
				uni.navigateTo({
					url: './career_detail?id='+id,
					success: res => {},
					fail: () => {},
					complete: () => {}
				});
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
	.to_career_button{
		width: 400upx; 
		height: 100upx; 
		font-size: 40upx; 
		border-radius: 20upx;
		background-color: #18BC37;
		color: white;
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
