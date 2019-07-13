function openNav() {
        document.getElementById("mySidebar").style.width = "250px";
        //document.getElementById("main").style.marginLeft = "250px";
    }
      
function closeNav() {
        document.getElementById("mySidebar").style.width = "0";
       // document.getElementById("main").style.marginLeft= "0";
    }
$num = $('.my-card').length;
$even = $num / 2;
$odd = ($num + 1) / 2;
 
if ($num % 2 == 0) {
  $('.my-card:nth-child(' + $even + ')').addClass('active');
  $('.my-card:nth-child(' + $even + ')').prev().addClass('prev');
  $('.my-card:nth-child(' + $even + ')').next().addClass('next');
} else {
  $('.my-card:nth-child(' + $odd + ')').addClass('active');
  $('.my-card:nth-child(' + $odd + ')').prev().addClass('prev');
  $('.my-card:nth-child(' + $odd + ')').next().addClass('next');
}
 
$('.my-card').click(function() {
  $slide = $('.active').width();
  console.log($('.active').position().left);
   
  if ($(this).hasClass('next')) {
    $('.card-carousel').stop(false, true).animate({left: '-=' + $slide});
  } else if ($(this).hasClass('prev')) {
    $('.card-carousel').stop(false, true).animate({left: '+=' + $slide});
  }
   
  $(this).removeClass('prev next');
  $(this).siblings().removeClass('prev active next');
   
  $(this).addClass('active');
  $(this).prev().addClass('prev');
  $(this).next().addClass('next');
});
 
 
// Keyboard nav
$('html body').keydown(function(e) {
  if (e.keyCode == 37) { // left
    $('.active').prev().trigger('click');
  }
  else if (e.keyCode == 39) { // right
    $('.active').next().trigger('click');
  }
});
$('.carousel.carousel-multi-item.v-2 .carousel-item').each(function(){
  var next = $(this).next();
  if (!next.length) {
    next = $(this).siblings(':first');
  }
  next.children(':first-child').clone().appendTo($(this));

  for (var i=0;i<4;i++) {
    next=next.next();
    if (!next.length) {
      next=$(this).siblings(':first');
    }
    next.children(':first-child').clone().appendTo($(this));
  }
});