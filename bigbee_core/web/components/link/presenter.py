# bigbee_core/web/components/link/presenter.py
from bigbee_core.web.rendering.templates import T
from bigbee_core.web.rendering.html import html
from .dto import Dto

class Presenter:
    @staticmethod
    def present(dto: Dto) -> str:
        # Safe default: if opening a new tab, ensure noopener/noreferrer
        rel = dto.rel
        if (dto.target or "").lower() == "_blank":
            base = {"noopener", "noreferrer"}
            existing = set(rel.split()) if rel else set()
            rel = " ".join(sorted(base | existing))

        tpl = T().get_template("components/link/template.pug")
        return html(tpl.render({**vars(dto), "rel": rel}))
