# Training with TensorFlow

## install Requitement

- Installed TensorFlow, either CPU or GPU (See [TensorFlow Installation][1])
- Installed TensorFlow Models (See [TensorFlow Models Installation][2])
- Installed labelImg (See [LabelImg Installation][3])

Now that we have done all the above, we can start doing some cool stuff. Here we will see how you can train your own object detector, and since it is not as simple as it sounds, we will have a look at:

1. How to organise your workspace/training files
2. How to prepare/annotate image datasets
3. How to generate tf records from such datasets
4. How to configure a simple training pipeline
5. How to train a model and monitor it’s progress
6. How to export the resulting model and use it to detect objects.

## Preparing workspace

```
TensorFlow
├─ addons
│   └── labelImg
└─ models
    ├── official
    ├── research
    ├── samples
    └── tutorials
```

Now create a new folder under `TensorFlow` and call it `workspace`. It is within the `workspace` that we will store all our training set-ups. Now let’s go under workspace and create another folder named `training_demo`. Now our directory structure should be as so:

```
TensorFlow
├─ addons
│   └─ labelImg
├─ models
│   ├─ official
│   ├─ research
│   ├─ samples
│   └─ tutorials
└─ workspace
    └─ training_demo
```


[1]: https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html#tf-install
[2]: https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html#tf-models-install
[3]: https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html#labelimg-install


```resource


https://www.tensorflow.org/install/pip

https://towardsdatascience.com/creating-your-own-object-detector-ad69dda69c85
https://medium.com/@WuStangDan/step-by-step-tensorflow-object-detection-api-tutorial-part-1-selecting-a-model-a02b6aabe39e

https://github.com/tensorflow/models/tree/master/research/object_detection
https://hci.iwr.uni-heidelberg.de/node/6132
https://github.com/bosch-ros-pkg/bstld

https://www.edureka.co/blog/tensorflow-object-detection-tutorial/

https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/training.html
https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/training.html
https://medium.com/pylessons/tensorflow-step-by-step-custom-object-detection-tutorial-d7ae840a74e2
https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10
https://jameslittle.me/blog/2019/tensorflow-object-detection
https://jameslittle.me/blog/2019/tensorflow-object-detection
https://pylessons.com/Tensorflow-object-detection-faster-csgo-aim-bot/
https://medium.com/@karol_majek/10-simple-steps-to-tensorflow-object-detection-api-aa2e9b96dc94
````

[tensorflow-model-install]: https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md
