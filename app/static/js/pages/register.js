document.addEventListener("DOMContentLoaded", () => {
  const registerForm = document.getElementById("register-form");
  const errorDiv = document.querySelector(".form-error");

  registerForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const pseudo = registerForm.pseudo.value;
    const password = registerForm.password.value;
    const password_confirm = registerForm.password_confirm.value;
    const date_of_birth = registerForm.date_of_birth.value;
    const job = registerForm.job.value;
    const addresse = registerForm.addresse.value;

    try {
      const response = await fetch("/api/register", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          pseudo,
          password,
          password_confirm,
          date_of_birth,
          job,
          addresse,
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || "Erreur lors de l'enregistrement");
      }

      const data = await response.json();

      window.location.href = "/";
      window.alert("Register success, you can now login");
    } catch (error) {
      errorDiv.textContent = error.message;
      errorDiv.style.display = "block";
    }
  });
});
