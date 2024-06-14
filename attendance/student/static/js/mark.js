
  window.onload = function() {
      var presentRadios = document.querySelectorAll('input[type="radio"][value="present"]');
      var absentRadios = document.querySelectorAll('input[type="radio"][value="absent"]');
      var presentCountDisplay = document.getElementById('presentNumber');
      var attendance = {}; // To keep track of the attendance status of each student

      var presentCount = 0;

      // Initialize attendance object
      presentRadios.forEach(function(radio) {
          var studentId = radio.name.split('_')[1];
          attendance[studentId] = "absent";
      });

      // Event listeners for "Present" radio buttons
      presentRadios.forEach(function(radio) {
          var studentId = radio.name.split('_')[1];

          radio.addEventListener('change', function() {
              if (this.checked && attendance[studentId] === "absent") {
                  presentCount++;
                  attendance[studentId] = "present";
              } else if (!this.checked && attendance[studentId] === "present") {
                  presentCount--;
                  attendance[studentId] = "absent";
              }
              presentCountDisplay.value = presentCount >= 0 ? presentCount : 0;
          });
      });

      // Event listeners for "Absent" radio buttons
      absentRadios.forEach(function(radio) {
          var studentId = radio.name.split('_')[1];

          radio.addEventListener('change', function() {
              if (this.checked && attendance[studentId] === "present") {
                  presentCount--;
                  attendance[studentId] = "absent";
              } else if (!this.checked && attendance[studentId] === "absent") {
                  presentCount++;
                  attendance[studentId] = "present";
              }
              presentCountDisplay.value = presentCount >= 0 ? presentCount : 0;
          });
      });
  };


// On Submit Function  

function submitrecord(){
    document.getElementById('alertMessage').textContent = "Attendance Submitted Successfully";
    document.getElementById('alertBox').style.display = 'block';
  }