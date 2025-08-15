// This is a basic JavaScript file.
// You can add code here for animations, form validation, etc.

console.log('Website is ready!');

// Example: Simple function to handle a click event
// const ctaButton = document.querySelector('.cta-button');
// ctaButton.addEventListener('click', () => {
//     alert('You clicked the CTA button!');
// });

// Get the button
let mybutton = document.getElementById("backToTopBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
mybutton.addEventListener("click", backToTop);

function backToTop() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

// This is the function that shows/hides the button
window.onscroll = function() {scrollFunction()};
// ...other JavaScript code...