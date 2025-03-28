from pages.base_form import BaseForm


class Alerts(BaseForm):
    __left_panel = '//*[@class="left-pannel"]'
    __showed_alerts_panel = '//*[@class="element-group" and .//text()[contains(., "Alerts, Frame & Windows")]]//*[@class="element-list collapse show"]'


    def __init__(self):
        super().__init__()