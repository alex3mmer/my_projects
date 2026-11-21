import database_functions as dbf

print("Entering testing mode for SQL Database program...")

def test_show_users(mocker, capsys):
    mock_connection = mocker.MagicMock()

    mocker.patch(
    "database_functions.database_config.get_connection",
    return_value = mock_connection
    )
    
    cursor = mock_connection.cursor.return_value.__enter__.return_value

    cursor.fetchall.return_value = [
        (1, "Alice", 25),
        (2, "Bob", 30)
    ]

    users = dbf.show_users()

    cursor.execute.assert_called_once_with("SELECT * FROM my_table")

    captured = capsys.readouterr()

    assert "Alice" in captured.out
    assert "Bob" in captured.out