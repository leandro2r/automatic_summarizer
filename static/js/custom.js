// Add name for each session used in this project
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
        case "créditos":
            return "credits";
        default:
            return "login";
    }
}

$(document).ready(function() {
    var name = $.trim($('.title-session').text()).toLowerCase();
    var app = "/" + app_name(name);

    // Navbar option activate
    $('ul.nav a[href="'+ app +'"]').parent().addClass('active');
    $('ul.nav a[id="'+ app +'"]').parent().addClass('active');
    if (app == '/edit') {
        $('li.dropdown').addClass('active');
    }
    $('ul.nav a').filter(function() {
        return this.href == app;
    }).parent().addClass('active');

    // Color bottom-line
    var color = $('li.active').css("border-bottom-color");
    $('.title-session').css(
        "border-color", color
    );

    // Color icon
    var icon = $('li.active span').attr('class');
    $('.title-session').append(
        "<span class='"+icon+"'></span>"
    );
    $('.title-session span').css(
        "color", color
    );

    // Collapsed menu from Converter
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

    // Clone App icon
    $($('.title-session').find('span')).clone().prependTo('h4.subtitle-session small');

    // App's messages
    $(".alert-success").delay(5000).fadeOut(500, function() {
        $(this).alert('close');
    });

    // Toggle from Converter collapsed menu
    $('#id_is_summarized').change(function() {
        var bool = $(this).prop("checked");
        if (bool) {
            $(this).val('True');
        } else {
            $(this).val('False');
        }

        $('.summarized').slideToggle( "fast", "linear" );
    });

    // Loading animation
    $('#run_app').click(function() {
        icon = ' <img src="/static/imgs/loading.gif" width="25px" height="25px">'
        var gerund = $(this).attr('title').slice(0, -1) + 'ndo';
        var subtitle = "<br><small>Dependendo do tamanho arquivo, isto poderá levar alguns minutos.</small>"
        var ratio = 0.1;
        if (gerund != 'Convertendo' || (gerund == 'Convertendo'
                                        && $("#id_title").val() != ""
                                        && $("#id_docfile").val() != "")) {
            $(".title-session").animate({opacity: ratio});
            $(".subtitle-session").animate({opacity: ratio});
            $(".panel-heading-custom").animate({opacity: ratio});
            $(".form-horizontal").animate({opacity: ratio});

            $("input").prop("readonly", true);
            $(".form-horizontal [type='submit']").hide();

            $('.loading').fadeIn(500);
            $('h4.loading').html(gerund + ", aguarde..." + icon + subtitle);
        }
    });
});