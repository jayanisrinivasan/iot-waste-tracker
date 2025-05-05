let wasteLog = [["Timestamp", "Item", "Weight (lbs)"]];

function dropBanana() {
  const weight = 0.18;
  const item = "Banana";
  const timestamp = new Date().toLocaleString();

  // Update waste log
  wasteLog.push([timestamp, item, weight]);

  // Show message
  const result = document.getElementById("result");
  result.textContent = `✅ ${weight.toFixed(2)} lbs of ${item.toLowerCase()} thrown away`;
  result.classList.remove("hidden");

  // Enable download
  const link = document.getElementById("downloadLink");
  link.href = createCSV(wasteLog);
  link.classList.remove("hidden");
}

function createCSV(data) {
  const csvRows = data.map(row => row.join(",")).join("\n");
  return URL.createObjectURL(new Blob([csvRows], { type: "text/csv" }));
}
