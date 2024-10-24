food_report_schema = {
    "type": "json_schema",
    "json_schema": {
        "name": "food_safety_report",
        "schema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "Name of the food"
                },
                "validity": {
                    "type": "bool",
                    "description": "If the image is a food or not"
                },
                "description": {
                    "type": "string",
                    "description": " What is this food and how it looks"
                },
                "freshness": {
                    "type": "string",
                    "description": "Description of how fresh the food looks."
                },
                "nutrients": {
                    "type": "string",
                    "description": " List of vitamins and minerals in the food"
                },
                "allergic_ingredient": {
                    "type": "string",
                    "description": " If the food contains any common allergic ingredient"
                },
                "physical_hazards": {
                    "type": "string",
                    "description": " If the food contains any external objects like glass, metal fragments or plastic"
                },
                "proper_storage": {
                    "type": "string",
                    "description": " If a packaged food is in proper condition or not"
                }
            },
            "required": ["name", "description"],
            "additionalProperties": False
        }
    }
}