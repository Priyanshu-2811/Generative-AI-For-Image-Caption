# Generative AI for Image using Python
from PIL import Image
import numpy as np
import random
import os

def image_features(image_path):
    image = Image.open(image_path)
    width, height = image.size
    colors = image.getcolors(width * height)
    color_histogram = {color: count for color, count in colors}
    return width, height, color_histogram

def generate_caption(width, height, color_histogram):
    adjectives = ['breathtaking', 'vibrant', 'stunning', 'amazing', 'gorgeous']
    verbs = ['showcases', 'displays', 'exhibits', 'illustrates', 'presents']
    objects = ['nature','colors','landscapes','views','arts']

    caption_parts = [
        f'A {random.choice(adjectives)} image of {random.choice(objects)}',
        f'This {random.choice(adjectives)} {random.choice(objects)}',
        f'A captivating view of {random.choice(objects)}',
    ]

    caption_parts.append(f'with dimensions {width}x{height}')

    if len(color_histogram) > 5:
        caption_parts.append('and a diverse color palette')
    elif len(color_histogram) > 2:
        caption_parts.append('with a rich color palette')
    else:
        caption_parts.append('with a limited color palette')

    caption_parts.append(f'{random.choice(verbs)} {width}x{height} pixels.')

    return ' '.join(caption_parts)

def suggest_caption(image_path):
    width, height, color_histogram = image_features(image_path)
    return generate_caption(width, height, color_histogram)

def suggest_likes(image_path):
    width, height, color_histogram = image_features(image_path)
    return estimate_likes(width, height, color_histogram)
      
def estimate_likes(width, height, color_histogram):
    like_multiplier = 10
    if width > 1920 or height > 1080:
        like_multiplier += 10
    if len(color_histogram) > 10:
        like_multiplier += 5
    return like_multiplier * 100

image_path = r"C:\Users\dell\Downloads\for.jpg"
caption = suggest_caption(image_path)
print("The Instagram Caption for the provided image could be :")
print(caption)
likes = suggest_likes(image_path)
shares = likes // 2
saves = likes // 3

print("The Estimated likes can be:")
print(f'Expected Likes: {likes}')
print(f'Expected Shares: {shares}')
print(f'Expected Saves: {saves}')



