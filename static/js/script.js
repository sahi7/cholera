const previousButton = document.querySelector('#prev')
const nextButton = document.querySelector('#next')
const submitButton = document.querySelector('#submit')
const tabTargets = document.querySelectorAll('.tab')
const tabPanels = document.querySelectorAll('.tabpanel')

var ques1 = document.getElementById("ques1").value
var ques2 = document.getElementById("ques2").value
var ques3 = document.getElementById("ques3").value
var ques4 = document.getElementById("ques4").value
var quantity1 = 0;
var quantity2 = 0;

const isEmpty = (str) => !str.trim().length
let currentStep = 0

// Validate first input on load
validateEntry()

document.getElementById("ques1").addEventListener("change", function() {
  if (ques1 === "no" ) {
    selectDiv.style.display = "none";
  } else {
    submitQuantity1()
  }
});

document.getElementById("ques2").addEventListener("change", function() {
  if (ques2 === "no") {
    selectDiv.style.display = "none";
  } else {
    submitQuantity2()
  }
});


// Next: Change UI relative to current step and account for button permissions
  nextButton.addEventListener('click', (event) => {
  event.preventDefault()

  // Hide current tab
  tabPanels[currentStep].classList.add('hidden')
  tabTargets[currentStep].classList.remove('active')

  // Show next tab
  tabPanels[currentStep + 1].classList.remove('hidden')
  tabTargets[currentStep + 1].classList.add('active')
  currentStep += 1
  
  validateEntry()
  updateStatusDisplay()
})

// Previous: Change UI relative to current step and account for button permissions
previousButton.addEventListener('click', (event) => {
  event.preventDefault()

  // Hide current tab
  tabPanels[currentStep].classList.add('hidden')
  tabTargets[currentStep].classList.remove('active')

  // Show previous tab
  tabPanels[currentStep - 1].classList.remove('hidden')
  tabTargets[currentStep - 1].classList.add('active')
  currentStep -= 1

  nextButton.removeAttribute('disabled')
  updateStatusDisplay()
})


function updateStatusDisplay() {
  // If on the last step, hide the next button and show submit
  if (currentStep === tabTargets.length - 1) {
    nextButton.classList.add('hidden')
    previousButton.classList.remove('hidden')
    submitButton.classList.remove('hidden')
    validateEntry()

    // If it's the first step hide the previous button
  } else if (currentStep == 0) {
    nextButton.classList.remove('hidden')
    previousButton.classList.add('hidden')
    submitButton.classList.add('hidden')
    // In all other instances display both buttons
  } else {
    nextButton.classList.remove('hidden')
    previousButton.classList.remove('hidden')
    submitButton.classList.add('hidden')
  }
}

function validateEntry() {
  document.addEventListener('DOMContentLoaded', function() {
  let input = tabPanels[currentStep].querySelector('.form-input')
  
  // Start but disabling continue button
  nextButton.setAttribute('disabled', true)
  submitButton.setAttribute('disabled', true)
  
  // Validate on initial function fire
  setButtonPermissions(input)
  
  // Validate on input
  input.addEventListener('input', () => setButtonPermissions(input))
  // Validate if bluring from input
  input.addEventListener('blur', () => setButtonPermissions(input))
});
  
}

function setButtonPermissions(input) {
  if (isEmpty(input.value)) {
    nextButton.setAttribute('disabled', true)
    submitButton.setAttribute('disabled', true)
  } else {
    nextButton.removeAttribute('disabled')
    submitButton.removeAttribute('disabled')
  }
}

function submitQuantity1() {
  if (document.getElementById("ques1").value === "yes") {
    quantity1 = prompt("How many times in the last 6 hours");
    if (quantity1 === null || quantity1 === "") {
      return; // Stop further execution if quantity is not provided
    }
  } 
}
function submitQuantity2() {
  if (document.getElementById("ques2").value === "yes") {
    while (true) {
      quantity2 = prompt("How many times have you vommited in the last 6 hours");
      if (quantity2 !== null && quantity2 !== "") {
        break;
      }
    }
  }
}
console.log("Submitted quantity:", quantity1);
console.log("Submitted quantity:", quantity2);