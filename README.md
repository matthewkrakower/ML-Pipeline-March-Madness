# ML March Madness Pipeline

There are four tasks in this pipeline, all falling in the folder ```preprocess_train_predict_scripts```. The folder ```dags```, defined by the file ```instructions.py``` inside of it, directs Apache Airflow to run the DAG accordingly. The scheduled runs are set to take place every year on March 17th, the day after Selection Sunday and the day before the tournament starts. The end goal is to predict how many rounds each team will advance in March Madness. This is done using the target column 'Winner', which is manually (and painfully) filled out so that every win in the tournament is an increase of 1/6. Teams that won zero games have a value of 0, one game (Round of 32) have a value of 1/6, ..., five games have a value of 5/6 (Finals Runner-Up), and six games have a value of 1 (Champion).

## docker-compose.yaml
Defines how Airflow runs in containers by configuring shared settings, volumes, and services-airflow-init (DB/user setup), airflow-webserver (UI), airflow-scheduler (task execution), and airflow-cli (command line access).

## Dockerfile
Builds a custom Airflow image by installing dependencies from ```requirements.txt``` and baking in the DAG and preprocessing scripts so they’re always available in the container.

# Below are the four tasks:

## Task 1: preprocess_training.py
This script does the preprocessing for the raw data file ```MM_KP.csv```, pulled directly from KenPom. This includes all KenPom metrics for every year back to its creation in 2002. The script cleans the file, feature engineers new columns like 'Tourney Seed' or 'Win Percentage', and manually fills the target column 'Winner'. The file also has code that calculates correlations between features and targets, along with covariance between features. The training/testing dataset uses only features that have a correlation magnitude with the target of 0.1 or higher. Additionally, for any pair of features with a correlation magnitude at or above 0.8, the feature with the weaker correlation to the target variable is dropped. Until next year's March Madness bracket is announced, 2002-2024 is used for training, and 2025 is used as the test. 

## Task 2: train.py
This script trains and tunes an XGBoost model on March Madness data using ```RandomizedSearchCV```, validates it with repeated k-fold cross-validation, evaluates performance metrics, and saves the best model with joblib. It also scales all features accordingly. For the current iteration, the training has resulted in the optimal MSE of 0.016804. The MAE, RMSE, and R^2 values are 0.090295, 0.129356, and 0.653505, respectively. These values can be found in ```eval_metrics_2025``` in the ```results``` folder. 

## Task 3: preprocess_test.py
This script has the same function as ```preprocess_training.py```, preprocessing only for 2025. 

## Task 4: predict.py
This script extracts the model that was trained in the second task and predicts on the test set. It saves the output predictions as ```predictions_2025.csv``` (for this year) in the ```results``` folder. 

# Run The Application
Assuming the user already has Docker installed, the following commands first clean up any existing containers, rebuild the Docker images, and initialize Airflow. Then the webserver and scheduler are started, the database and DAGs are verified, the pipeline is manually triggered, and the logs are streamed to watch it run:
```
docker compose down -v --remove-orphans
docker compose build
docker compose run --rm airflow-init
docker compose up -d airflow-webserver airflow-scheduler
docker compose exec airflow-scheduler airflow db check
docker compose exec airflow-scheduler airflow dags list
docker compose exec airflow-scheduler airflow dags list-import-errors
docker compose exec airflow-scheduler airflow dags trigger march_madness_predictions
docker compose logs -f airflow-scheduler
```

Once the containers are up, the user can access the Airflow UI at http://localhost:8080 and run the DAG from there. The username is march and password is madness. 

<img width="1508" height="645" alt="Image" src="https://github.com/user-attachments/assets/7d14ea9e-0305-466e-a09d-9fbaa66ddfab" />
