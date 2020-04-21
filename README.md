# COCO dataset from labelme
 Creating a COCO dataset from labelme's annotations

## Requirements

Install [Labelme](https://github.com/wkentaro/labelme)

Know the path of the installation

## Parameters
    - -i: Name of the folder which contains the images and annotations
    - -f: Name of the final folder with the COCO dataset
    - -l: Path to the file with the labels of the dataset
    - [-p: Path to the labelme installation (or path labelme doing: git clone https://github.com/wkentaro/labelme.git)] (Not now)
    - -y: Year of the dataset. By default, it is 2019
    - -t: Percetage of training. By default, it is 70

## Structure of the final folder

    - annotations
        - instances_train2019.json
        - instances_val2019.json
    - train2019
        - image_a.jpeg
        - image_b.jpeg
        - ...
        - image_z.jpeg
    - val2019
        - image_1.jpeg
        - image_2.jpeg
        - ...
        - image_15.jpeg
