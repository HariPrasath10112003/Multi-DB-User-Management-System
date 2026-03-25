function updateProfile() {
  var age = $("#age").val();
  var dob = $("#dob").val();
  var contact = $("#contact").val();
  
  //for identification of mongodb to store updated values
  var email = localStorage.getItem("email");

  $.ajax({
    url: "http://localhost:5000/profile",
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify({ email, age, dob, contact }),

    // success- mongodb save
    success: function () {
      alert("Profile Updated");
    },
    error: function () {
      alert("Update Failed");
    }
  });
}