
//switch
aa=3;
switch(aa){case 1:console.log(1);break;case 2:console.log(2);break;case 3: console.log(33);break;default: 444}

var i = 0;
var sum = 0;
while(i<=100){
    sum +=i;
    i++;
}


sum = 0;
for(var i=0;i<=100;i++){
    sum +=i;
}

//遍历数组
list = ['a','b','c','d'];
for(var i = 0 ;i<list.length;i++){
    console.log(list[i])
}

//删除元素
delete list[10];

//遍历数组
for (var item in list){
    console.log(list[item]);
}

//遍历字典
dic = {name:'ll',age:30}

for (var key in dic){
    console.log(key+'::'+dic[key]);
}


alert('提示信息');
prompt('请输入信息：');
confirm('确认删除吗?');

//函数
function sy_hi(name){
    console.log('Hi,'+name);
}

//函数返回值
function add(a,b){
    return a+b;
}