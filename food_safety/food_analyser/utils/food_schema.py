food_report_schema = {
    "type": "json_schema",
    "json_schema": {
        "name": "food_safety_report",
        "schema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string"
                },
                "description": {
                    "type": "string"
                }
            },
            "required": ["name", "description"],
            "additionalProperties": False
        }
    }
}