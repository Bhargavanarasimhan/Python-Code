import pandas as pd
import re
import nltk
import string
from sklearn.feature_extraction.text import CountVectorizer
data=pd.read_csv("G://MS-SEM3/AIT-624/Project/Condo_Virginia_Cleaned TXT_out.csv",header=None)
ps=nltk.WordNetLemmatizer()

stopwords= nltk.corpus.stopwords.words('english')
data.columns=['AD','Post','Owner_desc','ADD_com','Reviews']

data_needed=pd.DataFrame({'AD':data['AD'],
                   'full_DATA':data['Reviews']})
def rem_stopwords(text):
    text= "".join([word for word in text if word not in string.punctuation])
    tokens= re.split('\W+',text)
    text=" ".join([ps.lemmatize(word) for word in tokens if word not in stopwords])
    return text

data_needed['cleantext']=data_needed['full_DATA'].apply(lambda x: rem_stopwords(x.lower()))



Location=pd.read_csv("G://MS-SEM3/AIT-624/Project/Location.csv")
Loc=[]
for i in range(len(Location)):
   Loc.append(string.lower(Location['City'][i]))
def cities(text):
    text= "".join([word for word in text if word not in string.punctuation])
    tokens= re.split('\W+',text)
    text=([word for word in tokens if word in Loc])
    return text

data_needed['cleantext_AD']=data_needed['AD'].apply(lambda x: cities(x.lower()))

#print(data_needed['cleantext_AD'][1])

data_f=pd.DataFrame({
    'Location':data_needed['cleantext_AD'],
    'clean_data':data_needed['cleantext']})

ngram_vect=CountVectorizer(ngram_range=(1,1))
count_x=ngram_vect.fit_transform(data_f['clean_data'])
#print(count_x.shape)
#print(ngram_vect.get_feature_names())

data_frame1=pd.DataFrame(count_x.toarray())
data_frame1.columns=ngram_vect.get_feature_names()




ngram_vect1=CountVectorizer(ngram_range=(2,2))
count_x1=ngram_vect1.fit_transform(data_f['clean_data'])
data_frame2=pd.DataFrame(count_x1.toarray())
data_frame2.columns=ngram_vect1.get_feature_names()


print(data_frame2)