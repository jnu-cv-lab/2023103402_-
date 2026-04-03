import cv2
import matplotlib.pyplot as plt

def load_image(image_path):
    """读取图像"""
    img = cv2.imread(image_path)
    if img is None:
        print("图片读取失败")
        exit()
    return img

def print_image_info(img):
    """输出图像基本信息"""
    h, w = img.shape[:2]
    channels = img.shape[2] if len(img.shape) == 3 else 1
    dtype = img.dtype
    
    print("===== 图像基本信息 =====")
    print(f"宽度 : {w}")
    print(f"高度 : {h}")
    print(f"通道数 : {channels}")
    print(f"数据类型 : {dtype}")
    return h, w, channels, dtype

def show_save_original(img_rgb, save_path="output/original_image.png"):
    """显示并保存原图"""
    plt.figure(figsize=(8, 6))
    plt.imshow(img_rgb)
    plt.axis('off')
    plt.title("Original Image")
    plt.savefig(save_path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"原图已保存为 {save_path}")

def convert_to_grayscale(img):
    """转换为灰度图"""
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def show_save_grayscale(img_gray, save_path="output/grayscale_image.png"):
    """显示并保存灰度图"""
    plt.figure(figsize=(8, 6))
    plt.imshow(img_gray, cmap='gray')
    plt.axis('off')
    plt.title("Grayscale Image")
    plt.savefig(save_path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"灰度图已保存为 {save_path}")

def save_grayscale_result(img_gray, save_path="output/grayscale_result.jpg"):
    """保存灰度图结果"""
    cv2.imwrite(save_path, img_gray)
    print(f"灰度图结果已保存为 {save_path}")