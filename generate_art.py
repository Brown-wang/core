import random
import math

def jitter(val, amount=2):
    return val + random.uniform(-amount, amount)

def hand_drawn_path(points, fill="none", stroke="black", width=2, close=False):
    d = []
    if not points:
        return ""
    
    # Move to start
    start = points[0]
    d.append(f"M {jitter(start[0])} {jitter(start[1])}")
    
    # Draw lines to subsequent points with slight curves (quadratic bezier) or just jittered lines
    # For child style, jittered polylines are good
    for p in points[1:]:
        d.append(f"L {jitter(p[0])} {jitter(p[1])}")
    
    if close:
        d.append("Z")
        
    return f'<path d="{" ".join(d)}" fill="{fill}" stroke="{stroke}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round" />'

def draw_moon(cx, cy, size):
    # A crescent moon
    points = []
    # Outer arc
    for i in range(11):
        angle = -math.pi/2 + (math.pi * i / 10) # -90 to 90
        r = size
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        points.append((x, y))
    
    # Inner arc (to make it crescent)
    for i in range(10, -1, -1):
        angle = -math.pi/2 + (math.pi * i / 10)
        r = size * 0.6 # smaller radius for inner cutout look, but shifted
        x = cx + size*0.5 + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        points.append((x, y))
        
    return hand_drawn_path(points, fill="#FFD700", stroke="#FFD700", width=1, close=True)

def draw_crow(cx, cy, size):
    # M shape
    points = [
        (cx - size, cy),
        (cx - size/2, cy - size/2),
        (cx, cy),
        (cx + size/2, cy - size/2),
        (cx + size, cy)
    ]
    return hand_drawn_path(points, fill="none", stroke="black", width=2)

def draw_wave(cx, cy, width):
    points = []
    steps = 10
    for i in range(steps + 1):
        x = cx + (width * i / steps)
        y = cy + math.sin(i) * 5 # simple wave
        points.append((x, y))
    return hand_drawn_path(points, fill="none", stroke="#87CEEB", width=3)

def draw_tree(cx, cy, height):
    elements = []
    # Trunk
    trunk_points = [
        (cx, cy),
        (cx, cy - height)
    ]
    elements.append(hand_drawn_path(trunk_points, stroke="#8B4513", width=4))
    
    # Branches/Leaves (scribbles)
    for _ in range(5):
        lx = cx + random.uniform(-30, 30)
        ly = cy - height + random.uniform(-30, 30)
        # Scribble
        scribble_points = []
        for _ in range(10):
            scribble_points.append((lx + random.uniform(-10, 10), ly + random.uniform(-10, 10)))
        elements.append(hand_drawn_path(scribble_points, fill="none", stroke="#FF4500", width=1)) # Red/Orange for maple
        
    return "\n".join(elements)

def draw_temple(cx, cy):
    elements = []
    # Base
    base_points = [
        (cx - 40, cy),
        (cx + 40, cy),
        (cx + 30, cy - 30),
        (cx - 30, cy - 30)
    ]
    elements.append(hand_drawn_path(base_points, fill="none", stroke="gray", width=2, close=True))
    
    # Roof
    roof_points = [
        (cx - 50, cy - 30),
        (cx + 50, cy - 30),
        (cx, cy - 60)
    ]
    elements.append(hand_drawn_path(roof_points, fill="none", stroke="gray", width=2, close=True))
    
    # Bell nearby
    bell_points = [
        (cx + 60, cy - 10),
        (cx + 80, cy - 10),
        (cx + 70, cy - 40)
    ]
    elements.append(hand_drawn_path(bell_points, fill="none", stroke="black", width=2, close=True))
    
    return "\n".join(elements)

def draw_boat(cx, cy):
    elements = []
    # Hull
    hull_points = [
        (cx - 40, cy),
        (cx + 40, cy),
        (cx + 30, cy + 20),
        (cx - 30, cy + 20)
    ]
    elements.append(hand_drawn_path(hull_points, fill="none", stroke="black", width=2, close=True))
    
    # Shelter
    shelter_points = [
        (cx - 20, cy),
        (cx + 20, cy),
        (cx + 15, cy - 20),
        (cx - 15, cy - 20)
    ]
    elements.append(hand_drawn_path(shelter_points, fill="none", stroke="black", width=2, close=True))
    
    # Fire (red dot)
    elements.append(f'<circle cx="{jitter(cx)}" cy="{jitter(cy-5)}" r="3" fill="red" />')
    
    return "\n".join(elements)

def generate_svg():
    svg = []
    svg.append('<svg width="600" height="400" xmlns="http://www.w3.org/2000/svg" style="background-color: #F0F8FF; border: 2px solid black;">')
    
    # 1. Sky / Background (implicit in background color, but let's add some night shading)
    # Gradient or just a big rectangle for night sky
    svg.append('<rect x="0" y="0" width="600" height="250" fill="#191970" opacity="0.8" />') # Midnight Blue
    
    # 2. Moon (Top Right)
    svg.append(draw_moon(500, 80, 30))
    
    # 3. Crows (Sky)
    svg.append(draw_crow(200, 100, 20))
    svg.append(draw_crow(250, 120, 15))
    
    # 4. Temple & Bell (Distance, near horizon)
    svg.append(draw_temple(450, 250))
    
    # 5. Water (Bottom half)
    svg.append('<rect x="0" y="250" width="600" height="150" fill="#87CEFA" opacity="0.5" />') # Light Sky Blue
    svg.append(draw_wave(100, 300, 50))
    svg.append(draw_wave(300, 320, 60))
    svg.append(draw_wave(500, 280, 40))
    
    # 6. Boat (On water)
    svg.append(draw_boat(200, 300))
    
    # 7. Maple Trees (Foreground/Shore, Left)
    svg.append(draw_tree(80, 380, 120))
    svg.append(draw_tree(40, 360, 100))
    
    svg.append('</svg>')
    
    return "\n".join(svg)

if __name__ == "__main__":
    content = generate_svg()
    html_content = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>枫桥夜泊 - 儿童画版</title>
<style>
    body {{ display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background-color: #eee; }}
    h1 {{ position: absolute; top: 20px; font-family: "KaiTi", "楷体", serif; }}
</style>
</head>
<body>
<h1>枫桥夜泊</h1>
{content}
</body>
</html>
"""
    with open("fengqiao_yebo.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("HTML file generated: fengqiao_yebo.html")
