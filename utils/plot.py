import matplotlib.pyplot as plt
import numpy as np
from torch.utils.data import Subset

def plot_classes(set:Subset, class_names:list[str])->None:

    img_per_class = dict(zip(class_names, np.zeros(len(class_names))))
    for i,class_num in set:
         img_per_class[class_names[class_num]] += 1

    plt.figure(figsize=(20, 8))
    plt.bar(list(class_names), img_per_class.values(), color='g')
    plt.title("Images per class")
    plt.xticks(rotation=90)
    plt.xlabel('Class')
    plt.ylabel('Number of Images')
    plt.show()
