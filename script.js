const wheel = document.getElementById("wheel");
const spinButton = document.getElementById("spin-button");
const addOptionButton = document.getElementById("add-option-button");
const optionsList = document.getElementById("options-list");
const ctx = wheel.getContext("2d");

let options = [
    { name: "Option 1", text: "Texte supplémentaire pour l'option 1" },
    { name: "Option 2", text: "Texte supplémentaire pour l'option 2" },
    { name: "Option 3", text: "Texte supplémentaire pour l'option 3" },
    { name: "Option 4", text: "Texte supplémentaire pour l'option 4" },
    { name: "Option 5", text: "Texte supplémentaire pour l'option 5" },
    { name: "Option 6", text: "Texte supplémentaire pour l'option 6" },
    { name: "Option 7", text: "Texte supplémentaire pour l'option 7" },
    { name: "Option 8", text: "Texte supplémentaire pour l'option 8" }
];
let colors = [
    "#FFC300", "#FF5733", "#C70039", "#900C3F",
    "#581845", "#DAF7A6", "#FFC300", "#FF5733"
];

let arc = Math.PI / (options.length / 2);

function drawWheel() {
    ctx.clearRect(0, 0, 400, 400);
    for (let i = 0; i < options.length; i++) {
        const angle = i * arc;
        ctx.beginPath();
        ctx.fillStyle = colors[i % colors.length];
        ctx.moveTo(200, 200);
        ctx.arc(200, 200, 200, angle, angle + arc);
        ctx.lineTo(200, 200);
        ctx.fill();

        ctx.save();
        ctx.fillStyle = "white";
        ctx.translate(200 + Math.cos(angle + arc / 2) * 150, 200 + Math.sin(angle + arc / 2) * 150);
        ctx.rotate(angle + arc / 2 + Math.PI / 2);
        ctx.fillText(options[i].name, -ctx.measureText(options[i].name).width / 2, 0);
        ctx.restore();
    }
}

const popupContainer = document.getElementById("popup-container");
const resultNameSpan = document.getElementById("result-name");
const resultTextP = document.getElementById("result-text");
const closePopupButton = document.getElementById("close-popup");

function spin() {
    const spinAngle = Math.random() * 10 + 10; // Random spin angle
    wheel.style.transition = "transform 3s ease-out";
    wheel.style.transform = `rotate(${spinAngle}rad)`;

    setTimeout(() => {
        const degrees = spinAngle * 180 / Math.PI % 360;
        const index = Math.floor((360 - degrees) / (360 / options.length));
        resultNameSpan.textContent = options[index].name;
        resultTextP.textContent = options[index].text;
        if (popupContainer) {
            popupContainer.classList.remove("hidden");
        }
        wheel.style.transition = "none";
        const actualAngle = spinAngle % (2 * Math.PI);
        wheel.style.transform = `rotate(${actualAngle}rad)`;
    }, 3000);
}

if (closePopupButton) {
    closePopupButton.addEventListener("click", () => {
        if (popupContainer) {
            popupContainer.classList.add("hidden");
        }
    });
}

const newOptionNameInput = document.getElementById("new-option-name");
const newOptionTextInput = document.getElementById("new-option-text");

function addOption() {
    const newOptionName = newOptionNameInput.value;
    const newOptionText = newOptionTextInput.value;
    if (newOptionName) {
        options.push({ name: newOptionName, text: newOptionText });
        arc = Math.PI / (options.length / 2);
        drawWheel();
        updateOptionsList();
        newOptionNameInput.value = "";
        newOptionTextInput.value = "";
    }
}

function updateOptionsList() {
    optionsList.innerHTML = "";
    options.forEach((option, index) => {
        const div = document.createElement("div");
        div.innerHTML = `
            <span class="option-text">${option.name}</span>
            <button class="delete-button" data-index="${index}">Supprimer</button>
        `;
        optionsList.appendChild(div);
    });

    document.querySelectorAll(".option-text").forEach((span, index) => {
        span.addEventListener("click", (e) => {
            const newName = prompt("Modifier le nom de l'option :", options[index].name);
            if (newName) {
                options[index].name = newName;
                const newText = prompt("Modifier le texte de l'option :", options[index].text);
                if (newText) {
                    options[index].text = newText;
                }
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
