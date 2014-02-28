$(function(){

	var universeStockPick = Backbone.Model.extend({

		initialize:  function(universe) {
			Ticker = universe.Symbol,
			Service = universe.Service,
			Direction = universe.Direction,
		};,
		localStorage: new Backbone.LocalStorage("universe"),
		
	});

	var universeStockPickView = Backbone.View.extend({

		tagName: "li",
		template: _.template($('#stock-pick').html()),
		initialize: function() {
	      this.listenTo(this.model, 'change', this.render);
	      this.listenTo(this.model, 'destroy', this.remove);
	    },

	});

	var App = new universeStockPickView;

});