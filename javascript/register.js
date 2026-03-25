function registerUser() {
  var name = $("#name").val();
  var email = $("#email").val();
  var password = $("#password").val();

  $.ajax({
    url: "http://localhost:5000/register",
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify({ name, email, password }),

    success: function () {
      alert("Registered Successfully");
      //redirect to login page after alert 
      window.location.href = "login.html";
    },

    error: function () {
      alert("Registration Failed");
    }
  });
}