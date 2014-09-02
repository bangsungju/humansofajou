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


// $(document).ready(function(){
// 	$(window).on('scroll', function() {
// 		console.log($(window).scrollTop());
// 		if($(window).scrollTop() < 450) {
// 			var $scrollTop = $(window).scrollTop();
// 			var $scrollPoint = 450;

// 			var $per = 20 * ($scrollTop / $scrollPoint);
// 			console.log($per);

// 			$("#background-image").attr('style','-moz-' + $per + 'filter: blur(' + $per + 'px); -webkit-filter: blur(' + $per + 'px); -ms-filter: blur(' + $per + 'px); filter: blur(' + $per + 'px);');
// 		}
// 	});

// });


$(window).scroll(function() {
      // get scroll position
      var s = $(window).scrollTop();
      // scroll value and opacity
      opacityVal = (s / 280.0);
      // opacity value 0% ~ 100%
      $('.blurred-img').css('opacity', opacityVal);
    });


// navbar fixed by scroll
$( window ).bind( 'scroll', function(){
  var srlTop  = $( this ).scrollTop();
  var winHeight = $(window).height();
  if( srlTop > winHeight-53)
  {
    $( '#Header_nav_bar' ).css({ position :'fixed', top : '300px' ,right:'0px' ,left:'0px'});
    $( '#Header_nav_bar li' ).css({ float: 'none'});
    $( '#Header_nav_bar li' ).css({ width: '96px'});

    $( '.Prev_detail').css({position:'fixed', top : '330px' ,left :'50px'});
    $( '.Next_detail').css({position:'fixed', top : '330px' ,right:'50px'});
  }
  else
  {
    $( '#Header_nav_bar' ).css({ position :'relative', top : '0px',right:'0px',left:'0px'});
    $( '#Header_nav_bar li' ).css({ float: 'left'});
    $( '#Header_nav_bar li' ).css({ width: '96px'});

    
    $( '.Prev_detail').css({position:'relative'});
    $( '.Next_detail').css({position:'relative'});
  }
});


