# bigbee_core/services/shared/base_service.py

from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from bigbee_core.services.shared.service_result import ServiceResult

TInput = TypeVar("TInput")
TOutput = TypeVar("TOutput")

class BaseService(ABC, Generic[TInput, TOutput]):
    @staticmethod
    @abstractmethod
    def call(dto: TInput) -> ServiceResult[TOutput]:
        pass