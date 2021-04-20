import sys
from PIL import Image
def get_concat_h_multi_resize(im_list, resample=Image.BICUBIC):
    min_height = min(im.height for im in im_list)
    im_list_resize = [im.resize((int(im.width * min_height / im.height), min_height),resample=resample)
                      for im in im_list]
    total_width = sum(im.width for im in im_list_resize)
    dst = Image.new('RGB', (total_width, min_height))
    pos_x = 0
    for im in im_list_resize:
        dst.paste(im, (pos_x, 0))
        pos_x += im.width
    return dst

def get_concat_v_multi_resize(im_list, resample=Image.BICUBIC):
    min_width = min(im.width for im in im_list)
    im_list_resize = [im.resize((min_width, int(im.height * min_width / im.width)),resample=resample)
                      for im in im_list]
    total_height = sum(im.height for im in im_list_resize)
    dst = Image.new('RGB', (min_width, total_height))
    pos_y = 0
    for im in im_list_resize:
        dst.paste(im, (0, pos_y))
        pos_y += im.height
    return dst
def get_concat_tile_resize(im_list_2d, resample=Image.BICUBIC):
    im_list_v = [get_concat_h_multi_resize(im_list_h, resample=resample) for im_list_h in im_list_2d]
    return get_concat_v_multi_resize(im_list_v, resample=resample)
images=[]
for xx in range(50):
	arr=[str(xx*60+i) for i in range(1,61)]
	images+= [[Image.open('./60x50/'+x+'.jpg') for x in arr]]
	# print(arr)
	# print(images)
	# # a=input()
	# widths, heights = zip(*(i.size for i in images))

	# total_width = sum(widths)
	# max_height = max(heights)

	# new_im = Image.new('RGB', (total_width, max_height))

	# x_offset = 0
	# for im in images:
	#   new_im.paste(im, (x_offset,0))
	#   x_offset += im.size[0]

	# new_im.save(str(xx)+'test.jpg')
print(images)
get_concat_tile_resize(images).save('ans.jpg')