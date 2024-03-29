/* Angular */
var app = angular.module("myApp",[]);
app.controller("myController", function($scope){
    $scope.info = [
        {
            "title": "Bay Area Book Festival",
            "location": "Berkeley, CA",
            "tickets": "24 Tickets",
            "interested": "34 Interested",
            "link": "event.html",
        },
        {
            "title": "Yerba Buena Center",
            "location": "701 Mission St, San Francisco, CA",
            "tickets": "30 Tickets",
            "interested": "67 Interested",
            "link": "event.html",
        },
        {
            "title": "The Crucible",
            "location": "1260 7th Street, Oakland, CA",
            "tickets": "30 Tickets",
            "interested": "67 Interested",
            "link": "event.html",
        },
        {
            "title": "Oakland Museum of CA",
            "location": "1000 Oak Street, Oakland, CA",
            "tickets": "30 Tickets",
            "interested": "67 Interested",
            "link": "event.html",
        },
    ];
});

/* Code inspired by W3Schools */

function myFunction(x) {
    x.classList.toggle("change");
}

/* Code below from: https://blog.adam-marsden.co.uk/minimal-page-transitions-with-jquery-css-d97f692d5292 */

$(function() {

    // $('a').each(function() { /* [1] */
    //      if ( location.hostname === this.hostname || !this.hostname.length ) { /* [1] */

    //         var link = $(this).attr("href"); /* [2] */

    //         if ( link.match("^#") ) { /* [3] */

    //             $(this).click(function() {
    //                 var target = $(link); /* [4] */ 
    //                 target = target.length ? target : $('[name=' + this.hash.slice(1) +']'); /* [4] */ 
    //                 if (target.length) {
    //                     $('html,body').animate({ /* [5] */ 
    //                         scrollTop: target.offset().top - 70  [5]  
    //                     }, 1000); return false; /* [5] */ 
    //                 }
    //             });

    //         } else if ( link.match("^mailto") ) { /* [6] */ 
    //             // Act as normal  /* [6] */ 
    //         } else {

    //             $(this).click(function(e) {
    //                 e.preventDefault(); /* [7] */ 
    //                 $('html').addClass('fadeSiteOut'); /* [8] */ 
    //                 setTimeout(function() { /* [9] */
    //                     window.location = link; /* [9] */
    //                 }, 800); /* [9] */
    //             });

    //         }

    //     }
    // });
  
});

/* -------------------------- */

/* jQuery */

$(document).ready(function() {

  //Implement the showing and hiding of the sidebar when the user clicks on #sidebar-button:
  $("#sidebar-button").click(function() {
    if ($(".sidebar-container").hasClass("sidebar-active")) {
      $("body").removeClass("no-scroll");
      $("#sidebar-button").removeClass("button-active");
      $(".sidebar-container").removeClass("sidebar-active");
      $(".rest").removeClass("wrapper-active");
      $("#title").removeClass("wrapper-active");
    } else {
      $("#sidebar-button").addClass("button-active");
      $(".sidebar-container").addClass("sidebar-active");
      $(".rest").addClass("wrapper-active");
      $("#title").addClass("wrapper-active");
      $("body").addClass("no-scroll");
    }
  });

});