# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# compile CUDA with /usr/local/cuda/bin/nvcc
CUDA_FLAGS = "--expt-relaxed-constexpr" -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -gencode arch=compute_86,code=sm_86 -O3 -DNDEBUG -Xcompiler=-fPIC   -std=c++14

CUDA_DEFINES = -DPYTORCH_VERSION=11000 -DTV_CUDA

CUDA_INCLUDES = -I/home/drcl/workspace/lidar-camera-fusion-study/lidar_based/spconv-1.2.1/include 
