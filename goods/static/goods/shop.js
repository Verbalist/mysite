var IMAGES_URL='/media/';
var req = $.ajax({
	url:'/goods/jsonGoods',
	dataType:'json',
	cache:false,
	success:function(data){
		show(data,true);
	}
}).done(function(){
	data = req.responseJSON;
});

function filtered() {
	var data_w = data;
	
	for (j in stack) {
		if (stack[j].value.length != 0 ) {
			var temp = []
			for (i in data_w) {
				for (k in stack[j].value) {
					if (stack[j].clas == 'bases') {
						if (data_w[i].fields.base == parseInt(stack[j].value[k])) temp.push(data_w[i]);}
					else if (stack[j].clas == 'technics') { 
						if (data_w[i].fields.technic == parseInt(stack[j].value[k])) temp.push(data_w[i]);}
					else if (stack[j].clas == 'colors') {
						if (data_w[i].fields.color == parseInt(stack[j].value[k])) temp.push(data_w[i]);}
					else if (stack[j].clas == 'holidays') {
						if (data_w[i].fields.holiday == parseInt(stack[j].value[k])) temp.push(data_w[i]);}
					else if (stack[j].clas == 'styles') {
						if (data_w[i].fields.style == parseInt(stack[j].value[k])) temp.push(data_w[i]);}
				}
			}
			data_w = temp;
		}
	}
	show(data_w,true);
}


function show(data, is_refresh) {
	if (is_refresh) $('#show').html('');
	for(i in data) {
		if (data[i].fields.count != -1) {
			$('<div class="col-md-3">'+
				'<img height="250" src="'+IMAGES_URL+data[i].fields.avatar+'">'+
				'<a href="'+data[i].pk+'">'+data[i].fields.name+'</a>'+
				'<h5>Цена: '+data[i].fields.price+' грн</h5>'+
				'</div>').appendTo('#show');
		}
	}
}
