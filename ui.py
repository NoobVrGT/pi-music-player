from PIL import Image, ImageDraw, ImageFont
import ST7789
import time

# --- Display Setup ---
disp = ST7789.ST7789(
    height=240,
    width=240,
    rotation=0,
    port=0,
    cs=0,
    dc=25,
    backlight=18,
    spi_speed_hz=80_000_000
)

disp.begin()

# --- Load Fonts ---
font_large = ImageFont.load_default()
font_small = ImageFont.load_default()

# --- Main UI Loop ---
while True:
    # Create blank screen
    img = Image.new("RGB", (240, 240), (0, 0, 0))
    draw = ImageDraw.Draw(img)

    # --- Top Bar ---
    draw.rectangle((0, 0, 240, 30), fill=(30, 30, 30))
    draw.text((10, 7), "Music Player", fill=(255, 255, 255), font=font_small)
    draw.text((180, 7), "BT: ?", fill=(200, 200, 200), font=font_small)

    # --- Album Art Placeholder ---
    draw.rectangle((20, 40, 220, 180), outline=(0, 150, 255), width=3)
    draw.text((70, 105), "Album Art", fill=(0, 150, 255), font=font_small)

    # --- Song Info ---
    draw.text((20, 190), "Song Title", fill=(255, 255, 255), font=font_small)
    draw.text((20, 205), "Artist Name", fill=(180, 180, 180), font=font_small)

    # --- Controls ---
    draw.text((20, 225), "<<", fill=(255, 255, 255), font=font_large)
    draw.text((110, 225), "▶", fill=(255, 255, 255), font=font_large)
    draw.text((200, 225), ">>", fill=(255, 255, 255), font=font_large)

    # Display the frame
    disp.display(img)

    time.sleep(0.1)
