function get_status(channels, callback){
	// channels = '3,4'
	url = '/gpio'
	indata = {action: 'get', channels: channels}

	var genericResponseFunction = function (data, response){
	if (response === 'success') {
			console.log('Success: ')
		}
		else {
			console.log('Error: ')
		}
		console.log(data);
	}

	$.ajax({
		url: url,
		dataType: "json",
		success: genericResponseFunction,
		error: genericResponseFunction,
		data: indata
	});

}


function callServer(indata){
	if(typeof(indata) == 'undefined'){
		indata = {A: 'a', B: 'b'};
	}
	var genericResponseFunction = function (data, response) {
		if (response === 'success') {
			console.log('Success: ')
		}
		else {
			console.log('Error: ')
		}
		console.log(data)
	}

	$.ajax({
		url: "/data",
		dataType: "json",
		success: genericResponseFunction,
		error: genericResponseFunction,
		data: indata
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


	var initDone = true;
  
	
});