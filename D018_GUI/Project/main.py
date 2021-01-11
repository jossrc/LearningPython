import colorgram


def extract_colors_from(img: str, count: int):
    rgb_colors: list[tuple[int, int, int]] = []
    colors = colorgram.extract(img, count)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb_colors.append((r, g, b))
    return rgb_colors


rgb_color_list = extract_colors_from('image.jpg', 30)

print(rgb_color_list)
