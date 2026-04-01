from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, UpSampling2D, concatenate
from tensorflow.keras.models import Model

from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, UpSampling2D, concatenate
from tensorflow.keras.models import Model

def build_unet(input_size=(256, 256, 4)):  # ← CHANGED: 4 channels (RGB + NIR)
    inputs = Input(input_size)
    c1 = Conv2D(64, 3, activation="relu", padding="same")(inputs)
    p1 = MaxPooling2D()(c1)
    c2 = Conv2D(128, 3, activation="relu", padding="same")(p1)
    u1 = UpSampling2D()(c2)
    merge = concatenate([c1, u1])
    outputs = Conv2D(1, 1, activation="sigmoid")(merge)
    return Model(inputs, outputs)