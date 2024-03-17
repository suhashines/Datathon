import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.naive_bayes import GaussianNB

def scale_dataset(dataFrame,overSample=False):

    x = dataFrame[dataFrame.columns[:-1]].values 
    y = dataFrame[dataFrame.columns[-1]].values

    scaler = StandardScaler()
    x = scaler.fit_transform(x)

    if overSample:
        ros = RandomOverSampler()
        x,y = ros.fit_resample(x,y)

    data = np.hstack((x,np.reshape(y,(-1,1))))

    return data,x,y

    #let's understand this line 

    # so we're concatening together x and y again to form our final transformed dataset using np.hstack(x,y)

    #but numpys are very sensitive to dimensions reshape(y,(-1,1))
    # -1 saying infer what that dimension would be



columns = ["fLength","fWidth","fSize","fConc","fConc1","fAsym","fM3Long","fM3Trans","fAlpha","fDist","class"]
df = pd.read_csv('magic04.data',names=columns)

#print(df)

#now let's change the class value g=1, h=0

df['class'] = (df['class'] == 'g').astype(int)

print(df['class'])

#our task is to simply classify whether a data item falls into the g class or h class

#print(df.head())


#the following code draws a histogram for gamma and fLength
# plt.hist(df[df['class']==1]['fLength'],color='blue',label='Gamma',alpha=0.7,density=True)
# plt.xlabel('fLength')
# plt.ylabel('Probability')
# plt.title('fLength')
# plt.legend()
# plt.show()

# now suppose I want to draw histograms for each features

for column in columns[:-1]:

    plt.hist(df[df['class']==1][column],color='blue',label='Gamma',alpha=0.7,density=True)
    plt.hist(df[df['class']==0][column],color='red',label='Hadron',alpha=0.7,density=True)

    plt.title(column)
    plt.xlabel(column)
    plt.ylabel('Probability')
    plt.legend()
    #plt.show()


#now it's time to split our dataset into Train, valid and test
    
train,valid,test = np.split(df.sample(frac=1),[int(0.6*len(df)),int(0.8*len(df))])

#df.sample(frac=1) it basically shuffles our dataset
#[int(0.6*len(df)),int(0.8*len(df))] everything between 60 and 80 percent will go to my valid dataset and others will go
# to train and test accordingly

print(train)

# some important observations 
#---------------1--------------------------
# the data of the column of fLength has maxValue of 100 and above, whereas data of fConc1 column is has very small value
# so an important thing is to scale the dataset
#so let's define a function that will scale a given dataFrame

#scale_dataset(df) will do that for us

#--------------------2--------------------------
# let's see the density of gammas and handrons feature vectors in dataset

print(len(train[train['class']==1]))  # 7377

print(len(train[train['class']==0]))  # 4035

#so not enough hadrons as compared to gammas, so we want to oversample our data
#so let's another param to our scale_dataset function -> overSample -> overSample the data that has less quantity

train, x_train, y_train = scale_dataset(train,True)

print(sum(y_train==0))

valid, x_valid, y_valid = scale_dataset(valid)

test, x_test, y_test = scale_dataset(test)

#notice we're not oversampling valid and test, because upon giving a random feature vector that is unbalanced
# I want to see how my model performs

# now we're ready to train our model

# algorithm : K nearest neighbours 

knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(x_train, y_train)

y_pred = knn_model.predict(x_test)

print(classification_report(y_test,y_pred))

# there are two important things in a classification_report 

# precision : 0.77 of hadrons -> if model says there are 100 hadrons, actually there are 77 
# recall : 0.68 of hadrons -> Given 100 hadrons the model will be able to identify 68 of them

#now that we have a report we can apply naive bayes theorem

nb_model = GaussianNB()
nb_model = nb_model.fit(x_train,y_train)

y_pred = nb_model.predict(x_test)

print(classification_report(y_test, y_pred))