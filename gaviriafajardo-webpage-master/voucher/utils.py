from typing import Dict, Any, Optional


def epayco_data_get_value(data: Dict, field_name: str, default_value: Optional[Any] = None) -> Any:
    return data.get(field_name, [default_value])[0]
