$(document).ready(function(){
	$.ajax({
		url:'/goods/json',
		dataType:'json',
		cache:false,
		success:function(data){
			alert(data[0].fields.name)
		}
	
	})
});


