#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
枫桥夜泊 - 简笔画生成
根据古诗《枫桥夜泊》创作一幅童趣风格的简笔画
"""

from PIL import Image, ImageDraw, ImageFont
import math

# 创建画布 (800x600, 白色背景)
width, height = 800, 600
img = Image.new('RGB', (width, height), color='white')
draw = ImageDraw.Draw(img)

# 设置颜色
night_blue = (30, 30, 60)  # 夜空深蓝
moon_yellow = (255, 255, 200)  # 月亮淡黄
water_blue = (50, 80, 120)  # 水色深蓝
boat_brown = (100, 60, 40)  # 船棕色
fire_yellow = (255, 200, 100)  # 渔火黄色
tree_brown = (80, 50, 30)  # 树干棕色
tree_red = (180, 60, 40)  # 枫叶红色
temple_gray = (120, 120, 120)  # 寺庙灰色
bird_black = (20, 20, 20)  # 乌鸦黑色

# 填充夜空背景（渐变效果，从深到浅）
for y in range(height // 2):
    alpha = y / (height // 2)
    color = (
        int(30 + alpha * 20),
        int(30 + alpha * 30),
        int(60 + alpha * 40)
    )
    draw.line([(0, y), (width, y)], fill=color)

# 绘制水面（下半部分）
water_y = height // 2
for y in range(water_y, height):
    alpha = (y - water_y) / (height - water_y)
    color = (
        int(50 + alpha * 30),
        int(80 + alpha * 40),
        int(120 + alpha * 50)
    )
    draw.line([(0, y), (width, y)], fill=color)

# 绘制月亮（弯月，左上角）
moon_x, moon_y = 100, 80
moon_size = 60
# 绘制弯月（用两个圆叠加）
draw.ellipse([moon_x, moon_y, moon_x + moon_size, moon_y + moon_size], 
             fill=moon_yellow, outline=moon_yellow)
# 用深色覆盖一部分形成弯月
draw.ellipse([moon_x + 15, moon_y - 5, moon_x + moon_size + 20, moon_y + moon_size - 5],
             fill=(30, 30, 60), outline=(30, 30, 60))

# 绘制乌鸦（两三只，简单线条）
birds = [
    (150, 100),
    (200, 120),
    (180, 140)
]
for bx, by in birds:
    # 乌鸦身体（小椭圆）
    draw.ellipse([bx - 8, by - 5, bx + 8, by + 5], fill=bird_black)
    # 乌鸦翅膀（简单三角形）
    draw.polygon([(bx - 5, by), (bx - 12, by - 8), (bx - 8, by - 3)], fill=bird_black)
    draw.polygon([(bx + 5, by), (bx + 12, by - 8), (bx + 8, by - 3)], fill=bird_black)

# 绘制水面波纹（几条简单波纹）
wave_y = water_y + 20
for i in range(5):
    y_offset = i * 30
    for x in range(0, width, 20):
        # 简单的波浪线
        points = []
        for px in range(x, min(x + 20, width)):
            py = wave_y + y_offset + int(5 * math.sin(px / 10))
            points.append((px, py))
        if len(points) > 1:
            draw.line(points, fill=(70, 100, 140), width=2)

# 绘制小船（中间偏右）
boat_x, boat_y = 500, water_y + 30
boat_width = 80
boat_height = 25
# 船身（简单弧线）
boat_points = [
    (boat_x, boat_y + boat_height),
    (boat_x + boat_width // 4, boat_y),
    (boat_x + 3 * boat_width // 4, boat_y),
    (boat_x + boat_width, boat_y + boat_height)
]
draw.polygon(boat_points, fill=boat_brown, outline=(60, 40, 25))
# 船内简单线条
draw.line([(boat_x + boat_width // 4, boat_y + boat_height // 2),
           (boat_x + 3 * boat_width // 4, boat_y + boat_height // 2)],
          fill=(60, 40, 25), width=2)

# 绘制渔火（小点表示）
fire_positions = [
    (boat_x + boat_width // 3, boat_y + 5),
    (boat_x + 2 * boat_width // 3, boat_y + 5)
]
for fx, fy in fire_positions:
    # 渔火（小圆点，带光晕效果）
    draw.ellipse([fx - 4, fy - 4, fx + 4, fy + 4], fill=fire_yellow)
    draw.ellipse([fx - 2, fy - 2, fx + 2, fy + 2], fill=(255, 255, 150))

# 绘制岸边枫树（左侧，几棵简笔）
trees = [
    (150, water_y - 80, 40),  # x, y, 高度
    (100, water_y - 60, 35),
    (200, water_y - 70, 45)
]
for tx, ty, th in trees:
    # 树干（简单竖线）
    draw.rectangle([tx - 3, ty, tx + 3, ty + th], fill=tree_brown)
    # 枫叶（简单圆形，红色）
    leaf_size = 15
    for leaf_offset in [(0, -10), (-12, -5), (12, -5), (-8, 0), (8, 0)]:
        lx, ly = tx + leaf_offset[0], ty + leaf_offset[1]
        draw.ellipse([lx - leaf_size//2, ly - leaf_size//2,
                     lx + leaf_size//2, ly + leaf_size//2],
                    fill=tree_red, outline=(140, 40, 30))

# 绘制远处寒山寺（简化轮廓，右侧）
temple_x, temple_y = 600, 100
temple_width = 120
temple_height = 80

# 寺庙主体（简单矩形）
draw.rectangle([temple_x, temple_y + 30, temple_x + temple_width, temple_y + temple_height],
               fill=temple_gray, outline=(80, 80, 80))

# 寺庙屋顶（简单三角形）
roof_points = [
    (temple_x - 10, temple_y + 30),
    (temple_x + temple_width // 2, temple_y),
    (temple_x + temple_width + 10, temple_y + 30)
]
draw.polygon(roof_points, fill=(100, 100, 100), outline=(70, 70, 70))

# 寺庙门（简单矩形）
door_width = 20
door_height = 30
draw.rectangle([temple_x + temple_width // 2 - door_width // 2,
                temple_y + temple_height - door_height,
                temple_x + temple_width // 2 + door_width // 2,
                temple_y + temple_height],
               fill=(60, 60, 60))

# 绘制钟（简笔，在寺庙旁边）
bell_x, bell_y = temple_x + temple_width + 20, temple_y + 40
# 钟身（简单椭圆）
draw.ellipse([bell_x - 15, bell_y - 20, bell_x + 15, bell_y + 20],
             fill=(140, 140, 140), outline=(100, 100, 100))
# 钟顶（小圆）
draw.ellipse([bell_x - 8, bell_y - 25, bell_x + 8, bell_y - 15],
             fill=(120, 120, 120))
# 钟摆（简单线条）
draw.line([(bell_x, bell_y + 20), (bell_x, bell_y + 35)], fill=(100, 100, 100), width=3)
draw.ellipse([bell_x - 5, bell_y + 33, bell_x + 5, bell_y + 38], fill=(100, 100, 100))

# 添加一些星星点缀（小点）
stars = [(250, 60), (300, 80), (350, 50), (400, 70), (450, 55)]
for sx, sy in stars:
    draw.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=(255, 255, 200))

# 保存图片
output_path = '/workspace/fengqiao_yebo.png'
img.save(output_path)
print(f"画作已保存到: {output_path}")
