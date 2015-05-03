function callServer(){
	$.ajax({
		url: "/data",
		dataType: "json",
		success: function (msg) {
			console.log('success: ' + msg)
		},
		error: function (msg) {
			console.log('error: ' + msg)
		},
		data: {A: 'a', B: 'b'}
		});
}

$(function() {
	var initDone = false;
  $('#slider-1 input').switchButton({
  	checked: undefined,
		on_label:"Enabled",
		off_label:"Disabled",
		labels_placement: "right",
		on_callback: function(){
			console.log('slider-1 active');
			if (initDone) {
				$('#slider-2 input').switchButton('option', 'update', !$('#slider-2 input').switchButton('option', 'checked'));
				callServer()
			}
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

	var initDone = true;
  
	
});