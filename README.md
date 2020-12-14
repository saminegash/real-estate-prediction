![](beautiful_appartment.jpg)

I have build This data science project for my azure machine learning training which is given by Gebeya and Microsoft for Africa and the project is end to end machine learning model building from data collection to deployment on azure cloud with a real estate price prediction site to show how the model works. We have first build a model using sklearn and decision tree regressor using Brazil home prices dataset from [kaggle](https://www.kaggle.com/davivieirab/real-estate-data-brazil)) we then wrote a python flask server that uses the saved model to serve http requests. Third component is the website built in html, css and javascript that allows user to enter home square ft area, rooms etc and it will call python flask server to retrieve the predicted price. During model building we have covered almost all data science concepts such as data load and cleaning, outlier detection and removal, feature engineering, dimensionality reduction, gridsearchcv for hyperparameter tunning, k fold cross validation etc. Technology and tools wise this project covers,

1. Python
2. Numpy and Pandas for data cleaning
3. Matplotlib for data visualization
4. Sklearn for model building
5. Jupyter notebook, visual studio code and pycharm as IDE
6. Python flask for http server
7. HTML/CSS/Javascript for UI

# Deploy this app to cloud (on Azure cloud)

1. Create a resource group for web app with unique name
2. Connect your repository to connect to your project and fetch it to azure,
3. Follow the steps to connect each and every steps along the way