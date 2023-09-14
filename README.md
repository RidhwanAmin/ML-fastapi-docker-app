# ML-fastapi-docker-app
I built this project aiming to serve machine learning models with FastAPI. More specifically, I used a scikit-learn library of classification model for oilfield lithology prediction. The FastAPI implementation allows it to handle requests much faster than traditional synchronous frameworks. Furthermore I also integrate the code with Docker so it is portable and can be deployed with more ease.

## Problem Statement
Lithology prediction based on drilling data can be applied in real-time geosteering. Whenever the measurements from drilling come in, the model predicts the lithology. 

Our attempt is to predict lithology from drilling data using ML model.

## How this project works

The best way is to read along first the notebook first which explain the machine learning project in further details.

To clone this repo use the following command:

```bash
git clone https://github.com/RidhwanAmin/ML-fastapi-docker-app.git
```

First step to change directory to the cloned project folde in your terminal. 

Second step step is build the Docker image for this project. 

```bash
 docker build -t oilfield-classify-app .  
```

and lastly is to Run to run it as a container.

```bash
  docker run -p 80:80 oilfield-classify-app    
```

After that, you can test the HTTP response in your own local host with FASTAPI swagger UI by searching https://0.0.0.0/docs in your browser. 




