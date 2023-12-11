# SULAND: SUrface LANDmine (detection)

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

### Dataset split
For the Italian data, we decided to split the data based on the video numbers as follow:
```python
test = [2, 10, 19, 27, 36, 44]
val = [3, 7, 15, 26, 33]
train = [1, 4, 6, 8, 9, 11, 12, 13, 14, 16, 17, 18, 20, 21, 22, 23, 24, 25, 28, 29, 30, 31, 32, 34, 35, 37, 39, 40, 41, 42, 43, 45, 46, 47]
```

This because, as you can appreciate from the excell file that describe all videos, we wanted to have similar distribution of data across all the three splits.

For the USA data, however, we decided to provide all videos as `test` split as those `Out of Distribution` data are only used at inference:
```python
test = [1,2,3,4,5,6,7,8,9,10]
```

In the paper you can find the statistics about the datasets and the splits.
Raw information are shown in the following table:

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-d6h8{color:#FFCFC9;text-align:left;vertical-align:bottom}
.tg .tg-o5n3{background-color:#FFF;font-weight:bold;text-align:left;vertical-align:bottom}
.tg .tg-4e1g{background-color:#FFF;color:#D4EDBC;text-align:left;vertical-align:bottom}
.tg .tg-s26b{color:#E5E5E5;text-align:left;vertical-align:bottom}
.tg .tg-o88q{color:#473821;text-align:left;vertical-align:bottom}
.tg .tg-x2c0{background-color:#FCE5CD;text-align:left;vertical-align:bottom}
.tg .tg-4bam{background-color:#FFF;text-align:center;vertical-align:bottom}
.tg .tg-y486{color:#3D3D3D;text-align:left;vertical-align:bottom}
.tg .tg-j6zm{font-weight:bold;text-align:left;vertical-align:bottom}
.tg .tg-n1r7{background-color:#FFF;font-weight:bold;text-align:center;vertical-align:bottom}
.tg .tg-vp47{color:#0A53A8;text-align:left;vertical-align:bottom}
.tg .tg-yhwj{color:#11734B;text-align:left;vertical-align:bottom}
.tg .tg-7zrl{text-align:left;vertical-align:bottom}
.tg .tg-3y2x{background-color:#FFF;color:#B10202;text-align:left;vertical-align:bottom}
.tg .tg-nhkm{background-color:#FFF;color:#0A53A8;text-align:left;vertical-align:bottom}
.tg .tg-cfqi{color:#753800;text-align:left;vertical-align:bottom}
.tg-sort-header::-moz-selection{background:0 0}
.tg-sort-header::selection{background:0 0}.tg-sort-header{cursor:pointer}
.tg-sort-header:after{content:'';float:right;margin-top:7px;border-width:0 5px 5px;border-style:solid;
  border-color:#404040 transparent;visibility:hidden}
.tg-sort-header:hover:after{visibility:visible}
.tg-sort-asc:after,.tg-sort-asc:hover:after,.tg-sort-desc:after{visibility:visible;opacity:.4}
.tg-sort-desc:after{border-bottom:none;border-width:5px 5px 0}@media screen and (max-width: 767px) {.tg {width: auto !important;}.tg col {width: auto !important;}.tg-wrap {overflow-x: auto;-webkit-overflow-scrolling: touch;}}</style>
<div class="tg-wrap"><table id="tg-sbIaS" class="tg">
<thead>
  <tr>
    <th class="tg-o5n3"><span style="font-weight:bold;background-color:#FFF">Split</span></th>
    <th class="tg-j6zm"><span style="font-weight:bold">Video Title</span></th>
    <th class="tg-n1r7"><span style="font-weight:bold;background-color:#FFF">Durata (s)</span></th>
    <th class="tg-n1r7"><span style="font-weight:bold;background-color:#FFF">Ann. (%)</span></th>
    <th class="tg-n1r7"><span style="font-weight:bold;background-color:#FFF">n° frames ann.</span></th>
    <th class="tg-o5n3"><span style="font-weight:bold;background-color:#FFF">n° frames</span></th>
    <th class="tg-j6zm"><span style="font-weight:bold">Environment</span></th>
    <th class="tg-j6zm"><span style="font-weight:bold">Weather</span></th>
    <th class="tg-j6zm"><span style="font-weight:bold">Orientation</span></th>
    <th class="tg-j6zm"><span style="font-weight:bold">Slope</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-vp47"><span style="color:#0A53A8">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA 1</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">28,83</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">31,79%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">55</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">173</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-7zrl">Cloudy</td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-3y2x"><span style="color:#B10202;background-color:#FFF">test</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-2</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">80,17</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">47,61%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">229</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">481</span></td>
    <td class="tg-y486"><span style="color:#3D3D3D">Gravel</span></td>
    <td class="tg-7zrl">Cloudy</td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-4e1g"><span style="color:#D4EDBC;background-color:#FFF">val</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA 3</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">23,17</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">36,69%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">51</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">139</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-o88q">Cloudy</td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-nhkm"><span style="color:#0A53A8;background-color:#FFF">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-4</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">75,00</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">39,11%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">176</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">450</span></td>
    <td class="tg-y486"><span style="color:#3D3D3D">Gravel</span></td>
    <td class="tg-o88q">Cloudy</td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-nhkm"><span style="color:#0A53A8;background-color:#FFF">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-6</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">24,50</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">20,41%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">30</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">147</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-o88q"><span style="color:#473821">Sunny</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-4e1g"><span style="color:#D4EDBC;background-color:#FFF">val</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-7</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">75,17</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">19,96%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">90</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">451</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-o88q"><span style="color:#473821">Sunny</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-nhkm"><span style="color:#0A53A8;background-color:#FFF">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-8</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">105,33</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">10,60%</span></td>
    <td class="tg-4bam">67</td>
    <td class="tg-4bam"><span style="background-color:#FFF">632</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-o88q"><span style="color:#473821">Sunny</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-nhkm"><span style="color:#0A53A8;background-color:#FFF">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-9</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">41,83</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">17,53%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">44</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">251</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-o88q"><span style="color:#473821">Sunny</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-3y2x"><span style="color:#B10202;background-color:#FFF">test</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-10</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">30,17</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">24,31%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">44</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">181</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-s26b"><span style="color:#E5E5E5">Shadow</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-nhkm"><span style="color:#0A53A8;background-color:#FFF">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-11</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">20,00</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">40,00%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">48</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">120</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-o88q"><span style="color:#473821">Sunny</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-nhkm"><span style="color:#0A53A8;background-color:#FFF">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-12</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">121,33</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">24,86%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">181</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">728</span></td>
    <td class="tg-y486"><span style="color:#3D3D3D">Gravel</span></td>
    <td class="tg-s26b"><span style="color:#E5E5E5">Shadow</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-nhkm"><span style="color:#0A53A8;background-color:#FFF">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-13</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">125,83</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">32,05%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">242</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">755</span></td>
    <td class="tg-y486"><span style="color:#3D3D3D">Gravel</span></td>
    <td class="tg-s26b"><span style="color:#E5E5E5">Shadow</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-nhkm"><span style="color:#0A53A8;background-color:#FFF">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-14</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">24,50</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">100,00%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">147</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">147</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-o88q"><span style="color:#473821">Sunny</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-4e1g"><span style="color:#D4EDBC;background-color:#FFF">val</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-15</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">96,00</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">27,43%</span></td>
    <td class="tg-4bam">158</td>
    <td class="tg-4bam"><span style="background-color:#FFF">576</span></td>
    <td class="tg-y486"><span style="color:#3D3D3D">Gravel</span></td>
    <td class="tg-s26b"><span style="color:#E5E5E5">Shadow</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-nhkm"><span style="color:#0A53A8;background-color:#FFF">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-16</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">98,83</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">28,16%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">167</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">593</span></td>
    <td class="tg-y486"><span style="color:#3D3D3D">Gravel</span></td>
    <td class="tg-s26b"><span style="color:#E5E5E5">Shadow</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-nhkm"><span style="color:#0A53A8;background-color:#FFF">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-17</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">118,33</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">17,32%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">123</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">710</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-o88q"><span style="color:#473821">Sunny</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-nhkm"><span style="color:#0A53A8;background-color:#FFF">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-18</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">129,50</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">10,42%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">81</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">777</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-o88q"><span style="color:#473821">Sunny</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-3y2x"><span style="color:#B10202;background-color:#FFF">test</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-19</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">111,33</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">10,48%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">70</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">668</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-o88q"><span style="color:#473821">Sunny</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-nhkm"><span style="color:#0A53A8;background-color:#FFF">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-20</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">124,50</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">10,17%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">76</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">747</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-o88q"><span style="color:#473821">Sunny</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-nhkm"><span style="color:#0A53A8;background-color:#FFF">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-21</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">128,33</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">26,62%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">205</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">770</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-s26b"><span style="color:#E5E5E5">Shadow</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-nhkm"><span style="color:#0A53A8;background-color:#FFF">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-22</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">112,17</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">8,02%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">54</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">673</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-s26b"><span style="color:#E5E5E5">Shadow</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-nhkm"><span style="color:#0A53A8;background-color:#FFF">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-23</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">126,50</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">6,59%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">50</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">759</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-o88q"><span style="color:#473821">Sunny</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-nhkm"><span style="color:#0A53A8;background-color:#FFF">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-24</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">126,17</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">9,64%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">73</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">757</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-s26b"><span style="color:#E5E5E5">Shadow</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-nhkm"><span style="color:#0A53A8;background-color:#FFF">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-25</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">137,17</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">10,57%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">87</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">823</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-o88q"><span style="color:#473821">Sunny</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-4e1g"><span style="color:#D4EDBC;background-color:#FFF">val</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-26</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">120,17</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">9,71%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">70</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">721</span></td>
    <td class="tg-y486"><span style="color:#3D3D3D">Gravel</span></td>
    <td class="tg-s26b"><span style="color:#E5E5E5">Shadow</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-3y2x"><span style="color:#B10202;background-color:#FFF">test</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-27</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">121,83</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">6,57%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">48</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">731</span></td>
    <td class="tg-y486"><span style="color:#3D3D3D">Gravel</span></td>
    <td class="tg-s26b"><span style="color:#E5E5E5">Shadow</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-nhkm"><span style="color:#0A53A8;background-color:#FFF">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-28</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">128,00</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">9,24%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">71</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">768</span></td>
    <td class="tg-y486"><span style="color:#3D3D3D">Gravel</span></td>
    <td class="tg-s26b"><span style="color:#E5E5E5">Shadow</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-nhkm"><span style="color:#0A53A8;background-color:#FFF">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-29</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">130,67</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">14,54%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">114</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">784</span></td>
    <td class="tg-y486"><span style="color:#3D3D3D">Gravel</span></td>
    <td class="tg-s26b"><span style="color:#E5E5E5">Shadow</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-nhkm"><span style="color:#0A53A8;background-color:#FFF">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-30</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">144,33</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">7,97%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">69</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">866</span></td>
    <td class="tg-y486"><span style="color:#3D3D3D">Gravel</span></td>
    <td class="tg-o88q">Cloudy</td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-nhkm"><span style="color:#0A53A8;background-color:#FFF">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-31</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">120,17</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">15,12%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">109</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">721</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-s26b">Cloudy</td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-nhkm"><span style="color:#0A53A8;background-color:#FFF">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-32</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">120,67</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">39,23%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">284</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">724</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-s26b"><span style="color:#E5E5E5">Shadow</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-cfqi"><span style="color:#753800">Medium</span></td>
  </tr>
  <tr>
    <td class="tg-4e1g"><span style="color:#D4EDBC;background-color:#FFF">val</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-33</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">120,67</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">27,35%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">198</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">724</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-s26b"><span style="color:#E5E5E5">Shadow</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-cfqi"><span style="color:#753800">Medium</span></td>
  </tr>
  <tr>
    <td class="tg-nhkm"><span style="color:#0A53A8;background-color:#FFF">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-34</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">117,67</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">39,52%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">279</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">706</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-o88q"><span style="color:#473821">Sunny</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-d6h8"><span style="color:#FFCFC9">High</span></td>
  </tr>
  <tr>
    <td class="tg-nhkm"><span style="color:#0A53A8;background-color:#FFF">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-35</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">121,00</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">17,22%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">125</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">726</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-o88q"><span style="color:#473821">Sunny</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-d6h8"><span style="color:#FFCFC9">High</span></td>
  </tr>
  <tr>
    <td class="tg-3y2x"><span style="color:#B10202;background-color:#FFF">test</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-36</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">122,00</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">28,55%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">209</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">732</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-o88q"><span style="color:#473821">Sunny</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-d6h8"><span style="color:#FFCFC9">High</span></td>
  </tr>
  <tr>
    <td class="tg-nhkm"><span style="color:#0A53A8;background-color:#FFF">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-37</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">129,17</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">36,00%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">279</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">775</span></td>
    <td class="tg-y486"><span style="color:#3D3D3D">Gravel</span></td>
    <td class="tg-o88q"><span style="color:#473821">Sunny</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-d6h8"><span style="color:#FFCFC9">High</span></td>
  </tr>
  <tr>
    <td class="tg-nhkm"><span style="color:#0A53A8;background-color:#FFF">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-39</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">133,00</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">30,08%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">240</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">798</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-s26b">Cloudy</td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-d6h8"><span style="color:#FFCFC9">High</span></td>
  </tr>
  <tr>
    <td class="tg-nhkm"><span style="color:#0A53A8;background-color:#FFF">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-40</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">125,17</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">34,49%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">259</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">751</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-s26b"><span style="color:#E5E5E5">Shadow</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-d6h8"><span style="color:#FFCFC9">High</span></td>
  </tr>
  <tr>
    <td class="tg-nhkm"><span style="color:#0A53A8;background-color:#FFF">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-41</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">127,83</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">18,38%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">141</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">767</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-s26b"><span style="color:#E5E5E5">Shadow</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-d6h8"><span style="color:#FFCFC9">High</span></td>
  </tr>
  <tr>
    <td class="tg-nhkm"><span style="color:#0A53A8;background-color:#FFF">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-42</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">137,17</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">34,63%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">285</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">823</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-o88q"><span style="color:#473821">Sunny</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-d6h8"><span style="color:#FFCFC9">High</span></td>
  </tr>
  <tr>
    <td class="tg-nhkm"><span style="color:#0A53A8;background-color:#FFF">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-43</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">150,00</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">32,56%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">293</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">900</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-o88q"><span style="color:#473821">Sunny</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-d6h8"><span style="color:#FFCFC9">High</span></td>
  </tr>
  <tr>
    <td class="tg-3y2x"><span style="color:#B10202;background-color:#FFF">test</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-44</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">158,33</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">25,16%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">239</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">950</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-s26b"><span style="color:#E5E5E5">Shadow</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-d6h8"><span style="color:#FFCFC9">High</span></td>
  </tr>
  <tr>
    <td class="tg-nhkm"><span style="color:#0A53A8;background-color:#FFF">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-45</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">140,67</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">28,91%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">244</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">844</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-s26b"><span style="color:#E5E5E5">Shadow</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-d6h8"><span style="color:#FFCFC9">High</span></td>
  </tr>
  <tr>
    <td class="tg-nhkm"><span style="color:#0A53A8;background-color:#FFF">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-46</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">150,00</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">25,33%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">228</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">900</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-7zrl">Cloudy</td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-d6h8"><span style="color:#FFCFC9">High</span></td>
  </tr>
  <tr>
    <td class="tg-nhkm"><span style="color:#0A53A8;background-color:#FFF">train</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">ITA-47</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">148,33</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">34,61%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">308</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">890</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-o88q">Cloudy</td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-d6h8"><span style="color:#FFCFC9">High</span></td>
  </tr>
  <tr>
    <td class="tg-4e1g"><span style="color:#D4EDBC;background-color:#FFF">val</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">USA-1</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">39,00</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">71,79%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">168</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">234</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-o88q"><span style="color:#473821">Sunny</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-d6h8"><span style="color:#FFCFC9">High</span></td>
  </tr>
  <tr>
    <td class="tg-4e1g"><span style="color:#D4EDBC;background-color:#FFF">val</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">USA-2</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">56,17</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">90,50%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">305</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">337</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-o88q"><span style="color:#473821">Sunny</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-cfqi"><span style="color:#753800">Medium</span></td>
  </tr>
  <tr>
    <td class="tg-4e1g"><span style="color:#D4EDBC;background-color:#FFF">val</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">USA-3</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">63,50</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">87,66%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">334</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">381</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-o88q"><span style="color:#473821">Sunny</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-d6h8"><span style="color:#FFCFC9">High</span></td>
  </tr>
  <tr>
    <td class="tg-4e1g"><span style="color:#D4EDBC;background-color:#FFF">val</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">USA-4</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">87,83</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">77,23%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">407</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">527</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-s26b"><span style="color:#E5E5E5">Shadow</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-cfqi"><span style="color:#753800">Medium</span></td>
  </tr>
  <tr>
    <td class="tg-4e1g"><span style="color:#D4EDBC;background-color:#FFF">val</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">USA-5</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">80,83</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">70,10%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">340</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">485</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-7zrl">Cloudy</td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-4e1g"><span style="color:#D4EDBC;background-color:#FFF">val</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">USA-6</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">80,17</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">76,51%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">368</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">481</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-o88q"><span style="color:#473821">Sunny</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-4e1g"><span style="color:#D4EDBC;background-color:#FFF">val</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">USA-7</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">74,33</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">69,06%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">308</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">446</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-o88q"><span style="color:#473821">Sunny</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-4e1g"><span style="color:#D4EDBC;background-color:#FFF">val</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">USA-8</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">81,00</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">77,57%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">377</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">486</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-7zrl">Cloudy</td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-4e1g"><span style="color:#D4EDBC;background-color:#FFF">val</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">USA-9</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">80,83</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">84,54%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">410</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">485</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-o88q"><span style="color:#473821">Sunny</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
  <tr>
    <td class="tg-4e1g"><span style="color:#D4EDBC;background-color:#FFF">val</span></td>
    <td class="tg-x2c0"><span style="background-color:#FCE5CD">USA-10</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">95,00</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">89,82%</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">512</span></td>
    <td class="tg-4bam"><span style="background-color:#FFF">570</span></td>
    <td class="tg-yhwj"><span style="color:#11734B">Grass</span></td>
    <td class="tg-o88q"><span style="color:#473821">Sunny</span></td>
    <td class="tg-vp47"><span style="color:#0A53A8">Vertical</span></td>
    <td class="tg-o88q"><span style="color:#473821">Low</span></td>
  </tr>
</tbody>
</table></div>
<script charset="utf-8">var TGSort=window.TGSort||function(n){"use strict";function r(n){return n?n.length:0}function t(n,t,e,o=0){for(e=r(n);o<e;++o)t(n[o],o)}function e(n){return n.split("").reverse().join("")}function o(n){var e=n[0];return t(n,function(n){for(;!n.startsWith(e);)e=e.substring(0,r(e)-1)}),r(e)}function u(n,r,e=[]){return t(n,function(n){r(n)&&e.push(n)}),e}var a=parseFloat;function i(n,r){return function(t){var e="";return t.replace(n,function(n,t,o){return e=t.replace(r,"")+"."+(o||"").substring(1)}),a(e)}}var s=i(/^(?:\s*)([+-]?(?:\d+)(?:,\d{3})*)(\.\d*)?$/g,/,/g),c=i(/^(?:\s*)([+-]?(?:\d+)(?:\.\d{3})*)(,\d*)?$/g,/\./g);function f(n){var t=a(n);return!isNaN(t)&&r(""+t)+1>=r(n)?t:NaN}function d(n){var e=[],o=n;return t([f,s,c],function(u){var a=[],i=[];t(n,function(n,r){r=u(n),a.push(r),r||i.push(n)}),r(i)<r(o)&&(o=i,e=a)}),r(u(o,function(n){return n==o[0]}))==r(o)?e:[]}function v(n){if("TABLE"==n.nodeName){for(var a=function(r){var e,o,u=[],a=[];return function n(r,e){e(r),t(r.childNodes,function(r){n(r,e)})}(n,function(n){"TR"==(o=n.nodeName)?(e=[],u.push(e),a.push(n)):"TD"!=o&&"TH"!=o||e.push(n)}),[u,a]}(),i=a[0],s=a[1],c=r(i),f=c>1&&r(i[0])<r(i[1])?1:0,v=f+1,p=i[f],h=r(p),l=[],g=[],N=[],m=v;m<c;++m){for(var T=0;T<h;++T){r(g)<h&&g.push([]);var C=i[m][T],L=C.textContent||C.innerText||"";g[T].push(L.trim())}N.push(m-v)}t(p,function(n,t){l[t]=0;var a=n.classList;a.add("tg-sort-header"),n.addEventListener("click",function(){var n=l[t];!function(){for(var n=0;n<h;++n){var r=p[n].classList;r.remove("tg-sort-asc"),r.remove("tg-sort-desc"),l[n]=0}}(),(n=1==n?-1:+!n)&&a.add(n>0?"tg-sort-asc":"tg-sort-desc"),l[t]=n;var i,f=g[t],m=function(r,t){return n*f[r].localeCompare(f[t])||n*(r-t)},T=function(n){var t=d(n);if(!r(t)){var u=o(n),a=o(n.map(e));t=d(n.map(function(n){return n.substring(u,r(n)-a)}))}return t}(f);(r(T)||r(T=r(u(i=f.map(Date.parse),isNaN))?[]:i))&&(m=function(r,t){var e=T[r],o=T[t],u=isNaN(e),a=isNaN(o);return u&&a?0:u?-n:a?n:e>o?n:e<o?-n:n*(r-t)});var C,L=N.slice();L.sort(m);for(var E=v;E<c;++E)(C=s[E].parentNode).removeChild(s[E]);for(E=v;E<c;++E)C.appendChild(s[v+L[E-v]])})})}}n.addEventListener("DOMContentLoaded",function(){for(var t=n.getElementsByClassName("tg"),e=0;e<r(t);++e)try{v(t[e])}catch(n){}})}(document)</script>