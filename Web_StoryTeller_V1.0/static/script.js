const loadingBarComponent = document.getElementById('myProgress')

function generateStory() {
    loadBar(30)
    const selectedTypes = [];
    const checkboxes = document.querySelectorAll('.checkbox-container input');
    checkboxes.forEach(checkbox => {
        if (checkbox.checked) {
            selectedTypes.push(checkbox.value);
        }
    });

    const storyLength = document.getElementById('storyLength').value;
    const userInstructions = document.getElementById('userInstructions').value;

    loadBarSpeed = {
        'Very Short': 30,
        'Short': 50,
        'Medium': 80,
        'Long': 100
    }
    console.log(loadBarSpeed[storyLength]);
    const storyRequest = {
        availableType: selectedTypes,
        storyLength: storyLength,
        userInstructions: userInstructions
    };

    // Send request to Flask server
    fetch('/generate-story', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(storyRequest),
        })
        .then(response => response.json())
        .then(data => {
            // Display the generated story
            document.getElementById('storyName').textContent = data.storyName;
            document.getElementById('storyContent').textContent = data.story;

            // Save the story to localStorage
            saveToHistory(data.storyName, data.story);
            loadingBarComponent.classList.add('hidden')

        })
        .catch(error => {
            console.error('Error generating story:', error);
            document.getElementById('storyName').textContent = 'Error generating story';
            document.getElementById('storyContent').textContent = 'Please try again later.';
        });
}

function saveToHistory(storyName, storyContent) {
    const history = JSON.parse(localStorage.getItem('storyHistory')) || [];

    const newStory = {
        name: storyName,
        content: storyContent
    };

    history.push(newStory);
    localStorage.setItem('storyHistory', JSON.stringify(history));

    // Update history list on the page
    displayHistory();
}

function displayHistory() {
    const history = JSON.parse(localStorage.getItem('storyHistory')) || [];
    const historyList = document.getElementById('historyList');

    historyList.innerHTML = ''; // Clear previous history list

    history.forEach((story, index) => {
        const storyItem = document.createElement('div');
        storyItem.classList.add('history-item');

        const storyName = document.createElement('span');
        storyName.textContent = story.name;
        storyItem.appendChild(storyName);

        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Delete';
        deleteButton.onclick = () => deleteStory(index);
        storyItem.appendChild(deleteButton);

        storyItem.onclick = () => loadStory(index);

        historyList.appendChild(storyItem);
    });
}

function deleteStory(index) {
    const history = JSON.parse(localStorage.getItem('storyHistory')) || [];
    history.splice(index, 1);
    localStorage.setItem('storyHistory', JSON.stringify(history));

    // Update history list
    displayHistory();
}

function loadStory(index) {
    const history = JSON.parse(localStorage.getItem('storyHistory')) || [];
    const story = history[index];
    document.getElementById('storyName').textContent = story.name;
    document.getElementById('storyContent').textContent = story.content;
}

function toggleGlow(checkbox) {
    const label = checkbox.closest('label');
    if (checkbox.checked) {
        label.classList.add('glow');
    } else {
        label.classList.remove('glow');
    }
}

function loadBar(speed) {
    loadingBarComponent.classList.remove('hidden')
    let width = 0;
    const progressBar = document.getElementById("myBar");

    function move() {
        if (width >= 100) {
            clearInterval(interval); // Stop once it reaches 100%
        } else {
            width++; // Increase width by 1 every second
            progressBar.style.width = width + "%"; // Update the width of the progress bar
        }
    }

    // Start the function
    const interval = setInterval(move, speed); // Run 'move' every second
}

window.onload = displayHistory;