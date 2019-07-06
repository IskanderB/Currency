// Ajax-request for convert currensy 
$("#button_convert").click(function() {//Ajax-request run, when user click on button with id = "button_convert"
	$.ajax({
	type: "GET",// Data in GET
	url: "give_result",//Python function in view.py for processing data
	data: {
		"first_cur": $("#first_cur").val(),//Data from input with id = "first_cur"
		"second_cur": $("#second_cur").val(),
		"first_par_form": $("#first_par_form").val()
	},
	dataType: "text",
	cache: false,
	success: function (data) {//Answer
		var z=document.getElementById("result");//In value "z" put html-tag with id = "result"
		z.innerHTML=data;//In html-tag put value data
	}
	});
});
// Ajax-request for follow 
$("#button_follow").click(function() {
	$.ajax({
	type: "GET",
	url: "user_follow",
	data: {
		"user_email": $("#user_email").val(),
		"user_name": $("#user_name").val(),
	},
	dataType: "text",
	cache: false,
	success: function (data) {
		var z=document.getElementById("answer");
		z.innerHTML=data;
	}
	});
});
