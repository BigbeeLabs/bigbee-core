# bigbee_core/web/components/text_input/presenter.py
from bigbee_core.web.rendering.templates import T
from bigbee_core.web.rendering.html import html
from .dto import Dto

class Presenter:
    @staticmethod
    def present(dto: Dto) -> str:
        template = T().get_template("components/text_input/template.pug")
        help_id = f"{dto.id}-help" if dto.help_text else None
        error_id = f"{dto.id}-error" if dto.error_text else None
        described_by = " ".join(x for x in (help_id, error_id) if x) or None
        ctx = {
            **vars(dto),
            "help_id": help_id,
            "error_id": error_id,
            "described_by": described_by,
            "aria_invalid": "true" if dto.error_text else None,
        }
        return html(template.render(ctx))
