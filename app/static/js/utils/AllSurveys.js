document.addEventListener('DOMContentLoaded', () => {
    const surveysList = document.getElementById('surveys-list');

    async function fetchSurveys() {
        try {
            const token = getAuthToken();

            const response = await fetch('http://localhost:5001/api/surveys', {
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            });
            if (!response.ok) throw new Error(`HTTP Error: ${response.status}`);
            const surveys = await response.json();

            surveysList.innerHTML = '';

            if (surveys.length === 0) {
                surveysList.innerHTML = '<p>Aucun sondage disponible pour le moment.</p>';
                return;
            }

            surveys.forEach(survey => {
                const card = document.createElement('div');
                card.className = 'survey-card';

                card.innerHTML = `
                    <h2>${survey.question}</h2>
                    <p><strong>Algorithme :</strong> ${survey.algo}</p>
                    <p>${survey.description || 'Aucune description disponible.'}</p>
                    <p><strong>Date de création :</strong> ${survey.date.create}</p>
                    <p><strong>Débute le :</strong> ${survey.date.start}</p>
                    <p><strong>Se termine le :</strong> ${survey.date.end}</p>
                    <div class="choices">
                        ${survey.choix.map(choice => `
                            <button 
                                class="btn-choice" 
                                data-id="${survey.id}" 
                                data-choice="${choice}" 
                                ${survey.has_voted ? 'disabled' : ''}>
                                ${choice}
                            </button>
                        `).join('')}
                    </div>
                `;

                surveysList.appendChild(card);
            });

            addVoteEventListeners();
        } catch (error) {
            console.error('Erreur lors de la récupération des sondages :', error);
            surveysList.innerHTML = '<p>Une erreur est survenue lors du chargement des sondages.</p>';
        }
    }

    function addVoteEventListeners() {
        const choiceButtons = document.querySelectorAll('.btn-choice');
        choiceButtons.forEach(button => {
            button.addEventListener('click', async () => {
                const surveyId = button.getAttribute('data-id');
                const selectedChoice = button.getAttribute('data-choice');
                const token = getAuthToken();

                if (!token) {
                    alert('Vous devez être connecté pour voter.');
                    return;
                }

                try {
                    const response = await fetch('http://localhost:5001/api/vote', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'Authorization': `Bearer ${token}`
                        },
                        body: JSON.stringify({
                            id: surveyId,
                            data: { response: selectedChoice }
                        })
                    });

                    if (!response.ok) {
                        const errorData = await response.json();
                        alert(`Erreur : ${errorData.message || 'Une erreur est survenue.'}`);
                    } else {
                        alert('Votre vote a été enregistré avec succès !');

                        disableSurveyButtons(surveyId);
                    }
                } catch (error) {
                    console.error('Erreur lors de la participation au sondage :', error);
                    alert('Une erreur est survenue. Veuillez réessayer plus tard.');
                }
            });
        });
    }

    function disableSurveyButtons(surveyId) {
        const buttons = document.querySelectorAll(`.btn-choice[data-id="${surveyId}"]`);
        buttons.forEach(button => {
            button.disabled = true;
        });
    }

    function getAuthToken() {
        return localStorage.getItem('token');
    }

    fetchSurveys();
});
