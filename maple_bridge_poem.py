#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
枫桥夜泊 - 简笔画生成器
根据张继的经典诗歌创作简笔水墨风格的图画
"""

from PIL import Image, ImageDraw, ImageFont
import random

def draw_maple_bridge_night():
    # 创建画布 - 800x600像素，深灰色背景（夜色）
    width, height = 800, 600
    img = Image.new('RGB', (width, height), color='#1a1a2e')
    draw = ImageDraw.Draw(img)
    
    # 1. 绘制夜空 - 弯月
    moon_x, moon_y = 650, 80
    draw.ellipse([moon_x-30, moon_y-30, moon_x+30, moon_y+30], 
                 fill='#f0e68c', outline='#e6d87a', width=2)
    # 月亮的阴影部分（弯月效果）
    draw.ellipse([moon_x-20, moon_y-30, moon_x+40, moon_y+30], 
                 fill='#1a1a2e', outline='#1a1a2e')
    
    # 2. 绘制乌鸦（简笔画风格）
    def draw_crow(x, y, size=15):
        # 身体
        draw.ellipse([x-size//2, y-size//3, x+size//2, y+size//3], 
                    fill='#2d2d2d', outline='#000000', width=1)
        # 翅膀（简单的V形）
        draw.line([x-size, y, x-size//3, y+size//4], fill='#2d2d2d', width=3)
        draw.line([x+size, y, x+size//3, y+size//4], fill='#2d2d2d', width=3)
    
    draw_crow(550, 100)
    draw_crow(600, 120)
    draw_crow(680, 110)
    
    # 3. 绘制远处的寒山寺轮廓
    temple_base = 480
    # 寺庙墙壁
    draw.rectangle([50, temple_base-80, 180, temple_base], 
                   fill='#3d3d5c', outline='#5a5a7a', width=2)
    # 寺庙屋顶（简单的三角形）
    draw.polygon([30, temple_base-80, 115, temple_base-120, 200, temple_base-80], 
                fill='#4a4a6a', outline='#6a6a8a', width=2)
    # 钟楼
    draw.rectangle([90, temple_base-100, 130, temple_base-80], 
                   fill='#3d3d5c', outline='#5a5a7a', width=2)
    # 钟（简笔画）
    draw.arc([105, temple_base-95, 115, temple_base-85], 
            start=0, end=180, fill='#8b8b9b', width=2)
    
    # 4. 绘制水面河流
    water_y = temple_base + 20
    # 水面基础
    draw.rectangle([0, water_y, width, height], fill='#0f1e2e')
    
    # 绘制波纹（简单的曲线）
    for i in range(5):
        y_pos = water_y + i * 20 + 10
        for j in range(0, width, 60):
            x_start = j + random.randint(-5, 5)
            x_end = x_start + 40
            draw.arc([x_start, y_pos-5, x_end, y_pos+5], 
                    start=180, end=0, fill='#2a3a4a', width=2)
    
    # 5. 绘制岸边枫树（简笔风格）
    def draw_simple_tree(x, y):
        # 树干
        draw.line([x, y, x, y-60], fill='#4a4a4a', width=5)
        # 树枝（简单的Y形）
        draw.line([x, y-40, x-20, y-70], fill='#4a4a4a', width=3)
        draw.line([x, y-40, x+20, y-70], fill='#4a4a4a', width=3)
        draw.line([x, y-50, x-15, y-75], fill='#4a4a4a', width=2)
        draw.line([x, y-50, x+15, y-75], fill='#4a4a4a', width=2)
        # 树叶（简单的小圆圈）
        for dx, dy in [(-20, -70), (20, -70), (0, -60), (-15, -75), (15, -75)]:
            draw.ellipse([x+dx-8, y+dy-8, x+dx+8, y+dy+8], 
                        fill='#8b4513', outline='#a0522d', width=1)
    
    draw_simple_tree(220, temple_base)
    draw_simple_tree(280, temple_base + 10)
    draw_simple_tree(340, temple_base - 5)
    
    # 6. 绘制小船
    boat_x, boat_y = 450, 540
    # 船体（简单的弧形）
    draw.arc([boat_x-60, boat_y-20, boat_x+60, boat_y+20], 
            start=180, end=360, fill='#5a4a3a', width=4)
    draw.line([boat_x-55, boat_y, boat_x+55, boat_y], fill='#5a4a3a', width=4)
    # 船舱（小矩形）
    draw.rectangle([boat_x-20, boat_y-25, boat_x+20, boat_y-5], 
                   fill='#6a5a4a', outline='#7a6a5a', width=2)
    
    # 渔火（小亮点）
    fire_x, fire_y = boat_x, boat_y - 15
    draw.ellipse([fire_x-5, fire_y-5, fire_x+5, fire_y+5], 
                fill='#ff6600', outline='#ff8800', width=1)
    # 火光效果
    draw.ellipse([fire_x-10, fire_y-10, fire_x+10, fire_y+10], 
                fill='#ff880033', outline=None)
    
    # 7. 添加诗句（可选）
    try:
        # 尝试使用中文字体
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
    except:
        font = ImageFont.load_default()
    
    poem_text = "枫桥夜泊"
    draw.text((20, 20), poem_text, fill='#d0d0d0', font=font)
    
    # 添加更多星星点缀夜空
    for _ in range(30):
        star_x = random.randint(10, width-10)
        star_y = random.randint(10, temple_base-150)
        star_size = random.randint(1, 2)
        draw.ellipse([star_x, star_y, star_x+star_size, star_y+star_size], 
                    fill='#ffffff')
    
    # 保存图片
    output_path = '/workspace/maple_bridge_night_poem.png'
    img.save(output_path)
    print(f"图画已生成：{output_path}")
    print("画面包含：")
    print("  🌙 夜空中的弯月与乌鸦")
    print("  🏯 远处的寒山寺与钟楼")
    print("  🌊 宁静的水面波纹")
    print("  🍁 岸边的枫树")
    print("  🚤 停泊的小船与渔火")
    print("\n意境：宁静、安详、夜色朦胧")
    
    return output_path

if __name__ == "__main__":
    draw_maple_bridge_night()
