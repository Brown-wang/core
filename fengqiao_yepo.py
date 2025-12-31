#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
枫桥夜泊 - 儿童简笔画风格
唐·张继
月落乌啼霜满天，江枫渔火对愁眠。
姑苏城外寒山寺，夜半钟声到客船。
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Arc, Polygon, Circle, Ellipse, FancyBboxPatch
import numpy as np

# 设置中文字体支持
plt.rcParams['font.family'] = ['WenQuanYi Zen Hei', 'Noto Sans CJK JP', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# 创建画布 - 深蓝夜空背景
fig, ax = plt.subplots(1, 1, figsize=(14, 10))
fig.patch.set_facecolor('#1a1a3e')  # 深蓝夜色

# 设置坐标轴
ax.set_xlim(0, 100)
ax.set_ylim(0, 70)
ax.set_aspect('equal')
ax.axis('off')

# 背景渐变效果 - 夜空
for i in range(70, 30, -1):
    alpha = 0.02
    color_val = 0.05 + (70 - i) * 0.003
    ax.axhspan(i-1, i, color=(color_val, color_val, color_val + 0.15), alpha=0.5)

# ============ 1. 弯月亮 ============
def draw_crescent_moon(ax, x, y, size=5):
    # 外圆（月亮主体）
    outer = Circle((x, y), size, fill=True, 
                   facecolor='#fffacd', edgecolor='#ffd700', linewidth=2)
    ax.add_patch(outer)
    # 内圆（遮挡部分）- 创造弯月效果
    inner = Circle((x + size * 0.6, y + size * 0.3), size * 0.9, 
                   fill=True, facecolor='#1a1a3e', edgecolor='none')
    ax.add_patch(inner)

draw_crescent_moon(ax, 15, 58, 4)

# ============ 2. 乌鸦（简笔画风格）============
def draw_crow(ax, x, y, scale=1, direction=1):
    # 乌鸦身体 - 简单的V形翅膀
    wing_span = 3 * scale
    # 翅膀
    ax.plot([x - wing_span * direction, x, x + wing_span * direction], 
            [y + 0.5, y - 0.5, y + 0.5], 
            color='#2d2d2d', linewidth=2.5, solid_capstyle='round')
    # 小点表示头
    ax.plot(x, y - 0.5, 'o', color='#2d2d2d', markersize=3 * scale)

# 画三只乌鸦
draw_crow(ax, 25, 55, 0.8, 1)
draw_crow(ax, 32, 52, 0.6, -1)
draw_crow(ax, 28, 48, 0.5, 1)

# ============ 3. 星星点缀 ============
np.random.seed(42)
for _ in range(15):
    star_x = np.random.uniform(5, 95)
    star_y = np.random.uniform(40, 65)
    star_size = np.random.uniform(1, 3)
    ax.plot(star_x, star_y, '*', color='#fffacd', markersize=star_size, alpha=0.7)

# ============ 4. 远处的寒山寺 ============
def draw_temple(ax, x, y):
    # 寺庙主体 - 简化的塔形
    # 底座
    base = FancyBboxPatch((x - 8, y), 16, 6, 
                          boxstyle="round,pad=0.02",
                          facecolor='#4a4a4a', edgecolor='#2d2d2d', linewidth=1.5)
    ax.add_patch(base)
    
    # 中层
    mid = FancyBboxPatch((x - 6, y + 6), 12, 4,
                         boxstyle="round,pad=0.02",
                         facecolor='#5a5a5a', edgecolor='#2d2d2d', linewidth=1.5)
    ax.add_patch(mid)
    
    # 顶层
    top = FancyBboxPatch((x - 4, y + 10), 8, 3,
                         boxstyle="round,pad=0.02",
                         facecolor='#6a6a6a', edgecolor='#2d2d2d', linewidth=1.5)
    ax.add_patch(top)
    
    # 塔顶三角形
    roof = Polygon([(x - 5, y + 13), (x + 5, y + 13), (x, y + 18)],
                   facecolor='#5a5a5a', edgecolor='#2d2d2d', linewidth=1.5)
    ax.add_patch(roof)
    
    # 塔尖
    ax.plot([x, x], [y + 18, y + 21], color='#2d2d2d', linewidth=2)
    ax.plot([x - 1, x + 1], [y + 20, y + 20], color='#2d2d2d', linewidth=2)

draw_temple(ax, 80, 28)

# ============ 5. 钟（简笔画）============
def draw_bell(ax, x, y, size=3):
    # 钟的轮廓 - 简单的梯形+半圆
    bell_body = Polygon([(x - size, y), (x + size, y), 
                        (x + size * 0.7, y + size * 1.5), (x - size * 0.7, y + size * 1.5)],
                       facecolor='#8b7355', edgecolor='#5c4033', linewidth=2)
    ax.add_patch(bell_body)
    # 钟顶
    top_arc = patches.Arc((x, y + size * 1.5), size * 1.4, size * 0.8, 
                          theta1=0, theta2=180, color='#5c4033', linewidth=2)
    ax.add_patch(top_arc)
    # 钟锤
    ax.plot(x, y - 0.5, 'o', color='#5c4033', markersize=4)

draw_bell(ax, 90, 35, 2)

# ============ 6. 水面波纹 ============
def draw_water(ax):
    # 水面基础色
    water = patches.Rectangle((0, 0), 100, 25, 
                               facecolor='#1e3a5f', alpha=0.8)
    ax.add_patch(water)
    
    # 波纹线条
    for i in range(8):
        y_base = 3 + i * 2.5
        x_points = np.linspace(0, 100, 50)
        y_points = y_base + np.sin(x_points * 0.15 + i) * 0.5
        ax.plot(x_points, y_points, color='#3d5a80', linewidth=1, alpha=0.6)

draw_water(ax)

# ============ 7. 小船 ============
def draw_boat(ax, x, y):
    # 船身 - 简单的弧形
    boat_body = Polygon([(x - 8, y), (x - 6, y - 2), (x + 6, y - 2), (x + 8, y)],
                       facecolor='#8b4513', edgecolor='#5c3317', linewidth=2)
    ax.add_patch(boat_body)
    
    # 船底弧线
    theta = np.linspace(0, np.pi, 30)
    boat_bottom_x = x + 6 * np.cos(theta)
    boat_bottom_y = y - 2 - 1.5 * np.sin(theta)
    ax.fill(boat_bottom_x, boat_bottom_y, color='#8b4513', edgecolor='#5c3317', linewidth=2)
    
    # 船篷（半圆形遮蓬）
    canopy = patches.Arc((x, y + 1), 8, 5, theta1=0, theta2=180, 
                         color='#5c3317', linewidth=2)
    ax.add_patch(canopy)
    # 填充船篷
    theta2 = np.linspace(0, np.pi, 30)
    canopy_x = x + 4 * np.cos(theta2)
    canopy_y = y + 1 + 2.5 * np.sin(theta2)
    ax.fill(canopy_x, canopy_y, color='#654321', alpha=0.8)
    
    # 渔火 - 温暖的小点
    ax.plot(x + 2, y + 2, 'o', color='#ffa500', markersize=8, alpha=0.9)
    ax.plot(x + 2, y + 2, 'o', color='#ffff00', markersize=4)
    # 渔火光晕
    glow = Circle((x + 2, y + 2), 2, facecolor='#ffa500', alpha=0.2)
    ax.add_patch(glow)

draw_boat(ax, 35, 12)

# ============ 8. 岸边枫树 ============
def draw_maple_tree(ax, x, y, height=12, color='#8b0000'):
    # 树干
    ax.plot([x, x], [y, y + height * 0.4], color='#4a3728', linewidth=3)
    
    # 简笔树冠 - 用几个圆表示
    crown_y = y + height * 0.5
    for dx, dy, r in [(-2, 0, 3), (2, 0, 3), (0, 2, 3.5), (-1, 3.5, 2.5), (1, 3.5, 2.5)]:
        crown = Circle((x + dx, crown_y + dy), r, 
                       facecolor=color, edgecolor='#5c1010', linewidth=1, alpha=0.8)
        ax.add_patch(crown)
    
    # 几片飘落的叶子
    for _ in range(3):
        leaf_x = x + np.random.uniform(-4, 4)
        leaf_y = y + np.random.uniform(2, height * 0.3)
        ax.plot(leaf_x, leaf_y, 's', color=color, markersize=3, alpha=0.7)

# 画几棵枫树
draw_maple_tree(ax, 8, 24, 14, '#a52a2a')
draw_maple_tree(ax, 18, 25, 12, '#8b0000')
draw_maple_tree(ax, 55, 24, 10, '#b22222')

# ============ 9. 岸边地面 ============
ground = Polygon([(0, 24), (0, 28), (25, 26), (50, 25), (65, 26), (100, 28), (100, 24)],
                facecolor='#3d3d3d', edgecolor='#2d2d2d', linewidth=2)
ax.add_patch(ground)

# ============ 10. 水中倒影 ============
# 月亮倒影
moon_reflect = Ellipse((15, 8), 3, 6, facecolor='#fffacd', alpha=0.3)
ax.add_patch(moon_reflect)

# 渔火倒影
ax.plot([35, 35], [5, 10], color='#ffa500', linewidth=2, alpha=0.4)

# ============ 11. 诗文标题 ============
ax.text(50, 67, '枫桥夜泊', fontsize=20, fontweight='bold', 
        color='#fffacd', ha='center', va='center',
        fontfamily='WenQuanYi Zen Hei')
ax.text(50, 63.5, '唐 · 张继', fontsize=12, 
        color='#d4af37', ha='center', va='center',
        fontfamily='WenQuanYi Zen Hei')

# ============ 12. 儿童签名风格 ============
ax.text(92, 3, '小画家', fontsize=10, color='#ffd700', 
        ha='center', va='center', alpha=0.7,
        fontfamily='WenQuanYi Zen Hei')

# 保存图片
plt.tight_layout()
plt.savefig('/workspace/fengqiao_yepo_painting.png', 
            dpi=150, 
            facecolor='#1a1a3e',
            edgecolor='none',
            bbox_inches='tight',
            pad_inches=0.2)
plt.savefig('/workspace/fengqiao_yepo_painting.jpg', 
            dpi=150, 
            facecolor='#1a1a3e',
            edgecolor='none',
            bbox_inches='tight',
            pad_inches=0.2)

print("✨ 《枫桥夜泊》儿童简笔画已生成！")
print("📁 保存位置: /workspace/fengqiao_yepo_painting.png")
print("📁 保存位置: /workspace/fengqiao_yepo_painting.jpg")
