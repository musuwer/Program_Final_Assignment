from PIL import Image
import os
import frozen_dir

SUPER_DIR = frozen_dir.app_path() # 当前项目的绝对路径

def strip_icc_profile(src_dir):
    for filename in os.listdir(src_dir):
        if filename.lower().endswith('.png'):
            filepath = os.path.join(src_dir, filename)
            try:
                im = Image.open(filepath)
                # 明确去掉 icc_profile
                im.save(filepath, 'PNG', icc_profile=None)
                print(f"已修正：{filename}")
            except Exception as e:
                print(f"{filename} 处理出错: {e}")

if __name__ == '__main__':
    folder = SUPER_DIR + r'/res/style/img'
    strip_icc_profile(folder)
