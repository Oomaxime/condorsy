document.addEventListener("DOMContentLoaded", async () => {
  const accountForm = document.getElementById("account-form");
  const user = JSON.parse(localStorage.getItem('user'));

  const deleteForm = document.getElementById("delete-form");

  try {
    const response = await fetch(`/api/account/${user.pseudo}`);
    if (!response.ok) {
      throw new Error("Erreur lors de la récupération des données de l'utilisateur");
    }

    const userData = await response.json();
    console.log(userData);
    accountForm.pseudo.value = userData.pseudo || '';
    accountForm.date_naissance.value = userData.date_of_birth || '';
    accountForm.addresse.value = userData.addresse || '';
    accountForm.job.value = userData.job || '';
    accountForm.mot_de_passe.value = userData.password || '';
  } catch (error) {
    console.error("Erreur lors de la récupération des données de l'utilisateur :", error);
  }

  accountForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    console.log("Soumission du formulaire capturée !");
    const pseudo = accountForm.pseudo.value;
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
          pseudo: user.pseudo,
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
      // window.location.href = "/account";
    } catch (error) {
      console.error("Erreur lors de la mise à jour du profil:", error);
    }
  });

  deleteForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const suppresion_c = confirm("Vous êtes sur le point de supprimer votre compte. Êtes-vous sûr de vouloir continuer ?");

    if (suppresion_c) {
      try {
        const response = await fetch("/api/account", {
          method: "DELETE",
          headers: {
            "Content-Type": "application/json",
            "Cache-Control": "no-cache",
          },
          body: JSON.stringify({
            pseudo: user.pseudo,
          }),
        });

        const data = await response.json();
        console.log("Compte supprimé avec succès:", data);
        localStorage.removeItem('user');
        window.location.href = "/";
      } catch (error) {
        console.error("Erreur lors de la suppression du compte:", error);
      }
    }
  });
});