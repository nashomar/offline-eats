// Show current date
document.getElementById('date').textContent = 'Today: ' + new Date().toDateString();

// Load stored items
const foodList = JSON.parse(localStorage.getItem('foods')) || [];
const listElement = document.getElementById('foodList');

foodList.forEach(item => {
  const li = document.createElement('li');
  li.textContent = item;
  listElement.appendChild(li);
});

function addFood() {
  const input = document.getElementById('foodInput');
  const food = input.value.trim();
  if (food) {
    foodList.push(food);
    localStorage.setItem('foods', JSON.stringify(foodList));

    const li = document.createElement('li');
    li.textContent = food;
    listElement.appendChild(li);
    input.value = '';
  }
}
