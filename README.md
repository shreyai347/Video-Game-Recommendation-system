

# Video Game Recommendation System

This project implements a **video game recommendation system** based on user ratings using collaborative filtering techniques. The system is designed to recommend games to users based on their previous interactions with games in the dataset.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Video Game Recommendation System predicts and recommends games to users based on their historical ratings. It uses collaborative filtering to match similar users and games to generate personalized game recommendations.

## Features

- **Collaborative Filtering**: Recommends games by analyzing user-item interactions.
- **Cosine Similarity**: Computes game-to-game similarity.
- **Fuzzy String Matching**: Matches similar game titles when searching.
- **Web Interface**: Simple web interface built using Flask for user interaction.

## Technologies Used

- Python (pandas, numpy, scikit-learn)
- Flask (for the web interface)
- FuzzyWuzzy (for string matching)
- Cosine Similarity (for computing similarity between games)
- Jupyter Notebooks (for exploratory data analysis)
- HTML/CSS (for front-end)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/shreyai347/game-recommendation-system.git
   ```

2. Change into the project directory:

   ```bash
   cd game-recommendation-system
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:

   ```bash
   python app.py
   ```

## Usage

1. Open a web browser and go to `http://127.0.0.1:5000/`.
2. Enter a game title to search for recommendations.
3. The system will return a list of recommended games similar to the entered title based on user ratings.

## Dataset

The dataset consists of the following columns:
- **userId**: A unique identifier for each user.
- **game**: The name of the video game.
- **ratings**: The rating given by a user to a specific game.

## Project Structure

```
├── app.py                  # Flask app for the recommendation system
├── templates/              # HTML templates for the web pages
│   ├── index.html          # Main page
│   ├── recommendations.html # Recommendations page
│   └── no_output.html      # Page when no recommendation is found
├── static/                 # Static files (CSS, images, etc.)
├── model/                  # Contains precomputed models (if any)
├── data/                   # Dataset for training and testing
├── README.md               # Project documentation
└── requirements.txt        # List of dependencies
```

## Contributing

Feel free to fork this project and make your own changes. If you find any issues or have suggestions, please submit a pull request or open an issue in the GitHub repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

