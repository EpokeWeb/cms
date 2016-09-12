$(document).ready(function(){
    
    (function($) {
        "use strict";

    
    jQuery.validator.addMethod('answercheck', function (value, element) {
        return this.optional(element) || /^\bcat\b$/.test(value);
    }, "Inscrivez la bonne réponse.");

    // validate contactForm form
    $(function() {
        $('#contactForm').validate({
            rules: {
                contact_name: {
                    required: true,
                    minlength: 2
                },
                contact_email: {
                    required: true,
                    email: true
                },
                contact_url: {
                    required: true
                },
                addInfos: {
                    minlength: 50
                }
            },
            messages: {
                contact_name: {
                    required: "Inscrivez votre nom s'il-vous-plaît!",
                    minlength: "Votre nom doit avoir plus de deux caractères"
                },
                contact_email: {
                    required: "Il nous faut absolument votre courriel"
                },
                addInfos: {
                    required: "Il nous faut quelques mots ici!",
                    minlength: "Vous serez plus facile à comprendre avec davantage de mots!"
                },
            },
            submitHandler: function(form) {
                $(form).ajaxSubmit({
                    type:"POST",
                    data: $(form).serialize(),
                    url:"contact_process.php",
                    success: function() {
                        $('#contactForm :input').attr('disabled', 'disabled');
                        $('#contactForm').fadeTo( "slow", 0.15, function() {
                            $(this).find(':input').attr('disabled', 'disabled');
                            $(this).find('label').css('cursor','default');
                            $('#success').fadeIn();
                        })
                    },
                    error: function() {
                        $('#contactForm').fadeTo( "slow", 0.15, function() {
                            $('#error').fadeIn();
                        })
                    }
                })
            }
        })
    })
        
 })(jQuery)
});