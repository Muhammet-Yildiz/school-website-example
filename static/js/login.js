$(function() {
    var formicon2 = $(".fa-eye")
    var passwordInput = $("#passwordInput")
    formicon2.on("click", function() {

        // console.log(passwordInput.attr("type"))
        if (passwordInput.attr("type") == 'password') {
            passwordInput.attr("type", "text")
            $(this).addClass("fa-eye-slash")
            $(this).removeClass("fa-eye")

        } else {
            passwordInput.attr("type", "password")
            $(this).removeClass("fa-eye-slash")
            $(this).addClass("fa-eye")
        }

    })


    // KULLANICI GİRİŞ YAPTIGINDA 
    //AJAX İLE POST İŞLEMİ GONDERİCEM loginuser fonksiyonuna 


    $("#loginBtn").click(function(e) {

        e.preventDefault();
        console.log("submitlenme engellendi ")

        usernameValue = $("#usernameInput").val()
        passwordValue = $("#passwordInput").val()

        domain_Name = $("select#domain_name").val()

        console.log("username value ==", usernameValue)
        console.log("parola value ==", passwordValue)
        console.log("secilen alan adı ==", domain_Name)

        function getToken(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        const csrftoken = getToken('csrftoken');
        var url = '/auth/login'

        fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify({
                    'usernameValue': usernameValue,
                    'domain_Name': domain_Name,
                    'passwordValue': passwordValue
                })

            })
            .then((response) => {
                return response.json()
            })
            .then((data) => {
                console.log('data : ', data)

                if (data.bool) {

                    window.location.pathname = "/admin"

                } else {
                    // demekki hata almıs hata mesajı gosterelım 
                    $(".error_message").css("display", "flex")
                    
                }
            })






    })











})