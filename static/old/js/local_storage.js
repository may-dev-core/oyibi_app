var usert;
var user_profile_data;
var user_account_data;

if(localStorage.getItem("user_data")){
	usert=JSON.parse(localStorage.getItem("user_data"));
}else{
	usert=null;

}

if(localStorage.getItem("user_profile_data")){
	user_profile_data=JSON.parse(localStorage.getItem("user_profile_data"));
}else{
	user_profile_data=null;

}

if(localStorage.getItem("user_account_data")){
	user_account_data=JSON.parse(localStorage.getItem("user_account_data"));
}else{
	user_account_data=null;

}


console.log(getLocalStorage());


function getBaseUrl() {
	var base_url="http://192.168.43.52:9000"; //local
	// var base_url="http://172.17.7.79:8000"; //local
  // var base_url="http://0.0.0.0:8000"; //local
	// var base_url="https://wcpapp.herokuapp.com";//heroku
	return base_url;
}


function getLocalStorage(){

	return usert;
}

function logOutUser(){

	localStorage.clear();

	return window.location.href = "/";
}


//user profile related data

var user_p_data;


function getUserName_ID() {
  // var data=data;

  $.ajax({
         type:"GET",
         // url:getBaseUrl()+"/api/v1/accounts/get_user_profile/",
         url:getBaseUrl()+"/api/v1/accounts/get_user_details/?q="+getEmail()+"",
         // url:getBaseUrl()+"/api/v1/accounts/get_user_profile/?q="+data+"",
         data: {},//JSON.stringify(data),//frm.serialize(),// JSON.stringify(data),
         dataType:"json",
         contentType: 'application/json',

         success: function(data){ //gone to the server and sever gives a response
          // console.log(data);
          // console.log(data.message);
          $('#message').html("<h5>" +data.message+"</h5>") 
         },


    }).done(function(data) {
      if (data.status_code==200) {
          // localStorage.setItem("user_profile_data",JSON.stringify(data));
          
            user_p_data=data;
            console.log(user_p_data);
            var firstname=String(user_p_data.data["first_name"]);
            var lastname= String(user_p_data.data["last_name"]);

            
            
            // console.log("Profile data ", user_p_data.data["other_names"]);
            


            $("#fullname").html(firstname+ " "+lastname);

            // var firstname=String(user_p_data.data["first_name"]);
            // var lastname= String(user_p_data.data["last_name"]);

            if($('input[name=first_name]').length && $('input[name=last_name]').length){
                console.log("i exist")
                document.getElementById("firstname").value = firstname;
                document.getElementById("lastname").value = lastname;


            }else{
               document.getElementById("referral_id").innerHTML=(user_p_data.data["referral_id"]);
            document.getElementById("id-num-referals").innerHTML=(user_p_data.data["number_of_referrals"]);
            document.getElementById("id-upline").innerHTML=(user_p_data.data["upline"]);
            document.getElementById("id-reg-date").innerHTML=(user_p_data.data["registration_date"]);
            }

          // window.location.href = "{% url 'dashboard' %}"
          // $('#success-modal-body').html(data.message);
          // $('#successfulPaymentModal').modal('show');
        }else {
          console.log(data);
          console.log("stop")
   //        user_p_data=data;
      // var firstname=String(user_p_data.data["first_name"]);
      // var lastname= String(user_p_data.data["last_name"]);
      // console.log("Profile data ", user_p_data.data["other_names"]);
      // document.getElementById("referral_id").append(user_p_data.data["referral_id"]);
      // document.getElementById("firstname").value = firstname;
      // document.getElementById("lastname").value = lastname;

      // $('#message').html("<h5>" +data.message+"</h5>") 
          // console.log(data);

          // window.location.href = data.url;
          // $( "#fail-modal-body" ).html( data.message);
          // $('#failedPaymentModal').modal('show');
        }
   });
    // return user_p_data;
    return false; //<---- move it here
}






function getUserProfileDetails() {
	// var data=data;

	$.ajax({
         type:"GET",
         // url:getBaseUrl()+"/api/v1/accounts/get_user_profile/",
         url:getBaseUrl()+"/api/v1/accounts/get_user_profile/?q="+getEmail()+"",
         // url:getBaseUrl()+"/api/v1/accounts/get_user_profile/?q="+data+"",
         data: {},//JSON.stringify(data),//frm.serialize(),// JSON.stringify(data),
         dataType:"json",
         contentType: 'application/json',

         success: function(data){ //gone to the server and sever gives a response
          // console.log(data);
          // console.log(data.message);
          $('#message').html("<h5>" +data.message+"</h5>");
          // $('.dropdown-btn').dropdown();
         },


    }).done(function(data) {
     	if (data.status_code==200) {
          // localStorage.setItem("user_profile_data",JSON.stringify(data));
          // console.log(localStorage)
          // console.log("Profile data ",data);
			user_p_data=data;
			

			document.getElementById("other_names").value = user_p_data.data["other_names"];
			document.getElementById("phone_number").value = user_p_data.data["phone_number"];
			document.getElementById("date_of_birth").value = user_p_data.data["date_of_birth"];
			document.getElementById("occupation").value = user_p_data.data["occupation"];
			document.getElementById("country").value = user_p_data.data["country"];
			document.getElementById("region").value = user_p_data.data["region"];
			document.getElementById("address").value = user_p_data.data["address"];
			document.getElementById("city").value = user_p_data.data["city"];
			document.getElementById("gender").value = user_p_data.data["gender"];
			document.getElementById("marital_status").value = user_p_data.data["marital_status"];

          // document.getElementById("firstname").value = getFirstName();
          // give to funtions here

          // window.location.href = "{% url 'dashboard' %}"
          // $('#success-modal-body').html(data.message);
          // $('#successfulPaymentModal').modal('show');
        }else {
          console.log("stop")
   //        user_p_data=data;
			// var firstname=String(user_p_data.data["first_name"]);
			// var lastname= String(user_p_data.data["last_name"]);
			// console.log("Profile data ", user_p_data.data["other_names"]);
			// document.getElementById("referral_id").append(user_p_data.data["referral_id"]);
			// document.getElementById("firstname").value = firstname;
			// document.getElementById("lastname").value = lastname;

			// $('#message').html("<h5>" +data.message+"</h5>") 
          // console.log(data);

          // window.location.href = data.url;
          // $( "#fail-modal-body" ).html( data.message);
          // $('#failedPaymentModal').modal('show');
        }
   });
    // return user_p_data;
    return false; //<---- move it here
}


//Account 

var user_acc_data;

function getUserAccountDetails() {
	 // var data=data;
	$.ajax({
         type:"GET",
         url:getBaseUrl()+"/api/v1/accounts/get_user_account/?q="+getEmail()+"",
         data: {},//JSON.stringify(data),//frm.serialize(),// JSON.stringify(data),
         dataType:"json",
         contentType: 'application/json',

         success: function(data){ //gone to the server and sever gives a response
          // console.log(data);
          // console.log(data.message);
          $('#accountmessage').html("<h5>" +data.message+"</h5>") 
         },


    }).done(function(data) {
      	if (data.status_code==200) {
          // localStorage.setItem("user_account_data",JSON.stringify(data));
          // console.log(localStorage)
         	user_acc_data=data;
         	document.getElementById("bank_account_name").value = user_acc_data.data["bank_account_name"];
		    document.getElementById("bank_account_number").value = user_acc_data.data["bank_account_number"];
		    document.getElementById("bank_name").value = user_acc_data.data["bank_name"];
		    document.getElementById("bank_branch").value = user_acc_data.data["bank_branch"];
		    document.getElementById("mobile_money_number").value = user_acc_data.data["mobile_money_number"];
		    document.getElementById("mobile_money_name").value = user_acc_data.data["mobile_money_name"];
		    document.getElementById("mobile_money_provider").value = user_acc_data.data["mobile_money_provider"];
	          // window.location.href = "{% url 'dashboard' %}"
	          // $('#success-modal-body').html(data.message);
	          // $('#successfulPaymentModal').modal('show');
	        }else {
	          console.log("stop")
	          // console.log(data);

	          // window.location.href = data.url;
	          // $( "#fail-modal-body" ).html( data.message);
	          // $('#failedPaymentModal').modal('show');
	        }
   	});
    return false; //<---- move it here
}





function getEmail() {
	if(usert==null){
    // $("#login").show();
    // $("#logout").hide();
    // document.getElementById("login").style.visibility = "visible";
    // document.getElementById("logout").style.visibility = "hidden";
		return window.location.href="/";
	}else{
		var email=usert;
     // document.getElementById("login").hide();
    // $("#logout").show();
		return email;
	}
}


function getEmailTrueFalse() {
  if(usert==null){
    return false;
    // return window.location.href="/";
  }else{
    var email=usert;
     // document.getElementById("login").hide();
    // $("#logout").show();
    return true;
  }
}

// console.log(getEmail());


function getPassword(pass, confirmPass) {
	if(pass==confirmPass){
        return true;
    }else{
    	return false;
    }

}



function updateUserAccountDetails(data) {
	var data=data;
	$.ajax({
         type:"PUT",
         url:getBaseUrl()+"/api/v1/accounts/edit_account_profile/",
         data: JSON.stringify(data),//frm.serialize(),// JSON.stringify(data),
         dataType:"json",
         contentType: 'application/json',

         success: function(data){ //gone to the server and sever gives a response
          // console.log(data);
          // console.log(data.message);
          $('#accountmessage').html("<h5>" +data.message+"</h5>");
          $('.dropdown-toggle').dropdown();
         },


    }).done(function(data) {
      if (data.status_code==200) {
          // localStorage.setItem("user_account_data",JSON.stringify(data));
          console.log("update successful")
          // window.location.href = "{% url 'dashboard' %}"
          // $('#success-modal-body').html(data.message);
          // $('#successfulPaymentModal').modal('show');
        }else {
          console.log("No data returned")
          // console.log(data);

          // window.location.href = data.url;
          // $( "#fail-modal-body" ).html( data.message);
          // $('#failedPaymentModal').modal('show');
        }
   });
    return false; //<---- move it here
}


function updateProfileDetails(data) {
	var data=data;

	console.log("posting...");
            console.log(data)

    $.ajax({
         type:"POST",
         url:"{% url 'dash_profile_details' %}",
         data: JSON.stringify(data),//frm.serialize(),// JSON.stringify(data),
         dataType:"json",
         contentType: 'application/json',
         headers: {
                    'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()
                    },

         success: function(data){ //gone to the server and sever gives a response
          console.log(data.message);
          $('#message').html("<h5>" +data.message+"</h5>") 
         },


    }).done(function(data) {
      console.log(data);
      if (data.status_code==200) {
          console.log("update successful");
          // window.location.href = "{% url 'dashboard' %}"
          // $('#success-modal-body').html(data.message);
          // $('#successfulPaymentModal').modal('show');
        }else {
          console.log("stop")
          // window.location.href = data.url;
          // $( "#fail-modal-body" ).html( data.message);
          // $('#failedPaymentModal').modal('show');
        }
   });
    return false; //<---- move it here

}


function getNeworkProfile(data) {
  var data={"email":getEmail()};

  console.log("posting...");
            console.log(data)

    $.ajax({
         type:"POST",
         url:getBaseUrl()+"/network_profile/",
         data:JSON.stringify({"email": "m"}),//frm.serialize(),// JSON.stringify(data),
         dataType:"json",
         contentType: 'application/json',

         success: function(data){ //gone to the server and sever gives a response
          // console.log(data.message);
          // $('#message').html("<h5>" +data.message+"</h5>") 
         },


    }).done(function(data) {
      // console.log(data);
      // if (data.status_code==200) {
      //     console.log("update successful");
      //     // window.location.href = "{% url 'dashboard' %}"
      //     // $('#success-modal-body').html(data.message);
      //     // $('#successfulPaymentModal').modal('show');
      //   }else {
      //     console.log("stop")
      //     // window.location.href = data.url;
      //     // $( "#fail-modal-body" ).html( data.message);
      //     // $('#failedPaymentModal').modal('show');
      //   }
   });
    return false; //<---- move it here

}











// {% load mptt_tags %}
// <ul>
   
//     <!-- {% full_tree_for_model userapp.NetworkProfile as genress  %} -->

//     {% recursetree network_profile %}
//         <li>
//             {{ node.user.email }} - <a href="">{{ node.user.first_name }} {{ node.user.last_name }}</a>
//             {% if not node.is_leaf_node %}
//                 <ul class="children">
//                     {{ children }}
//                 </ul>
//             {% endif %}
//         </li>
//     {% endrecursetree %}
// </ul>