import argparse
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--thumbnail-size", default=256, type=int, help="size of thumbnails")
    parser.add_argument("embedding_csv_path", help="path to csv representing the data embedding. this csv file must have headers and columns for path, x, y which represent the embedding.")
    args = parser.parse_args()

    df = pd.read_csv(args.embedding_csv_path)

    paths = df["path"]
    X = df["x"]
    Y = df["y"]

    # preload thumbnails to improve interactivity
    thumbnails = {}

    for path in paths:
        image = Image.open(path)
        # need to choose smaller thumbnail size for very large datasets
        image.thumbnail((args.thumbnail_size, args.thumbnail_size))
        thumbnails[path] = image

    fig, (scatter_ax, thumbnail_ax) = plt.subplots(ncols=2)

    scatter_ax.scatter(X, Y, picker=True)

    state = {}

    def hover(event):
        # only process events from the scatter plot
        if event.inaxes != scatter_ax:
            return
        x, y = event.xdata, event.ydata
        i = np.argmin((x - X)**2 + (y - Y)**2)
        thumbnail_path = paths[i]
        # skip if still displaying the same thumbnails
        if state.get("thumbnail_path") == thumbnail_path:
            return
        thumbnail_ax.imshow(thumbnails[thumbnail_path], resample=False)
        state["thumbnail_path"] = thumbnail_path
        fig.canvas.draw_idle()

    fig.canvas.mpl_connect("motion_notify_event", hover)

    plt.show()


if __name__ == "__main__":
    main()
