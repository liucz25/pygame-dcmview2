# 统筹管理
# 如果需要 可以封装一个 manage 类 实现功能

from model.myevent.myevent import MyEvent
import model.app.app as app


if __name__ == '__main__':
    # app_event = dcmevent.DcmEvent()
    app_event = MyEvent()

    applicaton = app.APP(app_event)
    applicaton.run()
