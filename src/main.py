import cv2
import matplotlib.pyplot as plt
# 直接用相对导入
import image_utils

# 切换matplotlib后端
plt.switch_backend('Agg')

def main():
    # 1. 读取图像（路径：从src回到根目录，再进data）
    img = image_utils.load_image("../data/_20231211070702.jpg")
    
    # 2. 输出图像基本信息
    image_utils.print_image_info(img)
    
    # 3. 转换为RGB（matplotlib显示用）
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # 4. 显示并保存原图
    image_utils.show_save_original(img_rgb, "../output/original_image.png")
    
    # 5. 转换为灰度图
    img_gray = image_utils.convert_to_grayscale(img)
    
    # 6. 显示并保存灰度图
    image_utils.show_save_grayscale(img_gray, "../output/grayscale_image.png")
    
    # 7. 保存灰度图结果
    image_utils.save_grayscale_result(img_gray, "../output/grayscale_result.jpg")

if __name__ == "__main__":
    # 自动创建output文件夹
    import os
    os.makedirs("../output", exist_ok=True)
    main()