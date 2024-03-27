import tkinter as tk
from tkinter import filedialog as fd,simpledialog
from PIL import ImageTk,Image, ImageDraw,ImageFont

SAVE_MENU_ITEM = 2
WATERMARK_MENU_ITEM = 4

source_image = None
source_filename = ''
canvas_image_id = None
watermarked_image = None

def Reset():
    global canvas, watermarked_image, source_image, filemenu
    canvas.delete('all')
    watermarked_image = None
    filemenu.entryconfig(SAVE_MENU_ITEM, state=tk.DISABLED)
    filemenu.entryconfig(WATERMARK_MENU_ITEM, state=tk.DISABLED)

def draw_image(image):
    global panel, canvas_image_id,filemenu
    img = ImageTk.PhotoImage(image)
    canvas_image_id = canvas.create_image(0,0, anchor=tk.NW, image=img)

    # set the image as img
    panel.image = img

def openImage():
    global source_image, source_filename
    source_filename = openFile()
    if source_filename == '':
        return

    source_image = Image.open(source_filename).convert('RGBA')
    draw_image(source_image)

    filemenu.entryconfig(WATERMARK_MENU_ITEM, state=tk.NORMAL)
    
def openFile():
    name= fd.askopenfilename(filetypes=[("Image files", ".bmp .gif .jpg .png .tif")] )
    return name

def saveFile():
    global source_filename
    watermarked_image.save(source_filename[:-4] + "_wm.png")
    quit()
    
def addWatermark():
    global source_image, watermarked_image, filemenu
    watermark_filename = openFile()
    if watermark_filename == '':
        return

    source_width, source_height = source_image.size
    
    new_width = int(source_width/4)
    new_height = int(source_height/4)
    
    watermark_image = Image.open(watermark_filename).convert('RGBA').resize((new_width, new_height))

    watermark_target = Image.new("RGBA", source_image.size, (255,255,255,0))
    # Iterate through a grid, to place the background tile
    for i in range(0, source_width, new_width):
        for j in range(0, source_height, new_height):
            #paste the image at location i, j:
            watermark_target.paste(watermark_image, (i, j))

    bands = watermark_target.split()
    if len(bands) != 4: raise Exception('Not an RGBA image')
    adj_alpha = bands[3].point(lambda x: int(x * 0.25))
    watermark_target = Image.merge('RGBA', [*bands[:3], adj_alpha])

    watermarked_image = Image.alpha_composite(source_image, watermark_target)
    draw_image(watermarked_image)
    
    filemenu.entryconfig(SAVE_MENU_ITEM, state=tk.NORMAL)
    
    
root = tk.Tk()
root.resizable(width=True, height=True)
canvas = tk.Canvas(root, height=600, width=600, bg='white')

# create a label
panel = tk.Label(root)

canvas.pack()
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=Reset)
filemenu.add_command(label="Open", command=openImage)
filemenu.add_command(label="Save", command=saveFile,state=tk.DISABLED)
filemenu.add_separator()
filemenu.add_command(label="Watermark", command=addWatermark,state=tk.DISABLED)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()
