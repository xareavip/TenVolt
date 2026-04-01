# ffmpeg基本操作

ffmpeg -h   // 帮助
ffmpeg -version // 版本信息
ffmepg -devices // 查看可用设备
ffmpeg -i input.mp4 // 查看视频信息

# 格式转换

ffmpeg.exe -i input.mkv -vcodec h264 -b:v 1.5M -acodec aac -b:a 48K output.mp4

* \-i 后面是输入文件（编码方式任意，可以通过ffprobe查看）
* \-vcodec 转换目标格式
* \-b:v 设置视频流码率（1.5M）
* \-b:a 设置音频流码率（48K）
* output.mp4 输出mp4格式封装。

# 视频与gif互转

### 将视频 MP4 转化为 GIF

ffmpeg -i test.mp4 test.gif

### 将视频中的一部分转换为GIF

// 从视频中第10秒开始，截取时长为3秒的片段转化为 gif

ffmpeg -ss 00:00:10 -t 3  -i test.mp4 test.gif

### 转化高质量 GIF

// 默认转化是中等质量模式，若要转化出高质量的 gif，可以修改比特率

ffmpeg -i test.mp4 -b:v 2048k test.gif

### 将 GIF 转化为 MP4

ffmpeg -f gif -i test.gif test.mp4

// 也可以将 gif 转为其他视频格式

ffmpeg -f gif -i test.gif test.mpeg    

ffmpeg -f gif -i test.gif test.mkv

### 视频提取帧，保存为图片

// 将视频提取10帧

ffmpeg -i test.mp4 -r 10 %06d.jpg;

%06d为计算机表示符号，表示输出有六位数字的顺序编号

# 视频剪切

ffmpeg -ss 00:00:15 -t 00:00:05 -i input.mp4 -vcodec copy -acodec copy output.mp4
// -ss表示开始切割的时间，-t表示要切多少。上面就是从15秒开始，切5秒钟出来

ffmpeg  -i C:/plutopr.mp4 -acodec copy 

&#x09;	-vf scale=1280:720

&#x09;	-ss 00:00:10 -t 15 C:/cutout1.mp4 -y

* \-ss time\_off set the start time offset 设置从视频的哪个时间点开始截取，上文从视频的第10s开始截取
* \-to 截到视频的哪个时间点结束。上文到视频的第15s结束。截出的视频共5s.如果用-t 表示截取多长的时间如 上文-to 换位-t则是截取从视频的第10s开始，截取15s时长的视频。即截出来的视频共15s.
* \-vcodec copy表示使用跟原视频一样的视频编解码器。
* \-acodec copy表示使用跟原视频一样的音频编解码器。
* \-i 表示源视频文件
* \-y 表示如果输出文件已存在则覆盖。
* \-vf 设置视频分辨率

# 提取视频流

ffmpeg -i input.mp4 -vcodec copy -an -f m4v output.h264

从MP4容器中提取出纯H.264视频流，并以.h264格式（原始码流）保存。

* \-i input.mp4：指定输入文件
* \-vcodec copy：视频编码直接复制（不重新编码，快速无损）
* \-an：忽略音频流（audio none）
* \-f m4v：强制输出格式为MPEG-4视频（纯视频流）
* output.h264：输出文件名（虽然后缀.h264，实际是m4v格式）

主要用途

1. 去除音频：从视频中单独提取视频轨道
2. 格式转换：将MP4容器格式转为原始H.264码流格式（常用于一些专业视频处理软件）
3. 流媒体分析：获得纯净的视频流用于分析或测试
4. 兼容性：某些老旧设备或专业编码工具可能需要原始码流格式

# 视频缩放

&#x20;输入的1920x1080缩小到960x540输出:

* ffmpeg -i input.mp4 -vf scale=960:540 output.mp4  

如果540不写，写成-1，即scale=960:-1, 保持原始的宽高比进行缩放

* ffmpeg -i input.mp4 -vf scale=960:-1 output.mp4 // 保持宽高比,注意宽要能被2出尽，不然报错

# 视频旋转

顺时针旋转画面90度

ffmpeg -i test.mp4 -vf "transpose=1" out.mp4 或者

ffmpeg -i input.mp4 -vf transpose=1 output.mp4

逆时针旋转画面90度

ffmpeg -i test.mp4 -vf "transpose=2" out.mp4

顺时针旋转画面90度再水平翻转

ffmpeg -i test.mp4 -vf "transpose=3" out.mp4

逆时针旋转画面90度水平翻转

ffmpeg -i test.mp4 -vf "transpose=0" out.mp4

水平翻转视频画面

ffmpeg -i test.mp4 -vf hflip out.mp4

垂直翻转视频画面

ffmpeg -i test.mp4 -vf vflip out.mp4

# 截取视频图像

ffmpeg -i input.mp4 -r 1 -q:v 2 -f image2 pic-%03d.jpeg // -r 每一秒几帧，-q:v 存储jpeg的图像质量，一般2是高质量
ffmpeg -i input.mp4 -ss 00:00:20 -t 10 -r 1 -q:v 2 -f image2 pic-%03d.jpeg //抽取10帧图片
随便挑一张，转为YUV:
ffmpeg -i pic-001.jpeg -s 1440x1440 -pix\_fmt yuv420p xxx3.yuv

# 图片序列与视频转换

ffmpeg -i 001.mp3 -i example.%d.jpg -s 1024x768 -vcodec mpeg4 rebuild.mp4 // 把图片序列帧和音频文件利用mpeg4编码方式合成视频文件darkdoor.avi
ffmpeg -i input.mp4 example.%d.jpg // 把视频文件导出成序列帧

# 设置输出视频的分辨率

ffmpeg -i input\_file -vcodec h264 -s 1280x720 output\_file
其中 -s 表示分辨率。

# 分离音视频流保存为不同文件

ffmpeg -i input\_file -vcodec copy -an output\_file\_video　　//提取视频流 
ffmpeg -i input\_file -acodec copy -vn output\_file\_audio　　//提取音频流
其中 -an 表示不处理音频， -vn 表示不处理视频。

# 合并多个音视频文件为一个文件

ffmpeg –i video\_file –i audio\_file –vcodec copy –acodec copy output\_file 

# 提取视频图像保存为图片文件(将视频分解为单幅图片)

ffmpeg –i input\_file –r 1 –f image2 image-%3d.jpeg        //提取图片

# 多个视频文件拼接

首先创建一个需要拼接的文件，例如 concat.txt，内容如下：

file ‘orig\_20160616113303\_0.avi’
file ‘orig\_20160616113303\_1.avi’

然后执行如下命令

ffmpeg  -f concat -i concat.txt  -c copy orig\_20160616113303\_merge.avi 

* ***合并时注意视频格式统一，不然生成的视频无法播放***
* ***如果提示权限有问题，只需在concat命令后加入-safe 0***

# ***FFmpeg 推流：flv直播流***

ffmpeg -re -i 1.mp4 -vcodec copy -acodec copy -b:v 800k -b:a 32k -f flv rtmp://localhost/live

\- localhost, 本机，可以设置ip地址或者域名

需要先开启rtmp服务端才可以开始推流和拉流。

# 修改视频播放速度

ffmpeg -i input.mp4 -vf "setpts=0.5\*PTS" output.mp4

该命令调整视频2倍速播放，然后输出。

$ ffmpeg -i input.mp4 -vf "setpts=4.0\*PTS" output.mp4

减小视频播放速度。 乘以一个参数大于1的数。

