### Gender Classification Using Various Algorithms

<p> For this exercise the Fall 2018 DATA620 Web Analytics class worked together

to create algorithms to classify the gender of names from the python Names corpus. </p>

Idea is as follows:

- Extract the names from the nltk.corpus and assign genders to each name.

- Use different features to see which are the best candidates and feed them into
a Naive Bayes Classifer, Decision Tree Classification and Maximum Entropy Classification.

- Evaluate each classifer by accuracy and see which features are the most important
in classifying a name's gender.

- Some of us worked on different algorithms and getting the data ready.
Some example features include the last and first letters of the name and more interesting
features such as non-contigous letters, number of vowels and sharp consonants.

- With the features selected it was time to split the data into test, training and dev-test sets.
However, we decideed to randomly shuffle the names and assign the datasets so when repeated, the outcome
was not the same and is not biased from previous experiments.

- Then we on to train the classifers and see what the accuracy was, and main features.

- We started witn Naive Bayes which is based on independence and that all features are dependent on one another.
With names, that is usually not the case and in the real world is not the case as well. We did the the length of the name,
and the last and first letters initally, got a accuracy of about 70% and several names were missclassified.

- We decided to then do a round 2, re-assign randomly the training/test/dev-test sets and included the last 2 and last 3 letters
The accuracy increased slightly and we found that names ending with 'na' were about 94 times more likley to be female than male.

- We then proceeded with using decision trees and only use a few features to see how the decision tree classifer would work.
It turned out the accuracy was around 79% percent and a gini value of about 0.46.

- The final algorithm was using Maximum Entropy classifer. The Max Entropy Classifer is a classifer where unlike Naive Bayes,
it does not assume that the features are all independent. The idea behind it is that it finds the set of features/parameters that maximizes the likelihood of the training data. The higher the entropy the better then the classifer will be.

- In Summary, we find that the most important features to be used are the last 2 or last 3 letters in someone's name. Putting too many features could cause the model to overfit the data or possibly decrease the accuracy.

### Names of people who participated and their role:

- Naive Bayes:

    Jonathan Hernandez
    
    Kyle Glide
    
    Aaron G
    
- Maximum Entropy

    Ahmed Sajjad
    
    Raghunathan Ramanth
    
    Mezue
    
- Decision Trees

    Raghunathan Ramanth
    
    Dilip
