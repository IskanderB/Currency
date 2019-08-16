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


var start_1 = true;         //Vars for change over inputs when it fill to click on string of table
var start_2 = false;



var inputs_2 = document.getElementsByTagName("tr");   //Get teg elements "tr"
	for (var i = 0; i < inputs_2.length; i++) {       //Search teg elements "tr" you clicked
	  inputs_2[i].addEventListener("click", myFunction_2);
	}

	function myFunction_2() {
		//var z=document.getElementById("first_cur");
		//z.innerHTML=this.id;
		
		if((start_2)&&(this.id)){         //Fill id input #second_cur currency cod you clicked 
		$('#second_cur').val(this.id);
		$("#second_cur").attr("placeholder", this.id);
		console.log(this.id)
		start_2 = false;
		start_1 = false;
	}
		else start_1 = true;
	    //alert(this.id);
	}



var inputs = document.getElementsByTagName("tr");
for (var i = 0; i < inputs.length; i++) {
  inputs[i].addEventListener("click", myFunction);
}

function myFunction() {
	//var z=document.getElementById("first_cur");
	//z.innerHTML=this.id;

	if((start_1)&&(this.id)){           //Fill id input #first_cur currency cod you clicked 
	$('#first_cur').val(this.id);
	$("#first_cur").attr("placeholder", this.id);
	console.log(this.id)
	start_2 = true;
}
    //alert(this.id);
    
}