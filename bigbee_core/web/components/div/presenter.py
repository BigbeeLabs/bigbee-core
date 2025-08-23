# bigbee_core/web/components/div/presenter.py
from bigbee_core.web.rendering.templates import T
from bigbee_core.web.rendering.html import html
from .dto import Dto

class Presenter:
    @staticmethod
    def present(dto: Dto) -> str:
        tpl = T().get_template("components/div/template.pug")
        ctx = {**vars(dto), "content": html(dto.content) if dto.content else ""}
        return html(tpl.render(ctx))