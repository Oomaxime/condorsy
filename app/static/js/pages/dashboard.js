document.addEventListener("DOMContentLoaded", () => {
    // Graphique 1 : Les scrutins qui ont attiré le plus de participants
async function fetchTopSurveys() {
    try {
        const response = await fetch("http://localhost:5001/api/surveys/top");
        if (!response.ok) throw new Error(`HTTP Error: ${response.status}`);
        const data = await response.json();

        // Vérification du format attendu
        if (!Array.isArray(data)) throw new Error("La réponse attendue est un tableau.");
        console.log("Données des top surveys :", data);

            const labels = data.map(surveys => surveys.question);
            const participantCounts = data.map(surveys => surveys.participant_count);

            const ctx1 = document.getElementById('chartTopSurveys').getContext('2d');
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
    }
}

    // Graphique 2 : Répartition des votes par année de naissance
    const fetchSurveyVotesByBirthYear = async (surveysId) => {
        try {
            const response = await fetch(`/api/surveys/${surveysId}/votes-by-birth-year`);
            const data = await response.json();

            const labels = Object.keys(data);
            const voteCounts = Object.values(data).map(votes => votes.length);

            const ctx2 = document.getElementById('chartVotesByBirthYear').getContext('2d');
            new Chart(ctx2, {
                type: 'line',
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
    };

    // Ajouter un event listener pour le sélecteur de scrutin
    const surveySelector = document.getElementById('surveySelector');
    surveySelector.addEventListener('change', (event) => {
        const surveysId = event.target.value;
        if (surveysId) {
            fetchSurveyVotesByBirthYear(surveysId);
        }
    });

    // Charger la liste des scrutins dans le sélecteur
async function populateSurveySelector() {
    try {
        const response = await fetch("http://localhost:5001/api/surveys/top");
        if (!response.ok) throw new Error(`HTTP Error: ${response.status}`);
        const data = await response.json();

        if (!Array.isArray(data)) throw new Error("La réponse attendue est un tableau.");
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


    // Appels des fonctions pour charger les données et initialiser les graphiques
    fetchTopSurveys();
    populateSurveySelector();
    fetchAverageChoices();
});
