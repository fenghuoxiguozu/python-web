import random
import numpy as np
import string
from captcha.image import ImageCaptcha
from keras.layers import Input,MaxPooling2D,Dense,BatchNormalization,Conv2D,Flatten
from keras.models import Model,Sequential
from keras.callbacks import ModelCheckpoint,TensorBoard
from keras.utils.vis_utils import plot_model
import matplotlib.pyplot as plt
from PIL import Image


def random_code():
    raw = string.digits
    code = ''.join(random.sample(raw,4))
    return code,raw

def gen_sample(height=80,width=170,batch_size=32,n_class=4):
    print("生成样本")
    X = np.zeros((batch_size,height,width,3),dtype=np.float)
    Y = [np.zeros((batch_size,n_class),dtype=np.uint8) for i in range(4)]
    # 生成器
    generator = ImageCaptcha(height=height,width=width)
    while 1:
        for i in range(batch_size):
            code,raw,  = random_code()
            # print(rows, code)
            X[i] = np.array(generator.generate_image(code)).astype('float32')/255.0

            for j,ch in enumerate(code):
                print(code,X,Y)
                Y[j][i,:0] = 0
                Y[j][i,raw.find(ch)] = 1
        yield X,Y

def train_model():
    h,w,n_class = 80,170,4
    input = Input(shape=(h,w,3))
    x = input
    for i in range(4):
        x = Conv2D(filters=32*2**i,kernel_size=(3,3),activation='relu')(x)
        x = Conv2D(filters=32*2**i,kernel_size=(3,3),activation='relu')(x)
        x = BatchNormalization(axis=3)(x)
        x = MaxPooling2D((2,2))(x)
    x = Flatten()(x)
    x = [Dense(n_class,activation='softmax',name='D%d'%(n+1))(x) for n in range(4)]
    model = Model(inputs = input,outputs = x)

    return model

# plot_model(train_model(),to_file='train.png',show_shapes=True)



def train():
    model = train_model()
    check_point = ModelCheckpoint(
        filepath = 'train.h5',
        save_best_only = True
    )

    model.compile(
        loss = 'categorical_crossentropy',
        optimizer = 'adadelta',
        metrics = ['accuracy']
    )

    model.fit_generator(
        gen_sample(),
        epochs=10,
        steps_per_epoch=50,
        validation_data=gen_sample(),
        validation_steps=10,
        callbacks = [check_point,TensorBoard(log_dir='logs')]
    )


if __name__ == '__main__':
    train()
