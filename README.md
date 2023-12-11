# SULI: SUrface Lidar Imaging

This is the official dataset for the paper `Deep Learning-Based Real-Time Detection of Surface Landmines Using Optical Imaging`.  repo is about `Surface Lidar Image Analysis`. Our aim is to find surface land-mine such as `butterfly` and `star-fish`.

## Get started
You need to create a python venv following command:
```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

## Dataset creation

The dataset has been collected with `iPhone13-Lidar` and [record-3d](https://record3d.app/) software and application.
For information about the software, refer to the [record-3d](https://record3d.app/) github repository.
For information about dataset environmental settings and procedure, feel free to open an issue.

## Dataset Annotations

The data collected are annotated using [CVAT](https://www.cvat.ai/) software. Annotation are done both on their server, and locally.
To use their server, please refer to the [webpage](https://www.cvat.ai/). To set up your own CVAT server, please refer to the [documentation](https://github.com/opencv/cvat).

<!-- 
### Raw Data
If you want to access the data in Raw format, you can download the images and labels from the links:
- [images (both ITA and USA)](https://windu.micc.unifi.it/datasets/surland/raw-images)
- [labels (both ITA and USA)](https://windu.micc.unifi.it/datasets/surland/raw-labels)

These comprehend both ITA and USA images, and you can get the split files from [splits](https://windu.micc.unifi.it/datasets/surland/raw-splits) which
contains the `txt` for ITA (`raw-ITA-splits.txt`) and USA (`raw-USA-splits.txt`).

Then, using the code in utils, you can then create, using the format you want, the splits.  
-->

### Data in YOLO format
You can get the ITA and USA datasets from:
- [ITA (iid data)](https://windu.micc.unifi.it/datasets/surland/iid)
- [USA (ood data)](https://windu.micc.unifi.it/datasets/surland/ood)

These are the IID and OOD data, respectivelly. We advise you to download them (or link them with a sym-link) into the two folders:
```tree
/SURLAND-Dataset
    /data-iid   <-- ITALY dataset
        /ITA.yaml
        /yolo.json
        /train
        /val
        /test
    /data-ood   <-- USA dataset
        /USA.yaml
        /yolo.json
        /val
        /test
    /docs
    /examples
    /venv
    LICENSE
    README.md
    requirements
```

## Dataset split
For the Italian data, we decided to split the data based on the video numbers as follow:
```python
test = [2, 10, 19, 27, 36, 44]
val = [3, 7, 15, 26, 33]
train = [1, 4, 6, 8, 9, 11, 12, 13, 14, 16, 17, 18, 20, 21, 22, 23, 24, 25, 28, 29, 30, 31, 32, 34, 35, 37, 39, 40, 41, 42, 43, 45, 46, 47]
```

This because, as you can appreciate from the excell file that describe all videos, we wanted to have similar distribution of data across all the three splits.

For the USA data, however, we decided to provide `val` and `test` split as those `Out of Distribution` data are only used at inference.
