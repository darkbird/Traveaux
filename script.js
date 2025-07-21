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

const popupContainer = document.getElementById("popup-container");
const resultSpan = document.getElementById("result");
const closePopupButton = document.getElementById("close-popup");

function spin() {
    const spinAngle = Math.random() * 10 + 10; // Random spin angle
    wheel.style.transition = "transform 3s ease-out";
    wheel.style.transform = `rotate(${spinAngle}rad)`;

    setTimeout(() => {
        const degrees = spinAngle * 180 / Math.PI % 360;
        const index = Math.floor((360 - degrees) / (360 / options.length));
        resultSpan.textContent = options[index];
        popupContainer.classList.remove("hidden");
        wheel.style.transition = "none";
        const actualAngle = spinAngle % (2 * Math.PI);
        wheel.style.transform = `rotate(${actualAngle}rad)`;
    }, 3000);
}

closePopupButton.addEventListener("click", () => {
    popupContainer.classList.add("hidden");
});

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
    options.forEach((option, index) => {
        const div = document.createElement("div");
        div.innerHTML = `
            <span class="option-text">${option}</span>
            <button class="delete-button" data-index="${index}">Supprimer</button>
        `;
        optionsList.appendChild(div);
    });

    document.querySelectorAll(".option-text").forEach((span, index) => {
        span.addEventListener("click", (e) => {
            const newText = prompt("Modifier l'option :", options[index]);
            if (newText) {
                options[index] = newText;
                drawWheel();
                updateOptionsList();
            }
        });
    });

    document.querySelectorAll(".delete-button").forEach(button => {
        button.addEventListener("click", (e) => {
            const index = e.target.getAttribute("data-index");
            options.splice(index, 1);
            arc = Math.PI / (options.length / 2);
            drawWheel();
            updateOptionsList();
        });
    });
}

spinButton.addEventListener("click", spin);
addOptionButton.addEventListener("click", addOption);

drawWheel();
updateOptionsList();
