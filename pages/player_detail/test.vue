<template>
    <view class="qiun-columns">
		<uni-card>
			<view class="qiun-bg-white qiun-title-bar qiun-common-mt" >
			    <view class="qiun-title-dot-light">基本折线图</view>
			</view>
			<view class="qiun-charts" >
			    <canvas canvas-id="canvasLineA" id="canvasLineA" class="charts" @touchstart="touchLineA"></canvas>
			</view>
			
		</uni-card>
        
    </view>
</template>
<script>
    import uCharts from '../../components/u-charts/u-charts.js';
    var _self;
    var canvaLineA=null;
    export default {
        data() {
            return {
                cWidth:'',
                cHeight:'',
                pixelRatio:1,
            }
        },
        onLoad() {
            _self = this;
            this.cWidth=uni.upx2px(750);
            this.cHeight=uni.upx2px(500);
            this.getServerData();
        },
        methods: {
            getServerData(){
                        let LineA={categories:[],series:[]};
                        //这里我后台返回的是数组，所以用等于，如果您后台返回的是单条数据，需要push进去
                        LineA.categories=['2012','2013','2014'];
                        LineA.series=[{
							name : 'Year',
							data : [20, 10, 20],
							color : '#000000'
						}];
                        _self.showLineA("canvasLineA",LineA);
			},
                  
            showLineA(canvasId,chartData){
                canvaLineA=new uCharts({
                    $this:_self,
                    canvasId: canvasId,
					context:uni.createCanvasContext(canvasId, _self),
                    type: 'line',
                    fontSize:11,
                    legend:true,
                    dataLabel:false,
                    dataPointShape:true,
                    background:'#FFFFFF',
                    pixelRatio:_self.pixelRatio,
                    categories : ['2012','2013','2014'],
                    series : [{
                    	name : 'Year',
                    	data : [20, 10, 20],
                    	color : '#000000'
                    }],
                    animation: true,
                    xAxis: {
                        type:'grid',
                        gridColor:'#CCCCCC',
                        gridType:'dash',
                        dashLength:8
                    },
                    yAxis: {
                        gridType:'dash',
                        gridColor:'#CCCCCC',
                        dashLength:8,
                        splitNumber:5,
                        min:10,
                        max:180,
                        
                    },
                    width: _self.cWidth*_self.pixelRatio,
                    height: _self.cHeight*_self.pixelRatio,
                    extra: {
                        line:{
                            type: 'straight'
                        }
                    }
                });
            },
            touchLineA(e) {
                canvaLineA.showToolTip(e, {
                    format: function (item, category) {
                        return category + ' ' + item.name + ':' + item.data 
                    }
                });
            }
        }
    }
</script>
<style>
    /*样式的width和height一定要与定义的cWidth和cHeight相对应*/
    .qiun-charts {
        width: 750upx;
        height: 500upx;
        background-color: #FFFFFF;
    }
    .charts {
        width: 750upx;
        height: 500upx;
        background-color: #FFFFFF;
    }
</style>
