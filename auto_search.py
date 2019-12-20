# encoding=utf-8
import ocr_helper
import question_helper
import recommend_helper
import screenshot_helper
import selenium_helper
import _thread
import config
import time
import jieba
import img_compress_helper


def main():
    # 加载结巴字典
    jieba.initialize()
    driver = selenium_helper.browser_init()
    # 这是保存图片的文件夹路径
    img_folder = config.path
    time.sleep(2)
    while (True):
        time.sleep(1)
        start = time.time()
        # 图片名字、图片完整路径
        img_name = str(int(time.time())) + ".png"
        imgpath = img_folder + img_name
        # 截图，判断是否是题目
        screenshot_helper.screen_capture(imgpath, config.screen_shot_position, config.screen_shot_size)
        if screenshot_helper.isQuestion(imgpath) == False:
            continue
        time.sleep(0.2)
        # 再截一张，确保题目完整
        screenshot_helper.screen_capture(imgpath, config.screen_shot_position, config.screen_shot_size)
        screen_shot_tag = time.time()
        print('截图耗时: ' + str(int(screen_shot_tag - start))),
        # 压缩图片
        imgpath2 = imgpath.replace(".png", "_compressed.png")
        img_compress_helper.compress(imgpath, imgpath2)
        question = ocr_helper.get_question(imgpath2)
        question_body = question_helper.parse_question_and_answer(question)  # 题干和选项分开

        question = question_body[1] + " " + " ".join(question_body[2])
        #         选项加引号
        # question = question_body[1] + " \"" + '\" \"'.join(question_body[2]) + "\""
        print('搜索: ' + question)

        _thread.start_new_thread(selenium_helper.baidu_search, (driver, question))
        try:
            _thread.start_new_thread(recommend_helper.recommend_fast, (question_body, 0, 1))
            _thread.start_new_thread(recommend_helper.recommend_fast, (question_body, 0, 0))
        except:
            traceback.print_exc()
            continue
        time.sleep(10)


if __name__ == '__main__':
    main()
