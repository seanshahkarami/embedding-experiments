from transformers import AutoImageProcessor, ViTModel, ResNetModel, CLIPProcessor, CLIPModel
import torch
from PIL import Image
from pathlib import Path
import numpy as np
import sys
from multiprocessing.pool import ThreadPool
from sklearn.manifold import TSNE
import pandas as pd


def main():
    paths = [Path(s.strip()).absolute() for s in  sys.stdin.readlines()]

    # image_processor = AutoImageProcessor.from_pretrained("google/vit-base-patch16-224-in21k")
    # model = ViTModel.from_pretrained("google/vit-base-patch16-224-in21k")
    image_processor = AutoImageProcessor.from_pretrained("microsoft/resnet-50")
    model = ResNetModel.from_pretrained("microsoft/resnet-50")

    def get_embedding(path):
        image = Image.open(path)
        inputs = image_processor(image, return_tensors="pt")
        with torch.no_grad():
            outputs = model(**inputs)
        return outputs.last_hidden_state.view(-1).numpy()

    # can we use some kind of clip embedding for this?
    # model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    # processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

    # def get_embedding(path):
    #     image = Image.open(path)
    #     inputs = image_processor(image, return_tensors="pt")
    #     with torch.no_grad():
    #         outputs = model(**inputs)
    #     return outputs.last_hidden_state.view(-1).numpy()

    with ThreadPool() as pool:
        X = np.array(pool.map(get_embedding, paths))
    
    Y = TSNE(n_components=2, perplexity=5, n_iter=5000, init="random").fit_transform(X)

    df = pd.DataFrame({"path": paths, "x": Y[:, 0], "y": Y[:, 1]})
    df.to_csv("tsne-embedding-2.csv", index=False)


if __name__ == "__main__":
    main()
