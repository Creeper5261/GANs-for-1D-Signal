from PIL import Image
import imageio
import os


folder_path = './img/wgan'
output_gif_path = 'output.gif'


image_files = [os.path.join(folder_path, file) for file in sorted(os.listdir(folder_path)) if file.endswith('.png')]


images = [Image.open(image_file) for image_file in image_files]


frame_duration = 2


images[0].save(output_gif_path, save_all=True, append_images=images[1:], loop=0, duration=frame_duration)

print("GIF生成完成！")
