async function solveCaptcha() {
  const input = document.getElementById("captchaInput");
  const file = input.files[0];
  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch("https://captcha-solver-xzm2.onrender.com/solve", {
    method: "POST",
    body: formData,
  });

  const data = await response.json();
  document.getElementById("result").textContent = "Solved CAPTCHA: " + data.text;
}
