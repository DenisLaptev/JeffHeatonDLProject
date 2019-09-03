from PIL import Image
import requests
from io import BytesIO

import matplotlib.pyplot as plt

url = "https://upload.wikimedia.org/wikipedia/commons/9/92/Brookings.jpg"

response = requests.get(url)
img = Image.open(BytesIO(response.content))
plt.imshow(img)
plt.show()
