import ChatBot, random, re, json, pyttsx3

def generateStory(userInstructions, chosenType, storyLength):
    gptInstructions = '''You are a expert Story teller. Whatever you say, will be spoken by a text to speech generator. You have to response in the following pattern:
"
<story-name> type the story name according to you <story-name-end>
<story> Write the acctual story as told <story-end>
"

You have to strict follow the pattern. You have to type the story name between <story-name> and <story-name-end>. And type the story between <story> and <story-end>.
'''
    availableType = ["Funny",
                 "Suspense",
                 "Thriller",
                 "Romance",
                 "Sci-Fi",
                 "Drama",
                 "Mystery",
                 "Horror",
                 "Action"]

    storyName = ""
    if not chosenType:
        for x in range(2):
            chosenType.append(availableType[random.randint(0, len(availableType)-1)])

    gptPrompt = f'Write a "{storyLength}" story of the type {chosenType}. The user instructions are: {userInstructions}.\nYour instructions are: {gptInstructions}'

    response = ChatBot.generateText(gptPrompt, True)

    storyNamePattern = r"<story-name>(.*?)<story-name-end>"
    storyPattern = r"<story>(.*?)<story-end>"

    storyName = re.findall(storyNamePattern, response, re.DOTALL)
    story = re.findall(storyPattern, response, re.DOTALL)

    if story: story = story[0]
    else: story = 'ERR 1024: No Response To Fetch'

    if storyName: storyName = storyName[0]
    else: storyName = "Story"
    
    return [storyName, story]

def saveJson(storyName, story):
    with open('storyHistory.json', "r") as file:
        try:
            existing_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = []  # If file is empty or not found, initialize an empty list

    data = {
        "name": storyName,
        "story": story,
        "primaryKey": ChatBot.generatePrimaryKey(20)
    }

    # Append the new story data to the existing data
    existing_data.append(data)

    # Write the updated data back to the file
    with open('storyHistory.json', "w") as updatedFile:
        json.dump(existing_data, updatedFile, indent=4)

def generateSound(story, speed, output_file):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Set the speech rate (speed) and volume
    engine.setProperty('rate', speed)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

    # Get available voices and set the voice (you can change the index if you want a different voice)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Use first voice (usually a female voice)

    # Save the speech to a file (output_file should be the full path and filename you want)
    engine.save_to_file(story, output_file)

    # Run the engine to process and save the file
    engine.runAndWait()

    print(f"Audio saved as {output_file}")