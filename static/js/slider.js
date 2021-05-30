// navbar dakı su konuları ıcın yaptıgımız slicky slıder 
$('.slicky-slider').slick({

    prevArrow: '.arrow-prev',
    nextArrow: '.arrow-next ',
    autoplay: true,
    speed: 1000,
    fade: true,
    pauseOnHover: true,
    touchMove: true,
    autoplaySpeed: 5000,
    slidesToShow: 1,
    // slidesToScroll: 1,
    dots: true,
    infinite: true,
});

$(function() {
    $("li[role='presentation']>button").html(" ")
    $("li[role='presentation']>button").click(function() {

        $(this).css({
            'border-radius': '50%',
            'outline': '0',
        })

    })
})