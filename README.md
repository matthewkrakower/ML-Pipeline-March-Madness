# ML March Madness Pipeline

There are four tasks in this pipeline, all falling in the folder ```preprocess_train_predict_scripts```. The folder ```dags```, defined by the file ```instructions.py``` inside of it, directs Apache Airflow to run the DAG accordingly. Currently, the scheduled runs are set to none (```schedule_interval=None```) because does not need to run automatically in its current state. This could be easily changed to occur every X seconds, minutes, hours, etc. The end goal is to predict how many rounds each team will advance in March Madness. This is done using the target column 'Winner', which is filled out so that every win in the tournament is an increase of 1/6. Teams that won zero games have a value of 0, one game (Round of 32) have a value of 1/6, ..., five games have a value of 5/6 (Finals Runner-Up), and six games have a value of 1 (Champion).

## docker-compose.yaml
Defines how Airflow runs in containers by configuring shared settings, volumes, and services-airflow-init (DB/user setup), airflow-webserver (UI), airflow-scheduler (task execution), and airflow-cli (command line access).

## Dockerfile
Builds a custom Airflow image by installing dependencies from requirements.txt and baking in the DAG and preprocessing scripts so they’re always available in the container.

# Below are the four tasks:

## Task 1: preprocess_training.py
This script does the preprocessing for the raw data file ```MM_KP.csv```, pulled directly from KenPom. This includes all KenPom metrics for every year back to its creation in 2002. The script cleans the file, feature engineers new columns like 'Tourney Seed' or 'Win Percentage', and manually fills the target column 'Winner'. The file also has code that calculates correlations between features and targets, along with covariance between features. The training/testing dataset uses only features that have a correlation magnitude with the target of 0.1 or higher. Additionally, for any pair of features with a correlation magnitude at or above 0.8, I dropped the feature that has the weaker correlation with the target variable. Until next year's March Madness bracket is announced, 2002-2024 is used for training, and 2025 is used as the test. 

## Task 2: train.py
This script trains and tunes an XGBoost model on March Madness data using ```RandomizedSearchCV```, validates it with repeated k-fold cross-validation, evaluates performance metrics, saves the best model with joblib, and verifies the saved model by reloading it and making predictions. It also scales all features accordingly.

## Task 3: preprocess_test.py
This script has the same function as ```preprocess_training.py```, preprocessing only for 2025. 

## Task 4: predict.py
This script extracts the model that was trained in the second task and predicts on the test set. It saves the output predictions as ```predictions.csv``` in the ```results``` folder. 

# Run The Application
Assuming the user already has Docker installed, run the following commands in order:
```
- docker compose down -v --remove-orphans   # OPTIONAL IF USER HAS NO CONTAINERS RUNNING: Cleans up any existing containers, networks, and volumes 
- docker compose build                      # Builds the Docker images defined in your Dockerfile  
- docker compose run --rm airflow-init      # Initializes Airflow (sets up the database and create the default user)  
- docker compose up -d airflow-webserver airflow-scheduler   # Starts the Airflow webserver and scheduler in the background  
- docker compose exec airflow-scheduler airflow db check     # Verifies the Airflow database is initialized correctly  
- docker compose exec airflow-scheduler airflow dags list    # Lists available DAGs  
- docker compose exec airflow-scheduler airflow dags list-import-errors  # Checks for any DAG import issues  
- docker compose exec airflow-scheduler airflow dags trigger march_madness_predictions   # Triggers the DAG manually  
- docker compose logs -f airflow-scheduler  # Streams the logs from the scheduler in real time
```

Once the containers are up, the user can access the Airflow UI at http://localhost:8080. The username is march and password is madness. 

<img width="1506" height="810" alt="Image" src="https://github.com/user-attachments/assets/d3ace428-37f2-4e07-931c-0b611d3aefc0" />
