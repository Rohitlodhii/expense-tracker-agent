from typing import Any

import numpy as np


class OCRResult:
    json: dict[str, Any]


class PaddleOCR:
    def __init__(self, **kwargs: Any) -> None: ...

    def predict(
        self,
        input: str | np.ndarray,
        **kwargs: Any,
    ) -> list[OCRResult]: ...
