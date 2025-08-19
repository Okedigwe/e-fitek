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
    const dropdowns = document.querySelectorAll('.dropdown > a');
    dropdowns.forEach(dropdown => {
        dropdown.addEventListener('click', (e) => {
            // This prevents the link from navigating away
            e.preventDefault();

            // This toggles the 'active' class on the parent <li> element
            const parentLi = dropdown.parentElement;
            parentLi.classList.toggle('active');

            // This ensures only one dropdown is open at a time
            document.querySelectorAll('.dropdown.active').forEach(item => {
                if (item !== parentLi) {
                    item.classList.remove('active');
                }
            });
        });
    });
});







// Function to show the correct service section based on URL hash
function showServiceSection() {
    const hash = window.location.hash;
    const allSections = document.querySelectorAll('.service-content');
    const defaultSection = document.getElementById('default-intro');

    // Hide all sections first
    allSections.forEach(section => {
        section.classList.remove('active-content');
    });

    // Show the section that matches the hash, or the default section if no hash
    if (hash) {
        const targetSection = document.querySelector(hash);
        if (targetSection) {
            targetSection.classList.add('active-content');
        } else {
            defaultSection.classList.add('active-content');
        }
    } else {
        defaultSection.classList.add('active-content');
    }
}

// Event listener for when the page loads
window.addEventListener('DOMContentLoaded', () => {
    // Show the correct section on initial load
    showServiceSection();

    // Event listener for hash changes (when a user navigates between sections)
    window.addEventListener('hashchange', showServiceSection);
});






// ''''''''''''''''''''''''''''''''''''''''
document.addEventListener('DOMContentLoaded', () => {

    // Back to Top Button Logic
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

    // FAQ Accordion Logic
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

    // Hero Slideshow Logic
    const slides = document.querySelectorAll('.hero-image');
    let currentSlide = 0;
    function nextSlide() {
        if (slides.length === 0) return;
        slides[currentSlide].classList.remove('active-slide');
        currentSlide = (currentSlide + 1) % slides.length;
        slides[currentSlide].classList.add('active-slide');
    }
    if (slides.length > 1) {
        setInterval(nextSlide, 5000);
    }

    // Dynamic Service Page Logic
    const serviceLinks = document.querySelectorAll('.service-cards-container a, .service-content a');
    const serviceSections = document.querySelectorAll('.service-details-container .service-content');
    const backToServicesBtn = document.getElementById('back-to-services-btn');
    const servicesLanding = document.getElementById('services-landing');

    // This is the core part that makes content appear.
    serviceLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            const targetId = link.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);

            // Check if the target section is a service detail section
            if (targetSection && targetSection.classList.contains('service-content')) {
                e.preventDefault();

                // Hide all sections
                serviceSections.forEach(section => {
                    section.classList.remove('active-content');
                });

                // Add active class to the target section
                targetSection.classList.add('active-content');
                // Scroll to the details container for a smooth transition
                targetSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // "Back to Services" button logic
    if (backToServicesBtn) {
        backToServicesBtn.addEventListener('click', () => {
            // Hide all content sections
            serviceSections.forEach(section => {
                section.classList.remove('active-content');
            });
            // Show the default intro
            document.getElementById('default-intro').classList.add('active-content');
            // Scroll back to the top of the service cards
            servicesLanding.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
    }
});













// This is the correct line to select all service cards
const serviceCards = document.querySelectorAll('body.services-page main .');

// This code then loops through each card to add the click event listener
serviceCards.forEach(card => {
    card.addEventListener('click', () => {
        // ... (your logic for showing content)
    });
});