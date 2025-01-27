import App_Logic

availableType = ["Funny",
                 "Suspense",
                 "Thriller",
                 "Romance",
                 "Sci-Fi",
                 "Drama",
                 "Mystery",
                 "Horror",
                 "Action"]

chosenType = ['Romance']

storyLength = ['Very Short', 'Short', 'Medium', 'Long'][0]

userInstructions = 'I want it funny'

storyName, story = App_Logic.generateStory(userInstructions, chosenType, storyLength)