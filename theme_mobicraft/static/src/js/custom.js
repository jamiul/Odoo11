$(window).scroll(function() {
    if ($(window).scrollTop() >= 41) {
        $('body').addClass('header-fixed');
    } else {
        $('body').removeClass('header-fixed');
    }
});
//mobile touch
$(document).ready(function($) {
    $(".carousel").carousel();
});
$(document).ready(function($) {
    // browser window scroll (in pixels) after which the "back to top" link is shown
    var offset = 300,
        //browser window scroll (in pixels) after which the "back to top" link opacity is reduced
        offset_opacity = 1200,
        //duration of the top scrolling animation (in ms)
        scroll_top_duration = 700,
        //grab the "back to top" link
        $back_to_top = $('.cd-top');

    //hide or show the "back to top" link
    $(window).scroll(function() {
        ($(this).scrollTop() > offset) ? $back_to_top.addClass('cd-is-visible'): $back_to_top.removeClass('cd-is-visible cd-fade-out');
        if ($(this).scrollTop() > offset_opacity) {
            $back_to_top.addClass('cd-fade-out');
        }
    });

    //smooth scroll to top
    $back_to_top.on('click', function(event) {
        event.preventDefault();
        $('body,html').animate({
            scrollTop: 0,
        }, scroll_top_duration);
    });

    $('div#recommended_products_slider').owlCarousel({
        margin: 10,
        responsiveClass: true,
        items: 4,
        loop: true,
        autoPlay: 7000,
        stopOnHover: true,
        navigation: true,
        responsive: {
            0: {
                items: 1,
                nav: false
            },
            500: {
                items: 2,
                nav: false
            },
            700: {
                items: 3,
                margin: 10,
                nav: false
            },
            1000: {
                items: 4,
                nav: false,
                loop: false
            },
            1500: {
                items: 4,
                nav: false,
                loop: false
            }
        }
    });

    // Grid/List switching code
    $(".oe_website_sale .shift_list_view").click(function(e) {
        $(".oe_website_sale .shift_grid_view").removeClass('active')
        $(this).addClass('active')
        $('#products_grid').addClass("list-view-box");
        $('.oe_website_sale .oe_subdescription').addClass('hidden');
        localStorage.setItem("product_view", "list");
    });

    $(".oe_website_sale .shift_grid_view").click(function(e) {
        $(".oe_website_sale .shift_list_view").removeClass('active')
        $(this).addClass('active')
        $('#products_grid').removeClass("list-view-box");
        $('.oe_website_sale .oe_subdescription').removeClass('hidden');
        localStorage.setItem("product_view", "grid");
    });

    if (localStorage.getItem("product_view") == 'list') {
        $(".oe_website_sale .shift_grid_view").removeClass('active')
        $(".oe_website_sale .shift_list_view").addClass('active')
        $('.oe_website_sale .oe_subdescription').addClass('hidden');
        $('#products_grid').addClass("list-view-box");
    }

    if (localStorage.getItem("product_view") == 'grid') {
        $(".oe_website_sale .shift_list_view").removeClass('active')
        $(".oe_website_sale .shift_grid_view").addClass('active')
        $('.oe_website_sale .oe_subdescription').removeClass('hidden');
        $('#products_grid').removeClass("list-view-box");
    }
    // Grid/List switching code ends

    // Switched to review section
    $('p.review').click(function() {
        $('body').animate({
            scrollTop: $(this).offset().top
        }, 1800);
        $('ul#description_reviews_tabs > li').removeClass('active')
        $('div#description_reviews_tabs_contents > div').removeClass('active')
        $('ul#description_reviews_tabs > li:nth-child(2)').addClass('active')
        $('div#description_reviews_tabs_contents > div:nth-child(2)').addClass('active')
    });

    // Toggle global search
    $('.static-search').on('click', function(e) {
        $('.hm-search').toggleClass("search-toggle-open")
        $("input[name='search']").focus();
    });

    $("body").click(function(e) {
        if (e.target.className !== "fa fa-search" && e.target.className !== "form-control" && e.target.className !== "hm-search search-toggle-open") {
            $('.hm-search').removeClass("search-toggle-open");
        }
    });

});

// For Megamenu
$(document).on('click', '.mega-dropdown-menu', function(e) {
    e.stopPropagation()
});

//Equal height
// $(window).load(function() {
//     equal_height_all();
// });

/*function equal_height_all() {
    function resetHeight() {
        var maxHeight = 0;
        jQuery(".cs-product .pwp-info .pwpi-title").height("auto").each(function() {
            maxHeight = $(this).height() > maxHeight ? $(this).height() : maxHeight;
        }).height(maxHeight);
    }
    resetHeight();
    jQuery(window).resize(function() {
        resetHeight();
    });
}*/

$(document).ready(function() {
    $(".li-mega-menu > a .fa").click(function() {
        $(this).parent().parent().toggleClass("mob-open");
    });
});

//mobile Touch
$(document).ready(function() {
    // Activate Carousel
    $("#myCarousel").carousel();

    // Enable Carousel Indicators
    $(".item1").click(function() {
        $("#myCarousel").carousel(0);
    });
    $(".item2").click(function() {
        $("#myCarousel").carousel(1);
    });
    $(".item3").click(function() {
        $("#myCarousel").carousel(2);
    });
    $(".item4").click(function() {
        $("#myCarousel").carousel(3);
    });

    // Enable Carousel Controls
    $(".left").click(function() {
        $("#myCarousel").carousel("prev");
    });
    $(".right").click(function() {
        $("#myCarousel").carousel("next");
    });

    $(function() {
        $('.item.active img').addClass('animated');
        $(".item.active .big").addClass("animated");
        $(".item.active .small").addClass("animated");
        $(".item.active img").addClass("animated");
        $(".item.active .banner-button").addClass("animated");
    });

});

$(document).ready(function() {
    $("#myCarousel").carousel({
        interval: 500,
        pause: false
    });
});
