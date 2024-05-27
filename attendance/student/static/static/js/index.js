function loginFirst() {
    confirm("Please login to mark attendance.");
}


function showDepartments() {
    const semesterSelect = document.getElementById('department-select');
    const selectedSemester = semesterSelect.value;
    const departmentContainer = document.querySelector('.dep-cont');

    if (selectedSemester !== 'all') {
      departmentContainer.style.display = 'block';
    } else {
      departmentContainer.style.display = 'none';
    }
  }



