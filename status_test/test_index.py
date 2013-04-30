import status

app = status.app.test_client()

def test_home_page():
    result = app.get('/')
    assert result.status_code == 200