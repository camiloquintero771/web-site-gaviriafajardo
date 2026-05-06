from typing import Dict, Any, List

from django.db.models import QuerySet, F


def get_serialized_query(query: QuerySet, mapped_fields: Dict[str, Any]) -> List[Dict[str, Any]]:
    annotates = {}
    for key, value in mapped_fields.items():
        if isinstance(value, str):
            if key != value:
                annotates.update({key: F(value)})
        else:
            annotates.update({key: value})
    return list(query.annotate(**annotates).values(*list(mapped_fields.keys())))
