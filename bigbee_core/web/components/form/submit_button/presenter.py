# components/form/submit_button/presenter.py
from bigbee_core.web.rendering.templates import T
from .dto import Dto

class Presenter:
    @staticmethod
    def present(dto: Dto) -> str:
        template = T().get_template("components/form/submit_button/template.pug")
        return template.render(vars(dto))
