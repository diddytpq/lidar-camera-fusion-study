# lidar-camera-fusion-study
Study object detection based lidar and camera

## 1. Install spconv 1.2.1

* Edit .bashrc

	```
	export PATH=/usr/bin/cmake:$PATH
	export PATH=/usr/include/boost:$PATH

	export PYTHONPATH=$PYTHONPATH:/home/"work space path"/second.pytorch/
	```

* Edit CMakeLists.txt

	```
	add line 6

	set(CMAKE_CUDA_COMPILER "/usr/local/cuda/bin/nvcc")

* Edit torch code  (~/anaconda3/envs/{env_name}}/lib/{env_python_version}/site-packages/torch/share/cmake/Caffe2/public/cuda.cmake)

	```
	https://blog.csdn.net/epnine/article/details/124464206
	```

* Install spconv
	```
	python setup.py bdist_wheel
	cd /dist
	pip install file.wheel
	```

## 2. Run Second
	cd lidar_based/second.pytorch/second

* Make train data
	```
	python create_data.py kitti_data_prep --root_path=./data/ImageSets/kitti_data/
	
	```
* Train model
	```
	python ./pytorch/train.py train --config_path=./configs/all.fhd.config --model_dir=./train_model/all_model
	```



## 3. Run pointPillars
	
	cd lidar_based
	python test.py --ckpt pretrained/epoch_160.pth --pc_path dataset/testing/velodyne/000000.bin

	python test.py --ckpt pretrained/epoch_160.pth --pc_path dataset/testing/velodyne/000000.bin --calib_path dataset/testing/calib/000000.txt --img_path dataset/testing/image_2/000000.png
	
	python test_custom.py --ckpt pretrained/epoch_160.pth --pc_folder_path dataset/testing/velodyne/

## Reference
	
	point pillars -> https://github.com/zhulf0804/PointPillars
	PillarNet -> https://github.com/agent-sgs/PillarNet
