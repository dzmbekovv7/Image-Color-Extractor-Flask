from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

def extract_colors(image_path, num_colors=5):
    image = Image.open(image_path)
    image = image.resize((200, 200))
    image = image.convert('RGB')

    pixels = np.array(image).reshape(-1, 3)

    kmeans = KMeans(n_clusters=num_colors, random_state=42).fit(pixels)
    centers = kmeans.cluster_centers_.astype(int)

    hex_colors = ['#{:02x}{:02x}{:02x}'.format(*center) for center in centers]
    return hex_colors

