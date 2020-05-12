import string,random
import numpy as np
from captcha.image import ImageCaptcha
from keras.models import Model,load_model
import matplotlib.pyplot  as plt


def random_code():
    raw = string.digits + string.ascii_uppercase
    code = ''.join(random.sample(raw,4))
    return code,raw


def gen_sample(height=80,width=170,batch_size=1,n_class=36):
    print("生成样本")
    X = np.zeros((batch_size,height,width,3),dtype=np.float)
    Y = [np.zeros((batch_size,n_class),dtype=np.uint8) for i in range(4)]
    # 生成器
    generator = ImageCaptcha(height=height,width=width)
    while 1:
        for i in range(batch_size):
            code,raw,  = random_code()
            generate_code = generator.generate_image(code)
            X[i] = np.array(generate_code).astype('float32')/255

            for j,ch in enumerate(code):
                Y[j][i,:0] = 0
                Y[j][i,raw.find(ch)] = 1
        yield X,Y,raw,generate_code,code


def decoder(Y,code):
    y = np.argmax(np.array(Y),axis=2)[:,0]
    return ''.join([code[x] for x in y])

model = load_model('train.h5')
X,Y,raw,generate_code,code = next(gen_sample())
result = model.predict(X)
print(result,decoder(Y=result,code=raw))

plt.imshow(generate_code)
plt.title('Truth')
plt.show()