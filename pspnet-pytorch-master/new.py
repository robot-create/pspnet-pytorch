import streamlit as st
# 画图
from PIL import Image
import cv2
import time
import numpy as np
import os
from utils1 import PSPNet, draw_image_with_boxes, load_local_image


def detect_image():
    # 自己文件上传  -   单文件载入
    st.sidebar.markdown("### 选择本地的一张图片(png/jpg)...")
    uploaded_file = st.sidebar.file_uploader(" ")

    left_column, middle_column, right_column = st.sidebar.beta_columns(3)

    if middle_column.button('检测'):
        pspnet = PSPNet()
        st.image(uploaded_file, caption='The original image',
                 use_column_width=True)
        image = Image.open(uploaded_file)
        r_image = pspnet.detect_image(image)
        st.image(r_image, caption='The detection result',
                 use_column_width=True)

def detect_video():
    video_save_path = ""
    video_fps = 30.0


    st.title('Object Detection in Video')
    option = st.radio('', ['Choose a test video', 'Upload your own video (.mp4 only)', 'Camera'])

    if option == 'Choose a test video':
        test_videos = os.listdir('./img/test_video/')
        test_video = st.selectbox('Please choose a test video', test_videos)
    elif option == 'Camera':
        test_video = None
    else:
        test_video = st.file_uploader('Upload a video', type = ['mp4'])

        if test_video is not None:
            test_video = str(test_video.name)
            pass
        else:
            st.write('** Please upload a test video **')

    if test_video is not None:
        video = './img/test_video/' + test_video
    else:
        video = 0

    left_column, middle_column, right_column = st.sidebar.beta_columns(3)
    if middle_column.button('检测'):
        time.sleep(3)
        st.write(f"[INFO] Processing Video....")

        FRAME_WINDOW = st.image([])
        pspnet = PSPNet()
        capture = cv2.VideoCapture(video)
        if video_save_path != "":
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            size = (int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
            out = cv2.VideoWriter(video_save_path, fourcc, video_fps, size)

        fps = 0.0
        while (True):
            t1 = time.time()
            # 读取某一帧
            ref, frame = capture.read()

            try:
                #格式转变，BGRtoRGB
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # 转变成Image
                frame = Image.fromarray(np.uint8(frame))
                # 进行检测
                frame = np.array(pspnet.detect_image(frame))
                # RGBtoBGR满足opencv显示格式
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            except:
                break

            fps = (fps + (1. / (time.time() - t1))) / 2
            print("fps= %.2f" % (fps))
            frame = cv2.putText(frame, "fps= %.2f" % (fps), (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            #cv2.imshow("video", frame)
            FRAME_WINDOW.image(frame[:, :, ::-1])
            c = cv2.waitKey(1) & 0xff
            if video_save_path != "":
                out.write(frame)

            if c == 27:
                capture.release()
                break
        st.write(f"Finished!")
        capture.release()
        if video_save_path != "":
            out.release()
        cv2.destroyAllWindows()

def read_markdown(path):
    with open(path, "r", encoding='utf-8') as f:  # 打开文件
        data = f.read()  # 读取文件
    return data


# Streamlit encourages well-structured code, like starting execution in a main() function.
def main():
    st.sidebar.title("图像检测参数调节器")  # 侧边栏
    app_mode = st.sidebar.selectbox("切换页面模式:",
                                    ["detect image", "detect video", "Show the source code"])

    # 展示栏目三
    if app_mode == "detect image":
        # readme_text.empty()      # 刷新页面
        st.markdown('---')
        st.markdown('## pspnet 检测结果:')
        detect_image()  # 运行内容
    # 展示栏目一
    elif app_mode == "detect video":
        #st.sidebar.success('To continue select "Run the app".')
        st.markdown('---')
        st.markdown('## pspnet 检测结果:')
        detect_video()
    # 展示栏目二
    elif app_mode == "Show the source code":
        #readme_text.empty()  # 刷新页面
        st.code(read_markdown("new.py"))


if __name__ == "__main__":
    main()