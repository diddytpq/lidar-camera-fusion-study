# lidar-camera-fusion-study
Study object detection based lidar and camera

## Run pointPillars
	
	cd lidar_based
	python test.py --ckpt pretrained/epoch_160.pth --pc_path dataset/testing/velodyne/000000.bin

	python test.py --ckpt pretrained/epoch_160.pth --pc_path dataset/testing/velodyne/000000.bin --calib_path dataset/testing/calib/000000.txt --img_path dataset/testing/image_2/000000.png
	
	python test_custom.py --ckpt pretrained/epoch_160.pth --pc_folder_path dataset/testing/velodyne/

## Reference
	
	point pillars -> https://github.com/zhulf0804/PointPillars
	PillarNet -> https://github.com/agent-sgs/PillarNet
