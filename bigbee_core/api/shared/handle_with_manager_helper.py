
# use like
# from bigbee_core.api.shared.handle_with_manager_helper import handle_with_manager

from fastapi import HTTPException
from .manager_result import ManagerResult
import traceback

def handle_with_manager(manager_cls, dto, **kwargs):
    try:
        result: ManagerResult = manager_cls.manage(dto, **kwargs)
    except Exception as e:
        print("💥 Exception in manager:")
        traceback.print_exc()
        raise

    if result.is_ok():
        return result.data

    print(f"❌ Manager returned error: {result.error}")
    raise HTTPException(
        status_code=result.status_code,
        detail=result.error or "Unknown error"
    )
