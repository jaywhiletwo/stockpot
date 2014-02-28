var universeStockPick = Backbone.Model.extend({

	initialize:  function(universe) {
		Ticker: universe.Symbol,
		Service: universe.Service,
		Direction: universe.Direction,

	};,
	collection:  universes,
	localStorage: new Backbone.LocalStorage("universe"),
	
});

var universeStockPickView = Backbone.View.extend({

	tagName: "li",
	templase: _.template($('#stock-pick').html()),
	initialize: function() {
      this.listenTo(this.model, 'change', this.render);
      this.listenTo(this.model, 'destroy', this.remove);
    },

});