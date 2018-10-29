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

- We then proceeded with using decision trees and only use a few features and slowly build decision stumps and adding new featuersto see how the decision tree classifer would work.
It turned out the best features decided was 'last2' and 'every_other2_end' and 'last' with an accuracy of about 80.6% on the dev-test set. The accuracy on the test set was about 77.6%. One reason for this is that we tuned the decision tree towards the dev-test set to increase accuracy and decrease errors.

- The final algorithm was using Maximum Entropy classifer. The Max Entropy Classifer is a classifer where unlike Naive Bayes,
it does not assume that the features are all independent. The idea behind it is that it finds the set of features/parameters that maximizes the likelihood of the training data. The higher the entropy the better then the classifer will be.

## Summary

- We find that the most important features to be used are the last 2 or last 3 letters in someone's name. Putting too many features could cause the model to overfit the data or possibly decrease the accuracy.

- From the class_project python notebook:

    - last n letters: These have shown to be the most popular among classifying gender in names. Names ending in -na are well classified to be female for example.

    - test-set analysis:
        - We notice that in the naive bayes version 2 classifier performed the best in terms of accuracy, followed by Maximum Entropy           and then by Decision Trees.

    - dev-test analysis:
        - The Maximum Entropy classifer performed the best in terms of accuracy, followed by naive bayes v2, naive bayes v1 and,                decision trees.

- A reason why the dev-test accuracy performance was different than the test ones could be the following:

    - We trained and improved the accuracy of the dev-test set so that the test set can be even more accurate. Improving on the dev-test set helps to hopefully reduce errors and be ready for testing.

    - Randomly shuffling the datasets each run could've been a factor as different runs give slighly different accuracy and most informative features could change.


- Looking at the two graphs, it shows that the best classifer algorithm would be the Maximum Entropy. This is becauase it doesn't assume that all featuers and independent of one another. Also as mentioned, does not require a vast amount of data like decision trees as long as the dataset has a high entropy.

### Names of people who participated and their role:

- Naive Bayes:

    Jonathan Hernandez

    Kyle Glide

    Aaron G

    Alvaro Bueno

- Maximum Entropy

    Ahmed Sajjad

    Raghunathan Ramanth

    Mezue

    David Quarshie

- Decision Trees

    Raghunathan Ramanth

    Dilip
    
    Olya Fomicheva

- Summary Charts

    Bruce Hao
