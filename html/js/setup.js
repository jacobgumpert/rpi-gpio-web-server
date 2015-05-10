function get_status(channels, callback){
	'use strict';
	// channels = '3,4'
	var url = '/gpio'
	var indata = {action: 'get', channels: channels}

	var genericResponseFunction = function (data, response){
	if (response === 'success') {
			console.log('Success: ')
			if(typeof(callback) == 'function'){
				callback(data);
			}
		}
		else {
			console.log('Error: ');
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


function set_status(channel, status, callback){
	// channels = '3,4'
	var url = '/gpio'
	var indata = {action: 'set', channel: channel, status: status}

	var genericResponseFunction = function (data, response){
	if (response === 'success') {
			console.log('Success: ');
			if(typeof(callback) == 'function'){
				callback(data);
			}
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

	get_status('3,5', function(data){

	  $('#slider-1 input').switchButton({
	  	checked: data[3] == 1,
			on_label:"Enabled",
			off_label:"Disabled",
			labels_placement: "right",
			on_callback: function(){
				console.log('slider-1 Enabled');
				if (initDone) {
					set_status(3, 1)
				}
			},
			off_callback: function(){
				console.log('slider-1 Disabled');
				if (initDone) {
					set_status(3, 0)
				}
			}
	  });

	  $('#slider-2 input').switchButton({
	  	checked: data[5] == 1,
	  	on_label:"Enabled",
	  	off_label:"Disabled",
			labels_placement: "right",
			on_callback: function(){
					console.log('slider-2 Enabled');
					if (initDone) {
						set_status(5, 1)
					}
				},
				off_callback: function(){
					console.log('slider-2 Disabled');
					if (initDone) {
						set_status(5, 0)
					}
				}
	  });
		initDone = true;
	 });
	
});