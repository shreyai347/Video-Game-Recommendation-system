from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the similarity matrix
game_similarity_df = pd.read_pickle('game_similarity_df.pkl')  # Save similarity matrix to a pickle file from the notebook

# Function to recommend games
def recommend_games(game_name, similarity_matrix, num_recommendations=5):
    if game_name not in similarity_matrix.index:
        return f"Game '{game_name}' not found in the dataset!"
    
    # Sort by similarity scores
    similar_games = similarity_matrix[game_name].sort_values(ascending=False)[1:num_recommendations+1]
    return similar_games.index.tolist()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    game_name = request.form['game_name']
    recommendations = recommend_games(game_name, game_similarity_df)
    if isinstance(recommendations, list):
        return render_template('recommendations.html', recommendations=recommendations, game=game_name)
    else:
        return render_template('no_output.html', message=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
