function toggleRegistration() {
    var registrationDiv = document.getElementById('registration-div');
    var enterDiv = document.getElementById('enter-div');
  
    registrationDiv.style.display = 'flex';
    enterDiv.style.display = 'none';
}
  
function toggleEnter() {
    var registrationDiv = document.getElementById('registration-div');
    var enterDiv = document.getElementById('enter-div');
  
    registrationDiv.style.display = 'none';
    enterDiv.style.display = 'flex';
}

function createUser() {
    var email = document.getElementById('email-input').value;
    var nickname = document.getElementById('nickname-input').value;
    var password = document.getElementById('password-input').value;
    var repeatPassword = document.getElementById('repeat-password-input').value;
    var dob = document.getElementById('dob-input').value;
    var sex = document.querySelector('input[name="radiobutton"]:checked').value;
    
    // Perform form validation
    if (!email || !nickname || !password || !repeatPassword || !dob) {
      alert('Please fill in all required fields.');
      return;
    }
  
    // Validate email format using regular expression
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      alert('Please enter a valid email.');
      return;
    }
  
    // Check if passwords match
    if (password !== repeatPassword) {
      alert('Passwords do not match.');
      return;
    }
  
    // Send an AJAX request to create a new user
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/create_user');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function () {
      if (xhr.status === 200) {
        alert('User created successfully!');
        resetRegistrationForm();
      } else {
        alert('Error creating user.');
      }
    };
    xhr.send(JSON.stringify({ email, nickname, password, dob, sex }));
}
  
function resetRegistrationForm() {
    document.getElementById('email-input').value = '';
    document.getElementById('nickname-input').value = '';
    document.getElementById('password-input').value = '';
    document.getElementById('repeat-password-input').value = '';
    document.getElementById('dob-input').value = '';
    document.querySelector('input[name="radiobutton"][value="Other"]').checked = true;
}
  