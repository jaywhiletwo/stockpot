$(function(){

    // model
	var UniverseStockPick = Backbone.Model.extend({
        // model stuff
	});
    
    var ItemView = Backbone.View.extend({
        initialize: function(item) {
            this.render(item);
        },

        el: $('#item_container'),

        render: function(item){
            var template = _.template( $('#item_template').html(), item );
            this.$el.html( template );
        },
    })

    var u = new UniverseStockPick({ticker: 'AAPL', service: 'Rule Breakers', direction: 'Long'});
    var v = new ItemView(u);
});
