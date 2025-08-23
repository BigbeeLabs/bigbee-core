# bigbee_core/api/shared/manage_present_and_respond.py
from fastapi import HTTPException
from fastapi.responses import HTMLResponse
from bigbee_core.api.shared.presenter_result import PresenterResult  # your dataclass
from bigbee_core.api.shared.manager_result import ManagerResult
from typing import Tuple


def manage_and_present(manager_cls, manager_dto, presenter_cls) -> Tuple[PresenterResult, ManagerResult]:
    manager_result: ManagerResult = manager_cls.manage(manager_dto)
    presenter_result: PresenterResult = presenter_cls.present(manager_result)
    return manager_result, presenter_result