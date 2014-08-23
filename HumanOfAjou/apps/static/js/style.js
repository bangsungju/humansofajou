// if($(console.log($(window).scrollTop())>= 300))
// {
// 	$("#background-image").attr('style','-moz-filter: blur(20px); -webkit-filter: blur(5px); -ms-filter: blur(5px); filter: blur(5px);');
// }

// var winScroll = $(window).scrollTop()
// if(winScroll >= 500)
// {
// 	$("#background-image").attr('style','-moz-filter: blur(20px); -webkit-filter: blur(5px); -ms-filter: blur(5px); filter: blur(5px);');
// }
// var winScroll = $(window).scrollTop()
// if(winScroll >= 500)
// {
// 	$("#background-image").css('style','-moz-filter: blur(20px); -webkit-filter: blur(5px); -ms-filter: blur(5px); filter: blur(5px);');
// }


$(document).ready(function(){
	$(window).on('scroll', function() {
		console.log($(window).scrollTop());
		if($(window).scrollTop() < 450) {
			var $scrollTop = $(window).scrollTop();
			var $scrollPoint = 450;

			var $per = 20 * ($scrollTop / $scrollPoint);
			console.log($per);

			$("#background-image").attr('style','-moz-' + $per + 'filter: blur(' + $per + 'px); -webkit-filter: blur(' + $per + 'px); -ms-filter: blur(' + $per + 'px); filter: blur(' + $per + 'px);');
		}
	});
	
});


$( window ).bind( 'scroll', function(){
  var srlTop  = $( this ).scrollTop();
  if( srlTop > 710 )
  {
    $( '#Header_nav_bar' ).css({ position :'fixed', top : '0px' ,right:'0px' ,left:'0px'});
  }
  else
  {
    $( '#Header_nav_bar' ).css({ position :'relative', top : '0px',right:'0px',left:'0px'});
  }
});
