import os
from PIL import Image, ImageDraw

print("=" * 60)
print("开始创建项目所需的图片...")
print("=" * 60)

os.makedirs('static/images', exist_ok=True)
print("\n✅ static/images 文件夹已准备好")


# ========== 生成 Logo ==========
def create_logo():
    print("\n📝 正在创建 logo.png...")

    img = Image.new('RGBA', (200, 200), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    # 绘制蓝色圆形背景
    draw.ellipse([10, 10, 190, 190], fill=(21, 101, 192, 255), outline=(13, 71, 161, 255), width=3)

    # 绘制白色矩形（代表投资图表）
    draw.rectangle([50, 80, 150, 140], fill=(255, 255, 255, 255))
    draw.rectangle([60, 120, 80, 140], fill=(21, 101, 192, 255))
    draw.rectangle([90, 100, 110, 140], fill=(21, 101, 192, 255))
    draw.rectangle([120, 80, 140, 140], fill=(21, 101, 192, 255))

    img.save('static/images/logo.png')
    print("✅ logo.png 已创建 (200x200px)")


# ========== 生成 Hero 图片 ==========
def create_hero_image():
    print("\n📝 正在创建 hero-image.jpg...")

    # 创建蓝色渐变背景图片
    width, height = 600, 400
    img = Image.new('RGB', (width, height))
    pixels = img.load()

    # 蓝色渐变（浅蓝 → 深蓝）
    start_color = (227, 242, 253)  # 浅蓝
    end_color = (21, 101, 192)  # 深蓝

    for y in range(height):
        ratio = y / height
        r = int(start_color[0] + (end_color[0] - start_color[0]) * ratio)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * ratio)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * ratio)

        for x in range(width):
            pixels[x, y] = (r, g, b)

    # 保存图片
    img.save('static/images/hero-image.jpg', quality=85)
    print("✅ hero-image.jpg 已创建 (600x400px)")


if __name__ == "__main__":
    try:
        create_logo()
        create_hero_image()

        print("\n" + "=" * 60)
        print("🎉 所有图片已成功创建！")
        print("=" * 60)
        print("\n📁 已生成的图片：")
        print("   1. logo.png (200x200px)")
        print("   2. hero-image.jpg (600x400px)")
        print("\n✅ 所有图片已保存到：static/images/")
        print("\n现在可以运行: python app.py")
        print("访问: http://localhost:5000")
        print("=" * 60)

    except Exception as e:
        print(f"\n❌ 发生错误: {e}")
        print("请确保已安装 Pillow: pip install Pillow")