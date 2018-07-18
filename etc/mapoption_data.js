// 初始化地图
var BMapExt = new BMapExtension(domMain, BMap, require('echarts'), require('zrender'));
var map = BMapExt.getMap();
var container = BMapExt.getEchartsContainer();
var point = new BMap.Point(startPoint.x, startPoint.y);
map.centerAndZoom(point, 5);
map.enableScrollWheelZoom(true);



option = {
    color: ['gold','aqua','lime'],
    title : {
        text: '访问来源',
        subtext:'',
        x:'right'
    },
    tooltip : {
        trigger: 'item',
        formatter: function (v) {
            return v[1].replace(':', ' > ');
        }
    },
    legend: {
        orient: 'vertical',
        x:'left',
        data:['北京'],
        selectedMode: 'single',
        selected:{
            
        }
    },
    toolbox: {
        
    },
    dataRange: {
        min : 0,
        max : 100,
        y: '60%',
        calculable : true,
        color: ['#ff3333', 'orange', 'yellow','lime','aqua']
    },
    series : [
        {
            name:'北京',
            type:'map',
            mapType: 'none',
            data:[],
            geoCoord: {
                
            },

            markLine : {
                smooth:true,
                effect : {
                    show: true,
                    scaleSize: 1,
                    period: 30,
                    color: '#fff',
                    shadowBlur: 10
                },
                itemStyle : {
                    normal: {
                        borderWidth:1,
                        lineStyle: {
                            type: 'solid',
                            shadowBlur: 10
                        }
                    }
                },
                data : [
                    [{name:'上海'}, {name:'北京',value:115}],  
                    [{name:'乌鲁木齐'}, {name:'北京',value:10}],  
                    [{name:'兰州'}, {name:'北京',value:71}],  
                    [{name:'北京'}, {name:'北京',value:278}],  
                    [{name:'南京'}, {name:'北京',value:36}],  
                    [{name:'南进'}, {name:'北京',value:26}],  
                    [{name:'合肥'}, {name:'北京',value:10}],  
                    [{name:'哈尔滨'}, {name:'北京',value:6}],  
                    [{name:'嘉兴'}, {name:'北京',value:18}],  
                    [{name:'天津'}, {name:'北京',value:21}],  
                    [{name:'太原'}, {name:'北京',value:21}],  
                    [{name:'宁波'}, {name:'北京',value:10}],  
                    [{name:'广州'}, {name:'北京',value:55}],  
                    [{name:'成都'}, {name:'北京',value:79}],  
                    [{name:'杭州'}, {name:'北京',value:31}],  
                    [{name:'武汉'}, {name:'北京',value:26}],  
                    [{name:'沈阳'}, {name:'北京',value:6}],  
                    [{name:'河北'}, {name:'北京',value:17}],  
                    [{name:'济南'}, {name:'北京',value:19}],  
                    [{name:'深圳市'}, {name:'北京',value:16}],  
                    [{name:'湖陂'}, {name:'北京',value:11}],  
                    [{name:'福州市'}, {name:'北京',value:27}],  
                    [{name:'西宁'}, {name:'北京',value:9}],  
                    [{name:'西安'}, {name:'北京',value:19}],  
                    [{name:'贵阳'}, {name:'北京',value:63}],  
                    [{name:'郑州'}, {name:'北京',value:89}],  
                    [{name:'重庆'}, {name:'北京',value:51}],  
                    [{name:'长春'}, {name:'北京',value:14}],  
                    [{name:'长沙市'}, {name:'北京',value:14}],  
                    [{name:'阿姆斯特丹'}, {name:'北京',value:14}],  
                    [{name:'雷德蒙德'}, {name:'北京',value:7}]
                ]
            },
            markPoint : {
                symbol:'emptyCircle',
                symbolSize : function (v){
                    return 10 + v/10
                },
                effect : {
                    show: true,
                    shadowBlur : 0
                },
                itemStyle:{
                    normal:{
                        label:{show:false}
                    }
                },
                data : [
                    {name:'上海',value:115},  
                    {name:'乌鲁木齐',value:10},  
                    {name:'兰州',value:71},  
                    {name:'北京',value:278},  
                    {name:'南京',value:36},  
                    {name:'南进',value:26},  
                    {name:'合肥',value:10},  
                    {name:'哈尔滨',value:6},  
                    {name:'嘉兴',value:18},  
                    {name:'天津',value:21},  
                    {name:'太原',value:21},  
                    {name:'宁波',value:10},  
                    {name:'广州',value:55},  
                    {name:'成都',value:79},  
                    {name:'杭州',value:31},  
                    {name:'武汉',value:26},  
                    {name:'沈阳',value:6},  
                    {name:'河北',value:17},  
                    {name:'济南',value:19},  
                    {name:'深圳市',value:16},  
                    {name:'湖陂',value:11},  
                    {name:'福州市',value:27},  
                    {name:'西宁',value:9},  
                    {name:'西安',value:19},  
                    {name:'贵阳',value:63},  
                    {name:'郑州',value:89},  
                    {name:'重庆',value:51},  
                    {name:'长春',value:14},  
                    {name:'长沙市',value:14},  
                    {name:'阿姆斯特丹',value:14},  
                    {name:'雷德蒙德',value:7}
                ]
            }
            
        }
    ]
};

if (myChart && myChart.dispose) {
    myChart.dispose();
}
myChart = BMapExt.initECharts(container, curTheme);
window.onresize = myChart.resize;
BMapExt.setOption(option, true)
                    