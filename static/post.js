/////////////////////////////
/// JavaScript for Posts page 
/////////////////////////////
$(function() {
    $('.js-menu-icon').click( function(){
        // $(this) : self element, namely div.js-menu-icon
        $(this).next().toggle()
    } )
})