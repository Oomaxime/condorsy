// Graph front UC 11
document.addEventListener("DOMContentLoaded", () => {
    // Graphique 1 : Les scrutins qui ont attiré le plus de participants
async function fetchTopSurveys() {
    try {
        const response = await fetch("http://localhost:5001/api/surveys/top-participants");
        if (!response.ok) throw new Error(`HTTP Error: ${response.status}`);
        const data = await response.json();

        if (!Array.isArray(data)) throw new Error("La réponse attendue est un tableau.");
        console.log("Données des top surveys :", data);

        const labels = data.map(survey => survey.question);
        const participantCounts = data.map(survey => survey.participant_count);

        const ctx1 = document.getElementById('topSurveysChart').getContext('2d');
        new Chart(ctx1, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Nombre de participants',
                    data: participantCounts,
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: 'Scrutins avec le plus de participants'
                    }
                }
            }
        });
    } catch (error) {
        console.error("Erreur lors de la récupération des données des scrutins :", error);
        alert('Erreur lors de la récupération des données des scrutins : ' + error.message);
    }
}
// Graphique 2 : Répartition des votes par année de naissance
async function fetchSurveyVotesByBirthYear(surveyId) {
    try {
        const response = await fetch(`/api/surveys/${surveyId}/votes-by-birth-year`);
        const data = await response.json();

        console.log("Données récupérées : ", data); // (j'ai legit passer 5h sur ce graph et sa logique)

        // Vérif si un graph existe si oui le détruire puis le recréer
        if (window.birthYearVotesChart instanceof Chart) {
            window.birthYearVotesChart.destroy();
        }

        const labels = Object.keys(data); // Années de naissance
        const voteCounts = Object.values(data); // Nombre de votes

        const ctx2 = document.getElementById('birthYearVotesChart').getContext('2d');
        window.birthYearVotesChart = new Chart(ctx2, {
            type: 'pie',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Nombre de votes',
                    data: voteCounts,
                    backgroundColor: 'rgba(153, 102, 255, 0.2)',
                    borderColor: 'rgba(153, 102, 255, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: 'Répartition des votes par année de naissance'
                    }
                }
            }
        });
    } catch (error) {
        console.error('Erreur lors de la récupération des données des votes :', error);
    }
}

// Pour le sélect de survey
const surveySelector = document.getElementById('surveySelector');
surveySelector.addEventListener('change', (event) => {
    const surveyId = event.target.value; // Utiliser surveyId au lieu de surveysId
    if (surveyId) {
        fetchSurveyVotesByBirthYear(surveyId);
    }
});

// Charge la liste des surveys dans le sélect
async function populateSurveySelector() {
    try {
        const response = await fetch("http://localhost:5001/api/surveys/top-participants");
        const data = await response.json();

        const selector = document.getElementById("surveySelector");

        data.forEach(survey => {
            const option = document.createElement("option");
            option.value = survey._id;
            option.textContent = survey.question;
            selector.appendChild(option);
        });
    } catch (error) {
        console.error("Erreur lors de la récupération de la liste des scrutins :", error);
    }
}

    // Graphique 3 : Nombre moyen d'options par scrutin
async function fetchAverageChoices() {
    try {
        const response = await fetch("http://localhost:5001/api/surveys/average_choices");
        if (!response.ok) throw new Error(`HTTP Error: ${response.status}`);
        const data = await response.json();

        const canvas = document.getElementById("averageChoicesChart");
        if (!canvas) throw new Error("L'élément canvas pour les graphiques est introuvable.");
        const ctx = canvas.getContext("2d");

        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Moyenne'],
                datasets: [{
                    label: 'Nombre moyen d\'options',
                    data: [data.average_choices],
                    backgroundColor: ['rgba(75, 192, 192, 0.2)'],
                    borderColor: ['rgba(75, 192, 192, 1)'],
                    borderWidth: 1
                }]
            }
        });
    } catch (error) {
        console.error("Erreur lors de la récupération du nombre moyen d'options :", error);
    }
}


    // charge les datas et init les graph
    fetchTopSurveys();
    populateSurveySelector();
    fetchAverageChoices();
});

// recup et charge les surveys
async function fetchSurveys() {
    try {
        const response = await fetch('/api/surveys');
        const surveys = await response.json();

        const surveyList = document.getElementById('surveyList');
        surveyList.innerHTML = '';

        surveys.forEach(survey => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${survey.question}</td>
                <td>
                    <button onclick="deleteSurvey('${survey._id}')">Supprimer</button>
                </td>
            `;
            surveyList.appendChild(row);
        });
    } catch (error) {
        console.error('Erreur lors de la récupération des scrutins :', error);
    }
}

// Suppr un survey
async function deleteSurvey(surveyId) {
    if (confirm("Voulez-vous vraiment supprimer ce scrutin ?")) {
        try {
            const response = await fetch(`/api/surveys/delete?survey_id=${surveyId}`, {
                method: 'DELETE',
            });

            if (response.ok) {
                const data = await response.json();
                alert(data.message); // confirmation (?)
                fetchSurveys();
            } else {
                const errorData = await response.json();
                alert(errorData.error || "Erreur lors de la suppression.");
            }
        } catch (error) {
            console.error('Erreur lors de la suppression du scrutin :', error);
        }
    }
}

// ReCharge la liste des surveys
document.addEventListener('DOMContentLoaded', () => {
    fetchSurveys();
});
