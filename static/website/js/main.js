$(document).ready(function() {
    $(document).on("click", "#login-submit", function(e) {
        Dajaxice.website.user_login(Dajax.process, {form: $("#login-form").serialize(true)});
        e.preventDefault();
    });

    $(document).on("click", "#register-submit", function(e) {
        Dajaxice.website.user_register(Dajax.process, {form: $("#register-form").serialize(true)});
        e.preventDefault();
    });

    $(document).on("click", "#logout", function(e) {
        Dajaxice.website.user_logout(Dajax.process);
        e.preventDefault();
    });
});

$('#sidebar .nav-group').affix({
  offset: {
    top: 200
  }
});

$('.descp').tooltip();
$(".descp").click(function(e) { e.preventDefault();});

$("body").scrollspy({
    target: '#sidebar',
    offset: 30
}); 
