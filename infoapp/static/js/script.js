const form = document.querySelector('#contact-form');
const firstNameField = document.querySelector('#id_firstname');
const lastNameField = document.querySelector('#id_lastname');
const emailField = document.querySelector('#id_email');
const phoneNumberField = document.querySelector('#id_phonenumber');
const messageField = document.querySelector('#id_message');

form.addEventListener('submit', function(event) {
  event.preventDefault();

  // Validate the input fields
  let isValid = true;

  if (firstNameField.value.trim() === '') {
    firstNameField.style.border = '2px solid red';
    isValid = false;
  } else {
    firstNameField.style.border = '2px solid green';
  }

  if (lastNameField.value.trim() === '') {
    lastNameField.style.border = '2px solid red';
    isValid = false;
  } else {
    lastNameField.style.border = '2px solid green';
  }

  if (emailField.value.trim() === '') {
    emailField.style.border = '2px solid red';
    isValid = false;
  } else {
    emailField.style.border = '2px solid green';
  }

  if (phoneNumberField.value.trim() === '') {
    phoneNumberField.style.border = '2px solid red';
    isValid = false;
  } else {
    phoneNumberField.style.border = '2px solid green';
  }

  if (messageField.value.trim() === '') {
    messageField.style.border = '2px solid red';
    isValid = false;
  } else {
    messageField.style.border = '2px solid green';
  }

  // Submit the form if all fields are valid
  if (isValid) {
    // document.getElementById('contact-form').addEventListener('submit', function() {
      document.getElementById('submit-icon').style.display = 'inline-block';
      document.getElementById('sub-btn').style.display = 'none';
      
        setTimeout(function() {
          document.getElementById('submit-icon').style.display = 'none';
          // document.getElementById('sub-btn').style.display = 'none';
        }, 10000)
      // });
      
      
    form.submit();

  }
});
var animation = bodymovin.loadAnimation({container: document.getElementById('animation'),
  // renderer: 'svg',
  loop: true,
  autoplay: true,
  path: 'user.json'
});




