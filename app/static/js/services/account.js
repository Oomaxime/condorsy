document.addEventListener("DOMContentLoaded", () => {
  const accountForm = document.getElementById("account-form");

  accountForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    console.log("Soumission du formulaire capturée !");

    const pseudo = localStorage.getItem('user');
    const date_naissance = accountForm.date_naissance.value;
    const addresse = accountForm.addresse.value;
    const job = accountForm.job.value;
    const mot_de_passe = accountForm.mot_de_passe.value;

    try {
      const response = await fetch("/api/account", {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          "Cache-Control": "no-cache",
        },
        body: JSON.stringify({
          pseudo,
          date_of_birth: date_naissance,
          addresse,
          job,
          password: mot_de_passe,
        }),
      });

      if (!response.ok) {
        throw new Error("Échec de la mise à jour du profil");
      }

      const data = await response.json();
      console.log("Profil mis à jour avec succès:", data);
      // window.location.href = "/";
    } catch (error) {
      console.error("Erreur lors de la mise à jour du profil:", error);
    }
  });
});