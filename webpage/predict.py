import io
from PIL import Image
import torch
from torchvision import transforms

def get_model(path = None):
    checkpoint = torch.load(path,  map_location='cpu')
    model = checkpoint['model']
    model.classifier = checkpoint['classifier']
    model.load_state_dict(checkpoint['state_dict'], strict=False)
    model.eval()
    return model

def get_tensor(image, image_size = 224, norm_mean = [0.485, 0.456, 0.406], norm_std = [0.229, 0.224, 0.225]):
    preprocessing = [transforms.Resize(image_size+1),
                 transforms.CenterCrop(image_size),
                 transforms.ToTensor()]
    if norm_mean and norm_std:
        preprocessing += [transforms.Normalize(norm_mean, norm_std)]
    transform = transforms.Compose(preprocessing)
    image = Image.open(io.BytesIO(image))
    return transform(image).unsqueeze(0)


def get_prediction(x):
    # path = './model/{name}'.format(name='amsgrad_dense_60.pth')
    path = '../model/amsgrad_dense_60.pth'
    model = get_model(path)
    # Get the class probabilities
    ps = torch.exp(model(x))
    # Get highest values
    top_p, top_class = ps.topk(1, dim=1)
    print(top_class, '= flower idx')
    return float(top_p[0][0]), int(top_class[0][0])
