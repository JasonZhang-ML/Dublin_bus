## Prediction
The folder contains implement scripts of prediction model including stages from mysql access to prediction results.

- transformer/:
Contains all pipeline sections which will process origin data.

- with and without '_nodist':
The first kind of scripts will contain the distance and velocity features. However, in the process, I found that some stopids in 2018 have been deleted.
It means that those distance info will missed.
And provides another solution without distance feature with '_nodist.py' file set.

- pre_saved.py, pre_saved_nodist.py
The scripts will preprocessed data and saved their '.pkl' files.
filename will be 'routeid_direction.pkl' ex. '33E_1' means route '33E' and direction 1.

- load_predict.py, load_predict_nodist.py:
The scripts will load selected '.pkl' file and return prediction results based on input.


## Author
- Jiansheng Zhang