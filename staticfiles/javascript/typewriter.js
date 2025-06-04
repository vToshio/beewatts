const el = document.querySelector('.typewriter')
const characters = el.innerHTML.length
const clone = el.cloneNode(true);

el.style.setProperty('--characters', characters)

const durationPerChar = 0.1; // segundos por caractere
const totalDuration = characters * durationPerChar;

el.style.animationDuration = `${totalDuration}s, 0.75s`;