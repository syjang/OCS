from django.http import HttpResponse, JsonResponse

from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
from keras.preprocessing.image import array_to_img
import numpy as np
import tensorflow as tf

from django.views.decorators.csrf import csrf_exempt
import io
from PIL import Image


# init model
model = ResNet50(weights='imagenet')
graph = tf.get_default_graph()

# Create your views here.
@csrf_exempt
def Inference(request):
    if request.method == 'GET':
        s2 = "{ \"ok\" = ture }"
        return HttpResponse(s2)
    
    elif request.method == 'POST':
        body = request.body
        img = Image.open(io.BytesIO(body))
        img = img.resize((224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        global graph
        with graph.as_default():
                preds = model.predict(x)
                s = decode_predictions(preds, top=3)[0]#"{ \"ok\" = ture }"
        return HttpResponse(s)
        