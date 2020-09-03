from rest_framework.views import exception_handler


def custom_exception_handler(exception, context):
    response = exception_handler(exception, context)

    if response:
        updated_data = {}
        updated_data["status_code"] = response.status_code

        updated_data["errors"] = []
        for field, value in response.data.items():
            message = value

            if isinstance(value, list):
                if len(value) <= 1:
                    message = value[0]

            error = {"field": field, "message": message}
            updated_data["errors"].append(error)

        response.data = updated_data

    return response
