# 导入需要的
from moviepy.editor import *

# 从本地载入视频myHolidays.mp4并截取00:00:50 - 00:00:60部分
clip = VideoFileClip("/Users/chuzhaonan/Desktop/131_1677407247.mp4")

# 调低音频音量 (volume x 0.8)
clip = clip.volumex(0.8)
# 基本参数调节
clip  = clip.fx(vfx.mirror_x)

#打水印
logo = (ImageClip("~/Downloads/e9337be1d1341a5c.png")
        .set_duration(clip.duration)  # 水印持续时间
        .resize(height=80)  # 水印的高度，会等比缩放
        .margin(left=0, top=0, opacity=0.8)  # 水印边距和透明度opacity 1为不透明 0为透明
        .set_pos(("left","top")))

#做一个txt clip. 自定义样式，颜色.自定义文案
txt_clip = TextClip("My First Video", fontsize=50, color='white')
# 文本clip在屏幕正中显示持续10秒
txt_clip = txt_clip.set_pos('center').set_duration(10)

#添加音轨


#翻转
# 把 text clip 的内容覆盖 video clip
video = CompositeVideoClip([clip, txt_clip, logo])

# 把最后生成的视频导出到文件内
video.write_videofile("myFirstVideo1.mp4")

