$(function() {

    $(".sec2c li ").each(function(index, element) {

        if (index == 0) {
            $(element).addClass("checked")
        }

    })

    $(".sec2c li ").click(function() {

        $(".sec2c li ").each(function(index, element) {

            $(this).removeClass("checked")

        })
        target = $(this)[0];

        hedef = $(target)[0];

        // console.log("SUAN AKTIF OLAN :== ", $(target)[0].data("cursor"))

        console.log("target :== ", $(hedef).data("cursor"))

        $(target).addClass("checked")


        textClass = $(hedef).data("cursor")

        if (textClass == "AnnouncementsWrap") {

            $(".AnnouncementsWrap").css("display", "flex")
            $(".newsWrap").css("display", "none")
            $(".StudentNewsWrap").css("display", "none")
            $(".automatıonsWrap").css("display", "none")
            $(".advertisementsWrap").css("display", "none")


        } else if (textClass == "newsWrap") {



            $(".newsWrap").css("display", "flex")
            $(".AnnouncementsWrap").css("display", "none")
            $(".StudentNewsWrap").css("display", "none")
            $(".automatıonsWrap").css("display", "none")
            $(".advertisementsWrap").css("display", "none")


        } else if (textClass == "StudentNewsWrap") {


            $(".newsWrap").css("display", "none")
            $(".AnnouncementsWrap").css("display", "none")
            $(".StudentNewsWrap").css("display", "flex")

            $(".automatıonsWrap").css("display", "none")
            $(".advertisementsWrap").css("display", "none")


        } else if (textClass == "automatıonsWrap") {

            $(".newsWrap").css("display", "none")
            $(".AnnouncementsWrap").css("display", "none")
            $(".StudentNewsWrap").css("display", "none")
            $(".automatıonsWrap").css("display", "flex")

            $(".advertisementsWrap").css("display", "none")


        } else if (textClass == "advertisementsWrap") {

            $(".advertisementsWrap").css("display", "flex")


            $(".newsWrap").css("display", "none")
            $(".AnnouncementsWrap").css("display", "none")
            $(".StudentNewsWrap").css("display", "none")
            $(".automatıonsWrap").css("display", "none")


        }


    })




})