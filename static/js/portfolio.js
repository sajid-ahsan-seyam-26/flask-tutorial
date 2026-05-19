const menuBtn = document.getElementById("menuBtn");
const navLinks = document.getElementById("navLinks");
const typingText = document.getElementById("typingText");

menuBtn.addEventListener("click", () => {
  navLinks.classList.toggle("show");
});

const roles = ["Web Developer", "Flask Learner", "Frontend Designer"];
let roleIndex = 0;
let charIndex = 0;
let deleting = false;

function typingEffect() {
  let currentRole = roles[roleIndex];

  if (deleting) {
    typingText.textContent = currentRole.substring(0, charIndex - 1);
    charIndex--;
  } else {
    typingText.textContent = currentRole.substring(0, charIndex + 1);
    charIndex++;
  }

  if (!deleting && charIndex === currentRole.length) {
    deleting = true;
    setTimeout(typingEffect, 1000);
    return;
  }

  if (deleting && charIndex === 0) {
    deleting = false;
    roleIndex = (roleIndex + 1) % roles.length;
  }

  setTimeout(typingEffect, deleting ? 70 : 120);
}

typingEffect();

document.getElementById("contactForm").addEventListener("submit", function (e) {
  e.preventDefault();
  alert("Message sent successfully!");
});
