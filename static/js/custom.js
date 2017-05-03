function app_name(name) {
    switch (name) {
        case "conversor":
            return "converter";
        case "sumarizador":
            return "summarizer";
        case "tradutor":
            return "translator";
        case "alinhador":
            return "aligner";
        case "registrar":
            return "register";
        case "editar":
            return "edit";
        default:
            return "login";
    }
}

$(document).ready(function(){
    var name = $.trim($('.title-session').text()).toLowerCase();
    var app = "/" + app_name(name);

    $('ul.nav a[href="'+ app +'"]').parent().addClass('active');
    $('ul.nav a[id="'+ app +'"]').parent().addClass('active');
    if (app == '/edit') {
        $('li.dropdown').addClass('active');
    }
    $('ul.nav a').filter(function() {
        return this.href == app;
    }).parent().addClass('active');

    var color = $('li.active').css("border-bottom-color");
    $('.title-session').css(
        "border-color", color
    );

    var icon = $('li.active span').attr('class');
    $('.title-session').append(
        "<span class='"+icon+"'></span>"
    );
    $('.title-session span').css(
        "color", color
    );

    $('.submenu').click(function() {
        if ($(this).hasClass('sub1') 
            && !$(this).hasClass('collapsed')
            && $('.sub2').hasClass('collapsed')) {
            $('.submenu').children().addClass('reset-collapsed');
        } else if ($(this).hasClass('sub2') 
                   && !$(this).hasClass('collapsed')
                   && $('.sub1').hasClass('collapsed')) {
            $('.submenu').children().addClass('reset-collapsed');
        } else {
            $('.submenu').children().removeClass('reset-collapsed');
        }
    });

    $($('.title-session').find('span')).clone().appendTo('h4.subtitle-session span');

    $(".alert-success").delay(5000).fadeOut(500, function() {
        $(this).alert('close');
    });

    $('#id_is_summarized').change(function() {
        var bool = $(this).prop("checked");
        if (bool) {
            $(this).val('True');
        } else {
            $(this).val('False');
        }
    });
});