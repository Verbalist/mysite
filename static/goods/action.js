$(document).ready(function(){
	$("h1").click(function(){alert('lol')})
	var i = 0;
	var a = setInterval(function(){
		if (i == 100) clearInterval(a);
		i++;	
		$("h1").css({"padding-left": i});
		},10)
	$("#lol").css({'color':'red'})
	
	var b = setInterval(function(){
		if (i == 1000) clearInterval(b);
		i++;	
		$("#test").css({"padding-left": i});
		},10)
});


