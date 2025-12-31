#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成《枫桥夜泊》水彩笔风格画作
"""

from PIL import Image, ImageDraw, ImageFilter
import math
import random

def create_watercolor_painting():
    # 创建画布 - 水彩纸质感
    width, height = 1200, 800
    img = Image.new('RGB', (width, height), color=(245, 240, 230))  # 米黄色水彩纸底色
    
    draw = ImageDraw.Draw(img)
    
    # 添加一些纹理效果（模拟水彩纸）
    for _ in range(500):
        x = random.randint(0, width)
        y = random.randint(0, height)
        r = random.randint(1, 3)
        color = (240 + random.randint(-5, 5), 235 + random.randint(-5, 5), 225 + random.randint(-5, 5))
        draw.ellipse([x-r, y-r, x+r, y+r], fill=color)
    
    # 1. 夜空 - 深蓝色渐变
    sky_color = (30, 40, 60)  # 深蓝灰色
    for y in range(0, height // 2):
        alpha = y / (height // 2)
        color = (
            int(245 * (1 - alpha) + sky_color[0] * alpha),
            int(240 * (1 - alpha) + sky_color[1] * alpha),
            int(230 * (1 - alpha) + sky_color[2] * alpha)
        )
        draw.rectangle([0, y, width, y+1], fill=color)
    
    # 2. 一弯弯月亮（下弦月）
    moon_x, moon_y = 200, 150
    moon_size = 80
    # 绘制月亮（简单的弯月形状）
    moon_color = (255, 250, 200)  # 淡黄色
    # 先画一个圆
    draw.ellipse([moon_x-moon_size//2, moon_y-moon_size//2, 
                  moon_x+moon_size//2, moon_y+moon_size//2], 
                 fill=moon_color, outline=None)
    # 用天空色覆盖一部分形成弯月
    overlay_color = (
        int(245 * 0.3 + sky_color[0] * 0.7),
        int(240 * 0.3 + sky_color[1] * 0.7),
        int(230 * 0.3 + sky_color[2] * 0.7)
    )
    draw.ellipse([moon_x-moon_size//2+15, moon_y-moon_size//2, 
                  moon_x+moon_size//2+15, moon_y+moon_size//2], 
                 fill=overlay_color, outline=None)
    
    # 3. 两三只乌鸦（简笔画风格）
    crow_color = (20, 20, 20)  # 黑色
    # 乌鸦1
    crow1_x, crow1_y = 300, 120
    # 乌鸦身体（椭圆）
    draw.ellipse([crow1_x-15, crow1_y-8, crow1_x+15, crow1_y+8], fill=crow_color)
    # 乌鸦翅膀（简单三角形）
    draw.polygon([(crow1_x-10, crow1_y), (crow1_x-25, crow1_y-15), (crow1_x-20, crow1_y-5)], fill=crow_color)
    draw.polygon([(crow1_x+10, crow1_y), (crow1_x+25, crow1_y-15), (crow1_x+20, crow1_y-5)], fill=crow_color)
    
    # 乌鸦2
    crow2_x, crow2_y = 450, 100
    draw.ellipse([crow2_x-12, crow2_y-6, crow2_x+12, crow2_y+6], fill=crow_color)
    draw.polygon([(crow2_x-8, crow2_y), (crow2_x-20, crow2_y-12), (crow2_x-16, crow2_y-4)], fill=crow_color)
    draw.polygon([(crow2_x+8, crow2_y), (crow2_x+20, crow2_y-12), (crow2_x+16, crow2_y-4)], fill=crow_color)
    
    # 乌鸦3
    crow3_x, crow3_y = 550, 130
    draw.ellipse([crow3_x-10, crow3_y-5, crow3_x+10, crow3_y+5], fill=crow_color)
    draw.polygon([(crow3_x-7, crow3_y), (crow3_x-18, crow3_y-10), (crow3_x-14, crow3_y-3)], fill=crow_color)
    draw.polygon([(crow3_x+7, crow3_y), (crow3_x+18, crow3_y-10), (crow3_x+14, crow3_y-3)], fill=crow_color)
    
    # 4. 水面河流 - 几条简单波纹
    water_y = height // 2 + 50
    water_color = (40, 60, 80)  # 深蓝灰色水面
    # 填充水面区域
    draw.rectangle([0, water_y, width, height], fill=water_color)
    
    # 添加波纹（简单的波浪线）
    wave_color = (60, 80, 100)  # 稍亮的波纹
    for wave_offset in range(0, height - water_y, 40):
        y = water_y + wave_offset
        points = []
        for x in range(0, width, 20):
            wave_height = 5 * math.sin(x / 30 + wave_offset / 10)
            points.append((x, y + wave_height))
        if len(points) > 1:
            for i in range(len(points) - 1):
                draw.line([points[i], points[i+1]], fill=wave_color, width=2)
    
    # 5. 小船 - 停在水上的小船
    boat_x, boat_y = width // 2 - 100, water_y - 20
    boat_color = (60, 40, 20)  # 棕色
    # 船身（简单的弧形）
    boat_width = 120
    boat_height = 30
    # 船底（弧形）
    boat_points = [
        (boat_x, boat_y + boat_height),
        (boat_x + boat_width // 4, boat_y + boat_height - 10),
        (boat_x + boat_width // 2, boat_y + boat_height - 15),
        (boat_x + 3 * boat_width // 4, boat_y + boat_height - 10),
        (boat_x + boat_width, boat_y + boat_height)
    ]
    draw.polygon(boat_points, fill=boat_color, outline=(40, 25, 15), width=2)
    
    # 6. 渔火 - 用小点表示（黄色小点）
    fire_color = (255, 220, 100)  # 温暖的黄色
    # 在船上有几个小点表示渔火
    fire_positions = [
        (boat_x + 30, boat_y + 10),
        (boat_x + 60, boat_y + 8),
        (boat_x + 90, boat_y + 12)
    ]
    for fx, fy in fire_positions:
        # 绘制光晕效果
        for r in range(8, 0, -2):
            alpha = r / 8
            glow_color = (
                int(fire_color[0] * alpha + boat_color[0] * (1 - alpha)),
                int(fire_color[1] * alpha + boat_color[1] * (1 - alpha)),
                int(fire_color[2] * alpha + boat_color[2] * (1 - alpha))
            )
            draw.ellipse([fx-r, fy-r, fx+r, fy+r], fill=glow_color)
    
    # 7. 岸边 - 几棵枫树简笔表示
    tree_base_x = 100
    tree_base_y = water_y
    tree_color = (40, 60, 30)  # 深绿色/棕色
    
    # 枫树1
    tree1_x = tree_base_x
    # 树干
    draw.rectangle([tree1_x-8, tree_base_y-80, tree1_x+8, tree_base_y], fill=(50, 30, 20))
    # 树冠（简单的圆形，但用枫叶形状的点）
    for _ in range(30):
        leaf_x = tree1_x + random.randint(-40, 40)
        leaf_y = tree_base_y - 100 + random.randint(-30, 30)
        if (leaf_x - tree1_x)**2 + (leaf_y - (tree_base_y - 100))**2 < 1600:
            # 简单的枫叶形状（小点）
            draw.ellipse([leaf_x-3, leaf_y-3, leaf_x+3, leaf_y+3], fill=(120, 40, 20))  # 红色枫叶
    
    # 枫树2
    tree2_x = tree_base_x + 150
    draw.rectangle([tree2_x-6, tree_base_y-60, tree2_x+6, tree_base_y], fill=(50, 30, 20))
    for _ in range(20):
        leaf_x = tree2_x + random.randint(-30, 30)
        leaf_y = tree_base_y - 80 + random.randint(-25, 25)
        if (leaf_x - tree2_x)**2 + (leaf_y - (tree_base_y - 80))**2 < 900:
            draw.ellipse([leaf_x-2, leaf_y-2, leaf_x+2, leaf_y+2], fill=(140, 50, 25))
    
    # 枫树3（在右侧）
    tree3_x = width - 150
    draw.rectangle([tree3_x-7, tree_base_y-70, tree3_x+7, tree_base_y], fill=(50, 30, 20))
    for _ in range(25):
        leaf_x = tree3_x + random.randint(-35, 35)
        leaf_y = tree_base_y - 90 + random.randint(-28, 28)
        if (leaf_x - tree3_x)**2 + (leaf_y - (tree_base_y - 90))**2 < 1225:
            draw.ellipse([leaf_x-3, leaf_y-3, leaf_x+3, leaf_y+3], fill=(130, 45, 22))
    
    # 8. 远处 - 简化的寒山寺轮廓
    temple_x = width - 300
    temple_y = height // 3
    temple_color = (80, 70, 60)  # 灰色
    
    # 寺庙主体（简单的矩形）
    temple_width = 100
    temple_height = 80
    draw.rectangle([temple_x, temple_y, temple_x + temple_width, temple_y + temple_height], 
                   fill=temple_color, outline=(60, 50, 40), width=2)
    
    # 寺庙屋顶（三角形）
    roof_points = [
        (temple_x - 10, temple_y),
        (temple_x + temple_width // 2, temple_y - 30),
        (temple_x + temple_width + 10, temple_y)
    ]
    draw.polygon(roof_points, fill=(100, 80, 70), outline=(80, 60, 50), width=2)
    
    # 9. 钟 - 简笔画
    bell_x = temple_x + temple_width + 50
    bell_y = temple_y + 20
    bell_color = (100, 90, 80)
    # 钟身（倒U形）
    bell_width = 30
    bell_height = 40
    # 钟的上部（弧形）
    draw.arc([bell_x - bell_width//2, bell_y, bell_x + bell_width//2, bell_y + bell_height], 
             start=0, end=180, fill=bell_color, width=4)
    # 钟的下部（开口）
    draw.line([bell_x - bell_width//2, bell_y + bell_height, 
               bell_x + bell_width//2, bell_y + bell_height], fill=bell_color, width=4)
    # 钟的悬挂点
    draw.ellipse([bell_x - 5, bell_y - 5, bell_x + 5, bell_y + 5], fill=bell_color)
    
    # 添加一些水彩晕染效果（模糊处理）
    img = img.filter(ImageFilter.GaussianBlur(radius=1))
    
    # 添加一些随机的水彩笔触效果
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    
    # 在水面添加一些水彩晕染
    for _ in range(20):
        x = random.randint(0, width)
        y = random.randint(water_y, height)
        r = random.randint(20, 40)
        alpha = random.randint(10, 30)
        color = (random.randint(50, 80), random.randint(70, 100), random.randint(90, 120), alpha)
        overlay_draw.ellipse([x-r, y-r, x+r, y+r], fill=color)
    
    # 合并图层
    img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
    
    return img

if __name__ == '__main__':
    print("正在生成《枫桥夜泊》水彩画...")
    painting = create_watercolor_painting()
    output_path = '/workspace/fengqiao_yebo_painting.png'
    painting.save(output_path, 'PNG')
    print(f"画作已保存到: {output_path}")
    print("完成！")
