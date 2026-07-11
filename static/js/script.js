// =========================================
// Smart Lender - script.js
// =========================================

// ------------------------------
// Mobile Navigation Toggle
// ------------------------------

const menuToggle = document.querySelector(".menu-toggle");
const navLinks = document.querySelector(".nav-links");

if (menuToggle && navLinks) {
    menuToggle.addEventListener("click", () => {
        navLinks.classList.toggle("active");
    });
}

// ------------------------------
// Close Mobile Menu on Link Click
// ------------------------------

const navItems = document.querySelectorAll(".nav-links a");

navItems.forEach(item => {
    item.addEventListener("click", () => {
        if (navLinks) {
            navLinks.classList.remove("active");
        }
    });
});

// ------------------------------
// Sticky Navbar Shadow
// ------------------------------

const navbar = document.querySelector(".navbar");

window.addEventListener("scroll", () => {

    if (!navbar) return;

    if (window.scrollY > 40) {
        navbar.classList.add("scrolled");
    } else {
        navbar.classList.remove("scrolled");
    }

});

// ------------------------------
// Loan Form Validation
// ------------------------------

const loanForm = document.getElementById("loanForm");

if (loanForm) {

    loanForm.addEventListener("submit", function (e) {

        const applicantIncome =
            parseFloat(document.querySelector('[name="applicant_income"]').value);

        const coApplicantIncome =
            parseFloat(document.querySelector('[name="coapplicant_income"]').value || 0);

        const loanAmount =
            parseFloat(document.querySelector('[name="loan_amount"]').value);

        const loanTerm =
            parseFloat(document.querySelector('[name="loan_term"]').value);

        const applicantName =
            document.querySelector('[name="name"]').value.trim();

        // --------------------------

        if (applicantName.length < 3) {

            alert("Applicant name must contain at least 3 characters.");

            e.preventDefault();

            return;
        }

        if (applicantIncome < 0) {

            alert("Applicant income cannot be negative.");

            e.preventDefault();

            return;
        }

        if (coApplicantIncome < 0) {

            alert("Co-applicant income cannot be negative.");

            e.preventDefault();

            return;
        }

        if (loanAmount <= 0) {

            alert("Loan amount must be greater than zero.");

            e.preventDefault();

            return;
        }

        if (loanTerm <= 0) {

            alert("Loan term must be greater than zero.");

            e.preventDefault();

            return;
        }

    });

}

// ------------------------------
// Input Animation
// ------------------------------

const inputs = document.querySelectorAll("input, select");

inputs.forEach(input => {

    input.addEventListener("focus", () => {

        input.parentElement.classList.add("focused");

    });

    input.addEventListener("blur", () => {

        input.parentElement.classList.remove("focused");

    });

});

// ------------------------------
// Smooth Scroll
// ------------------------------

document.querySelectorAll('a[href^="#"]').forEach(anchor => {

    anchor.addEventListener("click", function (e) {

        const target = document.querySelector(this.getAttribute("href"));

        if (target) {

            e.preventDefault();

            target.scrollIntoView({

                behavior: "smooth"

            });

        }

    });

});

// ------------------------------
// Button Ripple Effect
// ------------------------------

const buttons = document.querySelectorAll(".btn");

buttons.forEach(button => {

    button.addEventListener("click", function (e) {

        const circle = document.createElement("span");

        const diameter = Math.max(
            this.clientWidth,
            this.clientHeight
        );

        const radius = diameter / 2;

        circle.style.width = circle.style.height = `${diameter}px`;

        circle.style.left = `${e.clientX - this.offsetLeft - radius}px`;

        circle.style.top = `${e.clientY - this.offsetTop - radius}px`;

        circle.classList.add("ripple");

        const ripple = this.querySelector(".ripple");

        if (ripple) {

            ripple.remove();

        }

        this.appendChild(circle);

    });

});

// ------------------------------
// Fade-in Animation
// ------------------------------

const observer = new IntersectionObserver((entries) => {

    entries.forEach(entry => {

        if (entry.isIntersecting) {

            entry.target.classList.add("show");

        }

    });

}, {
    threshold: 0.15
});

document.querySelectorAll(".feature-card, .form-card, .result-card, .stats div")
    .forEach(el => observer.observe(el));

// ------------------------------
// Console Message
// ------------------------------

console.log("Smart Lender Frontend Loaded Successfully.");