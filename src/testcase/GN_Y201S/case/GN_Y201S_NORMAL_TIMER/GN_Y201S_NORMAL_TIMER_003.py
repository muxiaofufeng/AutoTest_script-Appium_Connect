# coding=utf-8
from src.testcase.GN_Y201S.WidgetOperation import *


class GNY201SNormalTimer3(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"FUT_NTIMER_普通定时(#48)"  # 用例所属模块
        self.case_title = u'FUT_NTIMER_单次定时开'  # 用例名称
        self.zentao_id = "513"  # 禅道ID

    # 用例动作
    def case(self):
        device = conf["MAC"]["AL"][0]
        self.set_power(device, "power_off")

        self.choose_home_device(device)

        self.close_mode_timer()

        self.close_general_timer()

        self.widget_click(self.page["control_device_page"]["normal_timer"],
                          self.page["normal_timer_page"]["title"])

        self.delete_normal_timer()

        now = time.strftime("%H:%M")

        time_1 = 2
        start_time_1, set_time_1, cycle1 = self.create_normal_timer(now, time_1, "power_on", u"永不")

        self.widget_click(self.page["normal_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        attribute = self.ac.get_attribute(self.wait_widget(self.page["control_device_page"]["launch_mode"]), "name")
        if attribute != u"定时任务开":
            raise TimeoutException("mode launch failed, current: %s" % [attribute])

        self.widget_click(self.page["control_device_page"]["to_return"],
                          self.page["app_home_page"]["title"])

        self.check_timer(device, start_time_1, set_time_1, u"开", cycle1)
