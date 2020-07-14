# Prerequisites
You have two options to train the model:

### via docker
This is supported on linux. Windows support is iffy! See [here](https://github.com/NVIDIA/nvidia-docker/wiki/Frequently-Asked-Questions#is-microsoft-windows-supported), [wsl support](https://developer.nvidia.com/cuda/wsl) is in dev preview.

To access the GPU through docker you must have a fairly recent docker version (19.03) and install the [nvidia-container-toolkit](https://github.com/NVIDIA/nvidia-docker). There's a deprecated package `nvidia-docker2` - don't use that.

```sh
# run this from the root directory
$ make train-docker
```

### training on the host
install:
* [AlexeyAB/darknet](https://github.com/AlexeyAB/darknet.git) and its dependencies
* [cuda](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)

And run darknet in the export directory

```sh
# run this from the root directory
$ make train
```

### Frequest Issues

* make sure that the nvidia driver versions match using `nvidia-smi`
