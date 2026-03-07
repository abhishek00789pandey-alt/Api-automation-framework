from utils.schema_validator import validate_schema


def test_get_users(api_client):
    response = api_client.get("/users")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    for user in data:
        validate_schema(user, "schemas/user_schema.json")