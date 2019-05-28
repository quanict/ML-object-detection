import cv2 # computer vision library
import matplotlib.pyplot as plt # to plot
from darknet import Darknet # to use DarkNet

config_file = './cfg/yolov3.cfg'
pretrained_weights = './weights/yolov3.weights'

net = Darknet(config_file)

net.load_weights(pretrained_weights)

net.print_network()


plt.rcParams['figure.figsize'] = (15.0, 15.0)
img = cv2.imread('./images/city_scene.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)

class_names_file = 'data/coco.names'
class_names = load_class_names(class_names_file)

print(class_names)


resized_image = cv2.resize(img, (net.width, net.height))

iou_threshold = 0.4
nms_threshold = 0.6

boxes = detect_objects(net, resized_image, iou_threshold, nms_threshold)
print_objects(boxes, class_names)
plot_boxes(img, boxes, class_names, plot_labels = True)