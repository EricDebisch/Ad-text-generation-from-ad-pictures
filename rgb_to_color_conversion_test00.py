from scipy.spatial import KDTree
import webcolors

def convert_rgb_to_names(rgb_tuple):
    
    # a dictionary of all the hex and their respective names in css3
    css3_db = webcolors.CSS3_HEX_TO_NAMES
    names = []
    rgb_values = []

    for color_hex, color_name in css3_db.items():
        names.append(color_name)
        rgb_values.append(webcolors.hex_to_rgb(color_hex))
    
    kdt_db = KDTree(rgb_values)
    
    distance, index = kdt_db.query(rgb_tuple)
    return f'closest match: {names[index]}'

print(convert_rgb_to_names((254,0,0)))