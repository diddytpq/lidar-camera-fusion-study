import argparse
import cv2
import numpy as np
import os
import pdb

import torch
import torch.nn as nn
import torch.nn.functional as F
from model.anchors import Anchors, anchor_target, anchors2bboxes
from ops import Voxelization, nms_cuda
from utils import limit_period


def point_range_filter(pts, point_range=[0, -39.68, -3, 69.12, 39.68, 1]):
    '''
    data_dict: dict(pts, gt_bboxes_3d, gt_labels, gt_names, difficulty)
    point_range: [x1, y1, z1, x2, y2, z2]
    논문에 표기된 대로 car, pedstrian cyclist를 검출하는 포인터 범위
    '''
    flag_x_low = pts[:, 0] > point_range[0] # 0
    flag_y_low = pts[:, 1] > point_range[1] # -39.68
    flag_z_low = pts[:, 2] > point_range[2] # -3
    flag_x_high = pts[:, 0] < point_range[3] # 69.12
    flag_y_high = pts[:, 1] < point_range[4] # 39.68
    flag_z_high = pts[:, 2] < point_range[5] # 1
    keep_mask = flag_x_low & flag_y_low & flag_z_low & flag_x_high & flag_y_high & flag_z_high
    pts = pts[keep_mask]
    return pts 


voxel_size=[0.16, 0.16, 4]
point_cloud_range=[0, -39.68, -3, 69.12, 39.68, 1]
max_num_points=32
max_voxels=(16000, 40000)

voxel_layer = Voxelization(voxel_size=voxel_size, #voxel_size=[0.16, 0.16, 4],
                                point_cloud_range=point_cloud_range, #point_cloud_range=[0, -39.68, -3, 69.12, 39.68, 1],
                                max_num_points=max_num_points,  #max_num_points=32,
                                max_voxels=max_voxels) #max_voxels=(40000)):


pc_file_list = sorted(os.listdir("dataset/testing/velodyne/"))

input_pc_path = "dataset/testing/velodyne/" + pc_file_list[3]

suffix = os.path.splitext(input_pc_path)[1]

input_pc = np.fromfile(input_pc_path, dtype=np.float32).reshape(-1, 4)

input_pc_fillered = point_range_filter(input_pc)

pc_torch = torch.from_numpy(input_pc_fillered)


for i, pts in enumerate([pc_torch]):
    # print(pts.new_zeros())
    voxels_out, coors_out, num_points_per_voxel_out = voxel_layer(pts)

print(voxels_out.shape)
print(coors_out.shape)
print(num_points_per_voxel_out.shape)

print(voxels_out[0])
print(coors_out[0])
print(num_points_per_voxel_out[0])