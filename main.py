from PIL import Image , ImageDraw

def create_a4():
    background = Image.new('RGBA', (2480, 3508), (255, 255, 255, 255))
    draw = ImageDraw.Draw(background)
    im_w, im_h = background.size
    mitte = im_w / 2
    draw.line((mitte, 0, mitte, im_h), fill=(0,0,0,255), width=10)
    del draw
    return background

def place_bcard(bcard):
    background = create_a4()
    draw = ImageDraw.Draw(background)
    bildende_y = 100
    bg_w, bg_h = background.size
    draw.line((0, bildende_y-5, bg_w, bildende_y-5), fill=(0,0,0,255), width=10)
    with Image.open(bcard, "r") as card:
        
        for _ in range(5):
            

            offset_y = bildende_y
            card_w, card_h = card.size
            
            

            offset_x = int(bg_w/2 + 5)
            offset =  offset_x, offset_y

            background.paste(card, offset)

            offset_x = int(bg_w/2 - 4) - card_w
            offset =  offset_x, offset_y

            background.paste(card, offset)
            
            bildende_y = offset_y + card_h + 4
            draw.line((0, bildende_y, bg_w, bildende_y), fill=(0,0,0,255), width=10)
            bildende_y += 5
            print()

    background.save('front.png')


place_bcard("test.png")