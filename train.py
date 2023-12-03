import keras
from keras import layers
from keras.layers.embeddings  import Embedding
from keras.models import Sequential
from keras.preprocessing.text import one_hot
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Input, Dense, Dropout
from keras.models import Model
from keras.layers import LSTM, merge
from keras.layers import Bidirectional
from keras import optimizers

title1_list = []
title2_list = []
title1_embeded_list = []
title2_embeded_list = []
all_docs = title1_list + title2_list

#Our trainable encoder based on bidirectional siamese LSTM to find the similarity between two titles
def blstm_encoder(input_length, emb_dim):
    seq = Sequential()
    #TODO embedding the string inputs
    seq.add(Embedding(input_length, emb_dim, mask_zero=True))
    seq.add(Bidirectional(LSTM(128)))
    seq.add(Dropout(0.3))
    return seq

input_length = 50
dense_encoding = 16
vocab_size = 1000

#Our inputs
title_1 = Input(shape=(input_length,))
title_2 = Input(shape=(input_length,))

#Embeding the input texts using one_hot
#Pad the embeddings so that all have equal lengths(max_length)
max_length = 10
embeded_titles = [one_hot(d, vocab_size) for d in all_docs]
padded_titles = pad_sequences(embeded_titles, maxlen=max_length, padding='post')

title1_embeded_list = padded_titles[0:len(title1_list)]
title2_embeded_list = padded_titles[len(title1_list):]

#Pass the title_1 and title_2 through bidirectional siamese LSTM encoder
encoder = blstm_encoder(input_length, dense_encoding)
title_1_representation = encoder(title_1)
title_2_representation = encoder(title_1)

#The output should be a cosine proximity value
siamese_out = keras.layers.dot([title_1_representation, title_2_representation], 1, normalize=True)
#Functional model representation
siamese_model = Model(input=[title_1, title_2], output = siamese_out)
#Set the optimiser and loss function of the model
siamese_model.compile(optimizer=optimizers.Nadam(lr=0.002, beta_1=0.9, beta_2=0.999, epsilon=None, schedule_decay=0.004), loss='mean_squared_error')
tr_y = 0.5
#train the model
siamese_model.fit(x = [title_1, title_2], y = tr_y ,  epochs = 100, verbose = 0)
