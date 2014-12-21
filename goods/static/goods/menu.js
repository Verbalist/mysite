//Bases Technics Holidays Colors Materials
menuItem = []
stack = []
function stackObj(clas) {
	this.clas = clas;
	this.value = [];
	 
	
}
function getMenuItem() {
	var req = $.ajax({
		url:'/goods/jsonMenu',
		dataType:'json',
		cache:true
	}).done(function(){
		menuItem = req.responseJSON;
	});
}


function menu(e,item) {
	$('.garbage').remove();
	if ($(e).is('.empty'))
		for (j in menuItem) {
			if (menuItem[j].model == item) {
				$('<h5 class="animated fadeInLeft my_menu '+item.split('.')[1]+' '+menuItem[j].pk+'" onclick="myFilterIn(this)">'
					+menuItem[j].fields.name+'</h5>').insertAfter($(e))
		}
		$(e).attr('class','full')
	}
	else {//надо доделать что-б когда уезжают фильтры или уезжали и те или не унеузжали но приетом снова выезжали без
		$('.'+item.split('.')[1]).each(function(){
				$(this).slideUp(400)
				$(this).attr('class','garbage')}
			)
		$(e).attr('class','empty')
	}
}

function myFilterIn(e,type){
	$('.garbage').remove();
	var clas = $(e).attr('class')
	$('<h5 class="'+clas+'" onclick="myFilterOut(this)">'
		+$(e).html()+'</h5>').appendTo($('#filters'))
	$(e).attr('class','animated fadeOutLeft garbage').slideUp(500)

	var passed = stack.some(function(el,i,arr){
		return stack[i].clas == clas.split(' ')[3] 
	})	
			
	if (passed) {
		for (i in stack)
			if (stack[i].clas == clas.split(' ')[3])
				stack[i].value.push(clas.split(' ')[4])
	}
	else {
		var temp = new stackObj(clas.split(' ')[3]);
		temp.value.push(clas.split(' ')[4])
		stack.push(temp);
	}
	filtered();
}

function myFilterOut(e){
	var clas = $(e).attr('class')
	$('.garbage').remove();
	$('<h5 class="'+clas+'" onclick="myFilterIn(this)">'
		+$(e).html()+'</h5>').insertAfter('#'+clas.split(' ')[3])
	$(e).attr('class','animated fadeOutLeft garbage').slideUp(500);
	
	for(i in stack){
		stack[i].value.splice(stack[i].value.indexOf(clas.split(' ')[4]),1);
		if (stack[i].value.length == 0) stack.splice(i,1);
	}
	filtered();
}



$('document').ready(function() {
	getMenuItem()
})
