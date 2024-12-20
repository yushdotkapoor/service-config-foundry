class ServiceSection:
    def __init__(self):
        self.unit_name = "Service"
        self.user = None
        self.working_directory = None
        self.type = None
        self.exit_type = None
        self.guess_main_p_i_d = None
        self.remain_after_exit = None
        self.p_i_d_file = None
        self.bus_name = None
        self.exec_start = None
        self.exec_start_pre = None
        self.exec_start_post = None
        self.exec_reload = None
        self.exec_stop = None
        self.exec_stop_post = None
        self.restart_sec = None
        self.restart_steps = None
        self.restart_max_delay_sec = None
        self.timeout_start_sec = None
        self.timeout_stop_sec = None
        self.timeout_abort_sec = None
        self.timeout_sec = None
        self.timeout_start_failure_mode = None
        self.runtime_max_sec = None
        self.runtime_randomized_extra_sec = None
        self.watchdog_sec = None
        self.restart = None
        self.restart_mode = None
        self.success_exit_status = None
        self.restart_prevent_exit_status = None
        self.restart_force_exit_status = None
        self.root_directory_start_only = None
        self.non_blocking = None
        self.notify_access = None
        self.sockets = None
        self.file_descriptor_store_max = None
        self.file_descriptor_store_preserve = None
        self.usb_function_descriptors = None
        self.usb_function_strings = None
        self.o_o_m_policy = None
        self.open_file = None
        self.reload_file = None