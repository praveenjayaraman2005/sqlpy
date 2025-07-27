let totalAmount = 0;

function addExpense() {
  const descInput = document.getElementById("desc");
  const amountInput = document.getElementById("amount");

  const description = descInput.value.trim();
  const amount = Number(amountInput.value);

  if (description === "" || isNaN(amount) || amount <= 0) {
    alert("Please enter a valid description and amount");
    return;
  }

  const today = new Date();
  const day = today.getDate();
  const month = today.toLocaleString('default', { month: 'long' });

  const li = document.createElement("li");
  li.textContent = `${description}: ₹${amount} (${month} ${day})`;

  const delBtn = document.createElement("button");
  delBtn.textContent = "Delete";
  delBtn.onclick = () => {
    totalAmount -= amount;
    document.getElementById("total").textContent = totalAmount;
    li.remove();
  };

  li.appendChild(delBtn);
  document.getElementById("expenseList").appendChild(li);

  totalAmount += amount;
  document.getElementById("total").textContent = totalAmount;

  descInput.value = "";
  amountInput.value = "";
}

function clearAll() {
  document.getElementById("expenseList").innerHTML = "";
  totalAmount = 0;
  document.getElementById("total").textContent = totalAmount;
}
