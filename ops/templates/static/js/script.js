$('.container-vuelo').hover(
	function(){
		var originalContainer = this;
		$(this).find(".horas-vuelo").stop(true,true).fadeOut(50,function(){
			$(originalContainer).css('padding-top','15px');
		});
		$(this).find(".destino-origen").stop(true,true).fadeOut(50,function(){
			$(originalContainer).css('padding-top','15px');
		});
		
		$(this).stop().animate({
				backgroundColor: '#ea0b1a'
			},50,'linear', function(){
				$(this).children(".codigo-vuelo").fadeIn(50);
			});
	},function(){
		var originalContainer = this;
		$(this).find(".codigo-vuelo").fadeOut(50,function(){
			$(originalContainer).css('padding-top','8px');
			$(originalContainer).find(".destino-origen").fadeIn(50);
			$(originalContainer).find(".horas-vuelo").fadeIn(50);
		});
		
		$(this).stop().animate({
				backgroundColor: '#2D232E'
			},50,'linear', function(){
			$(originalContainer).css('padding-top','8px');
		});
	}
);

/*
$('.container-vuelo').bind('mouseenter'.mouseOverMe).bind('mouseleave',mouseOutMe);

function mouseOverMe(){
	console.log("hols");
	$(this).children(".destino-origen").stop(true,true).fadeOut(500);
}

function mouseOutMe(){
	$(this).children(".destino-origen").fadeIn(500);
}*/