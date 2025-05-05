const wasteLog = [["Timestamp", "Item", "Weight (lbs)"]];

function dropItem(item, weight) {
  const timestamp = new Date().toLocaleString();
  wasteLog.push([timestamp, item, weight.toFixed(2)]);

  // Update status
  const status = document.getElementById("status");
  status.textContent = `✅ ${weight.toFixed(2)} lbs of ${item.toLowerCase()} thrown away`;

  // Update download link
  const downloadLink = document.getElementById("downloadLink");
  downloadLink.href = generateCSV(wasteLog);
  downloadLink.classList.remove("hidden");
}

function generateCSV(data) {
  const csvContent = data.map(row => row.join(",")).join("\n");
  const blob = new Blob([csvContent], { type: "text/csv" });
  return URL.createObjectURL(blob);
}
