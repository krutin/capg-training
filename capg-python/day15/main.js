function saveToLocalStorage(event) {
  event.preventDefault();
  var first = document.getElementById("firstNameInput").value;
  var second = document.getElementById("lastNameInput").value;
  var email = document.getElementById("emailInput").value;
  var phone = document.getElementById("mobileInput").value;
  var gender = document.querySelector('input[name="gender"]:checked').value;
  var city = document.getElementById("city").value;
  var position = document.getElementById("positionInput").value;
  var startdate = document.getElementById("startDateInput").value;
  var interviewdate = document.getElementById("preferredInterviewDateInput").value;
  var time = document.getElementById("time_slots").value;
  var resume = document.getElementById("file-upload").value;

  var data = {
    firstName: first,
    lastName: second,
    email: email,
    phone: phone,
    gender: gender,
    city: city,
    position: position,
    startDate: startdate,
    interviewDate: interviewdate,
    time: time,
    resume: resume
};
  
  localStorage.setItem('applicationData', JSON.stringify(data));
  console.log("Data saved to local storage:");
  alert("You have successfully applied for fullstack developer job.")
  console.log(localStorage.getItem('applicationData'));
}

function updateFileName() {
  console.log("Updating file name...");
  const fileInput = document.getElementById("file-upload");
  const fileInfo = document.getElementById("file-info");

  if (fileInput.files.length > 0) {
      console.log("File selected:", fileInput.files[0].name);
      fileInfo.textContent = fileInput.files[0].name;
  } else {
      console.log("No file selected.");
      fileInfo.textContent = "No file selected";
  }
}
document.addEventListener("DOMContentLoaded", function() {
  

  const droparea = document.getElementById("file-label");
  const fileInput = document.getElementById("file-upload");

  droparea.addEventListener("dragover", function(e) {
      e.preventDefault();
  });

  droparea.addEventListener("drop", function(e) {
      e.preventDefault();
      fileInput.files = e.dataTransfer.files;
      updateFileName();
  });
});

function loadFirstNameFromLocalStorage() {
  var data = JSON.parse(localStorage.getItem('applicationData'));
 
  if (data && data.firstName) {
    document.getElementById("firstNameInput").value = data.firstName;
    }
  if (data.lastName && data) {
      document.getElementById("lastNameInput").value = data.lastName;
    }
  if (data && data.email) {
    document.getElementById("emailInput").value = data.email;
    }
    if (data && data.phone) {
      document.getElementById("mobileInput").value = data.phone;
  }
  if (data && data.gender) {
      var genderRadio = document.querySelector('input[name="gender"][value="' + data.gender + '"]');
      if (genderRadio) {
          genderRadio.checked = true;
      }
  }
  if (data && data.city) {
      document.getElementById("city").value = data.city;
  }
  if (data && data.position) {
      document.getElementById("positionInput").value = data.position;
  }
  if (data && data.startDate) {
      document.getElementById("startDateInput").value = data.startDate;
  }
  if (data && data.interviewDate) {
      document.getElementById("preferredInterviewDateInput").value = data.interviewDate;
  }
  if (data && data.time) {
      document.getElementById("time_slots").value = data.time;
  }
  if (data && data.resume) {
      var fileInfo = document.getElementById("file-info");
      fileInfo.textContent = data.resume.split('\\').pop(); // Extracts filename from the path
  }
    
  
}

function clear(){
  let session = sessionStorage.getItem('register');
  if(session == null){
    localStorage.clear();
  }
  sessionStorage.setItem('register', 1);

}


window.addEventListener('load',clear)

function validation(event){
  var firstname = document.getElementById("firstNameInput").value;
  var secondname = document.getElementById("lastNameInput").value;
  var emailval = document.getElementById("emailInput").value;
  var phoneval = document.getElementById("mobileInput").value;


  if (!/^[a-zA-Z\s]+$/.test(firstname)) {
    alert('First name must contain only alphabetic characters');
    return false;
  }

  if (secondname !== "" && !/^[a-zA-Z]+$/.test(secondname)) {
    alert('Last name must contain only alphabetic characters');
    return false;
  }

  if (emailval !== "" && !/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(emailval)) {
    alert('Invalid email address');
    return false;
  }

  if (phoneval !== "" && !/^\d{10}$/.test(phoneval)) {
    alert('Phone number must contain exactly 10 digits');
    return false;
  }
  saveToLocalStorage(event);
  return true;
}

window.addEventListener('load', loadFirstNameFromLocalStorage);



