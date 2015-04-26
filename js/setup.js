$(function() {
  $('#slider-1 input').switchButton({
  	checked: undefined,
		on_label:"Enable Visual Confirmation",
		off_label:"Enable Visual Confirmation",
		labels_placement: "left",
		on_callback: function(){
			console.log('slider-1 active');
		}
  });

  $('#slider-2 input').switchButton({
		on_label: "Visual Confirmation (On)",
		off_label:"Visual Confirmation (Off)",
		labels_placement: "right",
		on_callback: function(){
			console.log('slider-2 active');
		}
  });

  $('#slider-3 input').switchButton({
		on_label:"Enable Visual Confirmation",
		off_label:"Disable",
		labels_placement: "both"
  });


	
});