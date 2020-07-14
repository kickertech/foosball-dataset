FROM nvidia/cuda:11.0-cudnn8-devel-rc

ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /app

RUN apt update
RUN apt install -y \
	pkg-config git build-essential libopencv-dev vim wget curl

# build darknet
RUN git clone https://github.com/AlexeyAB/darknet.git
WORKDIR /app/darknet
RUN make OPENCV=1 GPU=1 AVX=1 OPENMP=1 CUDNN=1 OPENMP=1 CUDNN_HALF=1 -j $(nproc)
RUN chmod +x darknet && mv ./darknet /bin/darknet

RUN apt install -y \
	python3

RUN ln -s /usr/bin/python3 /usr/bin/python
