document.getElementById("captcha-form").addEventListener("submit", async function (e) {
  e.preventDefault();

  const fileInput = document.getElementById("image-input");
  const file = fileInput.files[0];
  if (!file) {
    alert("Please upload an image.");
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  try {
    const response = await fetch("https://https://captcha-solver-xzm2.onrender.com/solve", {
      method: "POST",
      body: formData
    });

    const result = await response.json();
    document.getElementById("result").innerText = result.text || "No text detected.";
  } catch (err) {
    document.getElementById("result").innerText = "Error: " + err.message;
  }
});
