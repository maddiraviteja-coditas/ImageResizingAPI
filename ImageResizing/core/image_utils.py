from PIL import Image


def crop_image(image_path, x, y, width, height):
    try:
        with Image.open(image_path) as img:
            cropped_img = img.crop((x, y, x + width, y + height))
            cropped_img.save(image_path, quality=95, optimize=True)
            return True
            
    except Exception as e:
        print(f"Error cropping image: {str(e)}")
        return False
