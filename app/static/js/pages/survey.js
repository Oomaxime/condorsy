document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('survey-form');
  const addChoiceButton = document.getElementById('add-choice');
  const choicesContainer = document.getElementById('choices-container');

  addChoiceButton.addEventListener('click', () => {
    const newChoiceInput = document.createElement('input');
    newChoiceInput.type = 'text';
    newChoiceInput.name = 'choices[]';
    newChoiceInput.required = true;
    choicesContainer.querySelector('.choice-inputs').appendChild(newChoiceInput);
  });

  form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData(form);

    const data = {
      creator_id: 1,
      question: formData.get('question'),
      description: formData.get('description') || '',
      choices: [],
      start_date: formData.get('start_date'),
      end_date: formData.get('end_date'),
      algo: formData.get('algo'),
    };

    formData.getAll('choices[]').forEach(choice => {
      if (choice.trim() !== '') {
        data.choices.push(choice.trim());
      }
    });

    try {
      const response = await fetch('/api/createSurveys', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      const responseData = await response.json();

      if (response.status === 201) {
        alert(`Sondage créé avec succès ! ID: ${responseData.id}`);
        form.reset();
      } else {
        alert(`Erreur: ${responseData.error}`);
      }
    } catch (error) {
      console.error('Erreur lors de l\'envoi du formulaire:', error);
    }
  });
});
