// This is a basic JavaScript file.
// You can add code here for animations, form validation, etc.

console.log('Website is ready!');

// Example: Simple function to handle a click event
// const ctaButton = document.querySelector('.cta-button');
// ctaButton.addEventListener('click', () => {
//     alert('You clicked the CTA button!');
// });

// Get the button
//let mybutton = document.getElementById("backToTopBtn");

document.addEventListener('DOMContentLoaded', () => {
    let mybutton = document.getElementById("backToTopBtn");

    if (mybutton) {
        window.onscroll = function() {
            scrollFunction();
        };

        function scrollFunction() {
            if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
                mybutton.classList.add("show");
            } else {
                mybutton.classList.remove("show");
            }
        }

        mybutton.addEventListener("click", backToTop);

        function backToTop() {
            document.body.scrollTop = 0; // For Safari
            document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
        }
    }
});