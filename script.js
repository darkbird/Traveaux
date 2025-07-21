const wheel = document.getElementById("wheel");
const spinButton = document.getElementById("spin-button");
const newOptionInput = document.getElementById("new-option");
const addOptionButton = document.getElementById("add-option-button");
const optionsList = document.getElementById("options-list");
const ctx = wheel.getContext("2d");

let options = [
    "Option 1", "Option 2", "Option 3", "Option 4",
    "Option 5", "Option 6", "Option 7", "Option 8"
];
let colors = [
    "#FFC300", "#FF5733", "#C70039", "#900C3F",
    "#581845", "#DAF7A6", "#FFC300", "#FF5733"
];

let arc = Math.PI / (options.length / 2);

function drawWheel() {
    ctx.clearRect(0, 0, 500, 500);
    for (let i = 0; i < options.length; i++) {
        const angle = i * arc;
        ctx.beginPath();
        ctx.fillStyle = colors[i % colors.length];
        ctx.moveTo(250, 250);
        ctx.arc(250, 250, 250, angle, angle + arc);
        ctx.lineTo(250, 250);
        ctx.fill();

        ctx.save();
        ctx.fillStyle = "white";
        ctx.translate(250 + Math.cos(angle + arc / 2) * 200, 250 + Math.sin(angle + arc / 2) * 200);
        ctx.rotate(angle + arc / 2 + Math.PI / 2);
        ctx.fillText(options[i], -ctx.measureText(options[i]).width / 2, 0);
        ctx.restore();
    }
}

function spin() {
    const spinAngle = Math.random() * 10 + 10; // Random spin angle
    wheel.style.transition = "transform 3s ease-out";
    wheel.style.transform = `rotate(${spinAngle}rad)`;

    setTimeout(() => {
        const degrees = spinAngle * 180 / Math.PI % 360;
        const index = Math.floor((360 - degrees) / (360 / options.length));
        alert(`Vous avez gagné : ${options[index]}`);
        wheel.style.transition = "none";
        const actualAngle = spinAngle % (2 * Math.PI);
        wheel.style.transform = `rotate(${actualAngle}rad)`;
    }, 3000);
}

function addOption() {
    const newOption = newOptionInput.value;
    if (newOption) {
        options.push(newOption);
        arc = Math.PI / (options.length / 2);
        drawWheel();
        updateOptionsList();
        newOptionInput.value = "";
    }
}

function updateOptionsList() {
    optionsList.innerHTML = "";
    options.forEach(option => {
        const div = document.createElement("div");
        div.textContent = option;
        optionsList.appendChild(div);
    });
}

spinButton.addEventListener("click", spin);
addOptionButton.addEventListener("click", addOption);

drawWheel();
updateOptionsList();
