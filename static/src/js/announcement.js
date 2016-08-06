openerp_announcement = function(instance) {
    instance.web.WebClient.include({
        show_application: function() {
            console.log("show application");
            return 
        },
        _ab_location: function(dbuuid) {
            console.log("ab location");
            return '';
        },
        show_annoucement_bar: function() {
            console.log("show annoucement bar");
           
           
        }
    });
};
