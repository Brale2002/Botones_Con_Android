let counterValue = 0;
const addButton = document.getElementById("add");
const subtractButton = document.getElementById("subtract");
const counter = document.getElementById("counter");

addButton.addEventListener("click", () => {
  counterValue += 1;
  counter.innerText = counterValue;
});

subtractButton.addEventListener("click", () => {
  counterValue -= 1;
  counter.innerText = counterValue;
});
