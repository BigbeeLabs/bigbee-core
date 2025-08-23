# bigbee_core/web/components/form/presenter.py
from bigbee_core.web.rendering.templates import T
from bigbee_core.web.rendering.html import html
from .template_data import FormTemplateData
from .dto import Dto as MyDto

class FormPresenter:
    @classmethod
    def present(cls, my_dto: MyDto) -> str:
        data = FormTemplateData(
            method=my_dto.method, 
            action=my_dto.action, 
            csrf_token=my_dto.csrf_token,
            buttons=my_dto.buttons,
            remote=my_dto.remote,
            form_fields=my_dto.form_fields,
            initializers=my_dto.initializers
        )
        template = T().get_template("components/form/template.pug")
        return html(template.render(vars(data)))