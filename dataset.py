from torchvision.datasets import VOCDetection

dataset = VOCDetection(
    root="data/voc",
    year="2012",
    image_set="trainval",
    download=True
)



