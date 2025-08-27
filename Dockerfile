FROM apache/airflow:2.10.2-python3.11
COPY requirements.txt /opt/airflow/requirements.txt
RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt

#bake into image
COPY dags /opt/airflow/dags
COPY preprocess_train_predict_scripts /opt/airflow/scripts