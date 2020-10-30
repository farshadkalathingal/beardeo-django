
jQuery(function($) {
	
    'use strict';
    Window_Scroll();
});


// jQuery to collapse the navbar on scroll
var Window_Scroll = function() {
    $(window).scroll(function() {
        var scroll = $(window).scrollTop();
        if (scroll > 50) {
            $(".navbar").addClass("top-nav-collapse");
        } else {
            $(".navbar").removeClass("top-nav-collapse");
        }
    });
};



