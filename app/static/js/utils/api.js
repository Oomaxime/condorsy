// Utilitaire pour interagir avec l'API backend
const SurveyAPI = {
  // Récupérer tous les sondages
  async getSurveys() {
    try {
      const response = await fetch("/api/surveys");
      if (!response.ok)
        throw new Error("Erreur lors de la récupération des sondages");
      return await response.json();
    } catch (error) {
      console.error("Erreur API:", error);
      throw error;
    }
  },

  // Créer un nouveau sondage
  async createSurvey(surveyData) {
    try {
      const response = await fetch("/api/surveys", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(surveyData),
      });
      if (!response.ok)
        throw new Error("Erreur lors de la création du sondage");
      return await response.json();
    } catch (error) {
      console.error("Erreur API:", error);
      throw error;
    }
  },
};

// Exemple d'utilisation dans un formulaire de création de sondage
document.addEventListener("DOMContentLoaded", () => {
  const surveyForm = document.querySelector("#survey-form");
  if (surveyForm) {
    surveyForm.addEventListener("submit", async (e) => {
      e.preventDefault();

      // Récupération des données du formulaire
      const formData = new FormData(surveyForm);
      const surveyData = {
        question: formData.get("question"),
        description: formData.get("description"),
        choices: Array.from(formData.getAll("choices[]")),
      };

      try {
        // Appel à l'API pour créer le sondage
        const result = await SurveyAPI.createSurvey(surveyData);
        // Redirection vers le nouveau sondage
        window.location.href = `/surveys/${result.id}`;
      } catch (error) {
        // Affichage d'une erreur à l'utilisateur
        alert("Erreur lors de la création du sondage");
      }
    });
  }
});
