$(function() {

    // navbardakı hover mevzusu 


    $("nav ul li .menu__link").first().css("border-left", "#a61025 solid 1px ")


    // messages alanı bellı sanıye sonra yok olsun 


    setTimeout(function() {
        $(".messages").css("display", "none")
    }, 5000)


})