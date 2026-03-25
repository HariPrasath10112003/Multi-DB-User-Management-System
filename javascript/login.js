function loginUser() {
  // taking email input value
  var email = $("#email").val();
  // taking password input value
  var password = $("#password").val();

  // sending ajax request to the backend 
  $.ajax({
    url: "http://localhost:5000/login",
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify({ email, password }),

    success: function () {
      alert("Login Success");

      // store session 
      localStorage.setItem("loggedIn", true);
      // redirect to profile page, if login success
      window.location.href = "profile.html";
    },
   //wrong login
    error: function () {
      alert("Invalid Credentials");
    }
  });
}