// This is a basic JavaScript file.
// You can add code here for animations, form validation, etc.

console.log('Website is ready!');

// Example: Simple function to handle a click event
// const ctaButton = document.querySelector('.cta-button');
// ctaButton.addEventListener('click', () => {
//     alert('You clicked the CTA button!');
// });

document.addEventListener('DOMContentLoaded', () => {
    // ---- Back to Top Button Logic ----
    let mybutton = document.getElementById("backToTopBtn");

    if (mybutton) {
        window.onscroll = function () {
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
    faqQuestions.forEach(function (question) {
        question.addEventListener('click', function () {
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
        form.addEventListener('submit', function (event) {
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


document.addEventListener('DOMContentLoaded', () => {
    const fadeInElements = document.querySelectorAll('.fade-in');

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('show');
            }
        });
    });

    fadeInElements.forEach(element => {
        observer.observe(element);
    });
});


document.addEventListener('DOMContentLoaded', () => {
    const dropdownToggle = document.querySelector('.dropdown > a');
    const dropdownMenu = document.querySelector('.dropdown-menu');

    dropdownToggle.addEventListener('click', (e) => {
        e.preventDefault(); // Prevents the link from navigating
        dropdownMenu.classList.toggle('show');
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelectorAll('.hero-image');
    let currentSlide = 0;

    function nextSlide() {
        slides[currentSlide].classList.remove('active-slide');
        currentSlide = (currentSlide + 1) % slides.length;
        slides[currentSlide].classList.add('active-slide');
    }

    // Change slide every 5 seconds
    setInterval(nextSlide, 5000);
});


// Get the menu toggle button and the navigation list
const menuToggle = document.querySelector('.menu-toggle');
const navList = document.querySelector('nav ul');

// Add a click event listener to the button
menuToggle.addEventListener('click', () => {
    // Toggle a class on the navigation list to show/hide it
    navList.classList.toggle('active');
});



document.addEventListener('DOMContentLoaded', () => {
    const menuToggle = document.querySelector('.menu-toggle');
    const navMenu = document.querySelector('.nav-menu');

    menuToggle.addEventListener('click', () => {
        navMenu.classList.toggle('active');
    });
});