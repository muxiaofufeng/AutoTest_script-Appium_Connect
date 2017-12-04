# coding=utf-8
# 由CreateSomeFiles.py生成
from src.testcase.page.AppPageElement import *


class PageElementAL(object):
    """
    阿里智能App all page element
    """

    def __init__(self, device, phone_os, app):
        self.mpw = MainPageWidget(phone_os, app).wrapper()
        self.device = device

    def get_page_element(self):
        self.device["page"] = {}
        self.device["page"]["add_device_class_page"] = self.mpw.add_device_class_page()
        self.device["page"]["add_device_method_page"] = self.mpw.add_device_method_page()
        self.device["page"]["add_normal_timer_page"] = self.mpw.add_normal_timer_page()
        self.device["page"]["add_outlet_list_page"] = self.mpw.add_outlet_list_page()
        self.device["page"]["add_specification_page"] = self.mpw.add_specification_page()
        self.device["page"]["app_home_page"] = self.mpw.app_home_page()
        self.device["page"]["change_nickname_page"] = self.mpw.change_nickname_page()
        self.device["page"]["control_device_page"] = self.mpw.control_device_page()
        self.device["page"]["cycle_timer_page"] = self.mpw.cycle_timer_page()
        self.device["page"]["day_elec_page"] = self.mpw.day_elec_page()
        self.device["page"]["delay_timer_page"] = self.mpw.delay_timer_page()
        self.device["page"]["device_info_page"] = self.mpw.device_info_page()
        self.device["page"]["elec_page"] = self.mpw.elec_page()
        self.device["page"]["exit_error"] = self.mpw.exit_error()
        self.device["page"]["fish_mode_timer_page"] = self.mpw.fish_mode_timer_page()
        self.device["page"]["input_wifi_password_page"] = self.mpw.input_wifi_password_page()
        self.device["page"]["login_page"] = self.mpw.login_page()
        self.device["page"]["more_elec_history_page"] = self.mpw.more_elec_history_page()
        self.device["page"]["mosquito_mode_timer_page"] = self.mpw.mosquito_mode_timer_page()
        self.device["page"]["my_page"] = self.mpw.my_page()
        self.device["page"]["night_mode_timer_page"] = self.mpw.night_mode_timer_page()
        self.device["page"]["normal_timer_page"] = self.mpw.normal_timer_page()
        self.device["page"]["peak_valley_price_page"] = self.mpw.peak_valley_price_page()
        self.device["page"]["piocc_mode_timer_page"] = self.mpw.piocc_mode_timer_page()
        self.device["page"]["search_device_fail_page"] = self.mpw.search_device_fail_page()
        self.device["page"]["search_device_loading_page"] = self.mpw.search_device_loading_page()
        self.device["page"]["set_elec_page"] = self.mpw.set_elec_page()
        self.device["page"]["set_peak_price_page"] = self.mpw.set_peak_price_page()
        self.device["page"]["set_valley_price_page"] = self.mpw.set_valley_price_page()
        self.device["page"]["setting_page"] = self.mpw.setting_page()
        self.device["page"]["single_price_page"] = self.mpw.single_price_page()
        self.device["page"]["timer_repeat_page"] = self.mpw.timer_repeat_page()
        self.device["page"]["warmer_mode_timer_page"] = self.mpw.warmer_mode_timer_page()
        self.device["page"]["water_mode_timer_page"] = self.mpw.water_mode_timer_page()
        self.device["page"]["welcome_page"] = self.mpw.welcome_page()

        self.device["page"]["add_device_popup"] = self.mpw.add_device_popup()
        self.device["page"]["bind_device_popup"] = self.mpw.bind_device_popup()
        self.device["page"]["loading_popup"] = self.mpw.loading_popup()
        self.device["page"]["logout_popup"] = self.mpw.logout_popup()
        self.device["page"]["mode_timer_conflict_popup"] = self.mpw.mode_timer_conflict_popup()
        self.device["page"]["timer_roll_popup"] = self.mpw.timer_roll_popup()
        self.device["page"]["unbind_device_popup"] = self.mpw.unbind_device_popup()
        self.device["page"]["update_popup"] = self.mpw.update_popup()
