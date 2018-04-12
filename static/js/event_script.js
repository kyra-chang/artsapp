/* Code inspired by W3Schools */

function heart(t){

        console.log(t)
        var likeUrl = t.dataset.href
        var tog = $("#heart")[0]
          $.ajax({
              url: likeUrl,
              method: "GET",
              data: {},
              success: function(data){
                if (tog.dataset.prefix == "fas"){
                  tog.dataset.prefix = "far"
                } else {
                  tog.dataset.prefix = "fas"
                }
              }, error: function(error){
                console.log(error)
              }
            })
       return false;


    };

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
    // $("#heart").click(function(event) {
    //   // Call `myFunc`
    //   event.preventDefault();
    //   heart(event.target)

    //   // Use `event` here at the event handler level, for instance
    //   event.stopPropagation();
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