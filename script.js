// This is a basic JavaScript file.
// You can add code here for animations, form validation, etc.

console.log('Website is ready!');

// Example: Simple function to handle a click event
// const ctaButton = document.querySelector('.cta-button');
// ctaButton.addEventListener('click', () => {
//     alert('You clicked the CTA button!');
// });

// Get the button
document.addEventListener('DOMContentLoaded', () => {
    // ---- Back to Top Button Logic ----
    let mybutton = document.getElementById("backToTopBtn");

    if (mybutton) {
        window.onscroll = function() {
            if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
                mybutton.classList.add("show");
            } else {
                mybutton.classList.remove("show");
            }
        };

        mybutton.addEventListener("click", () => {
            document.body.scrollTop = 0;
            document.documentElement.scrollTop = 0;
        });
    }

    // ---- FAQ Accordion Logic ----
    let faqQuestions = document.querySelectorAll('.faq-question');
    faqQuestions.forEach(function(question) {
        question.addEventListener('click', function() {
            let answer = this.nextElementSibling;
            if (answer.style.maxHeight) {
                answer.style.maxHeight = null;
            } else {
                answer.style.maxHeight = answer.scrollHeight + 'px';
            }
        });
    });

    // ---- Contact Form Validation Logic ----
    let form = document.getElementById('contactForm');
    if (form) {
        form.addEventListener('submit', function(event) {
            let name = document.getElementById('name');
            let email = document.getElementById('email');
            let message = document.getElementById('message');

            if (name.value.trim() === '' || email.value.trim() === '' || message.value.trim() === '') {
                alert('Please fill in all fields before sending your message.');
                event.preventDefault();
            }
        });
    }
});

document.addEventListener('DOMContentLoaded', function() {
    let faqQuestions = document.querySelectorAll('.faq-question');

    faqQuestions.forEach(function(question) {
        question.addEventListener('click', function() {
            let answer = this.nextElementSibling;
            
            // Check if the answer is currently visible
            if (answer.style.maxHeight) {
                // If it is, collapse it
                answer.style.maxHeight = null;
            } else {
                // If not, expand it
                answer.style.maxHeight = answer.scrollHeight + 'px';
            }
        });
    });
});


document.addEventListener('DOMContentLoaded', function() {
    let form = document.getElementById('contactForm');

    form.addEventListener('submit', function(event) {
        let name = document.getElementById('name');
        let email = document.getElementById('email');
        let message = document.getElementById('message');

        // Check if all fields are filled
        if (name.value === '' || email.value === '' || message.value === '') {
            alert('Please fill in all fields before sending your message.');
            event.preventDefault(); // Stop the form from submitting
        }
    });
});