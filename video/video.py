import os
import time
from tqdm import tqdm, trange
from moviepy.editor import VideoFileClip, concatenate_videoclips


dir = time.strftime("%Y-%m-%d", time.localtime())
dir_ls = os.listdir(dir)
clip_ls = []

for d in tqdm(dir_ls, ncols=60):
    clip_ls.append(VideoFileClip('/'.join((dir, d))))
print('读取完成，共{:2}个文件'.format(len(clip_ls)))

i = ti = 0
oun = []
ouv = []
while True:
    print('可接受指令\nn e others')
    s = input()
    if s == 'n':
        i += 1
        ti = 0
        print('切换到第{:2}段视频'.format(i))
        continue
    elif s.startswith('n'):
        i = int(s[1:])
        ti = 0
        print('切换到第{:2}段视频'.format(i))
        continue
    elif s == 'e':
        print('退出剪辑')
        break
    else:
        tu = s.split(' ')
        if len(tu) == 2:
            tu.append('_'.join((str(i), str(ti))))
            ti += 1
        print(tu)
        oun.append(tu[2])
        ouv.append(clip_ls[i].subclip(int(tu[0]), int(tu[1])))

for ci in trange(len(ouv), ncols=60):
    ouv[ci].write_videofile('/'.join(('output', dir, oun[ci]+'.mp4')))

print('渲染完成')