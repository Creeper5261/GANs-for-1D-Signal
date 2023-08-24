from PIL import Image
import imageio
import os

# 定义文件夹路径和输出GIF的文件名
folder_path = './img/wgan'
output_gif_path = 'output.gif'

# 获取文件夹中所有图片文件的路径，按照字典序排序
image_files = [os.path.join(folder_path, file) for file in sorted(os.listdir(folder_path)) if file.endswith('.png')]

# 用PIL打开所有图片
images = [Image.open(image_file) for image_file in image_files]

# 调整每帧之间的持续时间
frame_duration = 2  # 每帧持续时间，单位为毫秒

# 将帧保存为GIF
images[0].save(output_gif_path, save_all=True, append_images=images[1:], loop=0, duration=frame_duration)

print("GIF生成完成！")
