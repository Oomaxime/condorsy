<<<<<<< HEAD
<<<<<<< HEAD
=======
console.log("login.js est exécuté !");
>>>>>>> 73ef767 (merge a la mains)
=======
console.log("login.js est exécuté !");
>>>>>>> origin/7-préparation-requête-admin-uc10-11
document.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.getElementById("login-form");
  const errorDiv = document.querySelector(".form-error");

  loginForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    console.log("Soumission du formulaire capturée !");

    const pseudo = loginForm.pseudo.value;
    const password = loginForm.password.value;

    try {
      const response = await AuthService.login(pseudo, password);
      if (response.token) {
        window.location.href = "/home";
        console.log(response);
      }
    } catch (error) {
      console.error("Login error:", error);
      errorDiv.textContent = "Identifiants invalides";
      errorDiv.style.display = "block";
    }
  });
});
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> origin/7-préparation-requête-admin-uc10-11
document.addEventListener("DOMContentLoaded", () => {
  console.log("Page chargée et script chargé !");
  const loginForm = document.getElementById("login-form");
  if (!loginForm) {
    console.error("Formulaire de login introuvable !");
    return;
  }
<<<<<<< HEAD
});
>>>>>>> 73ef767 (merge a la mains)
=======
});
>>>>>>> origin/7-préparation-requête-admin-uc10-11
