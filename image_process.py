from PIL import Image

def adjust_size(graph: str, length: int, height: int) -> None:
    im = Image.open(graph)
    im.thumbnail((length, height), Image.ANTIALIAS)
    im.save(graph, 'png')

def add_flag(input_image_name: str):
    flag = Image.open("flag.png")
    input_image = Image.open("Resource/"+input_image_name)
    adjust_size("Resource/"+input_image_name, 400, 400)
    box = (250,300,400,400)
    flag_box = (0,0,150,100)
    region = flag.crop(flag_box)
    input_image.paste(region, box)
    input_image.save("output/" + input_image_name, "png")



if __name__ == "__main__":
    # some error may happen when you edit the image at the first time, if you
    # try again, it works.
    file_name = "3-1Z52G12Q5457.jpg"
    try:
        add_flag(file_name) #if fail, try again)
    except:
        add_flag(file_name)
