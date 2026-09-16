"""Тесты CLI-интерфейса."""
import subprocess
import sys


def test_add_command_output():
    result = subprocess.run(
        [sys.executable, "src/main.py", "add", "Купить хлеб"],
        capture_output=True, text=True,
    )
    assert result.returncode == 0
    assert "Купить хлеб" in result.stdout