"""Tests for the main window's Tools commands: what the user sees after a click."""

from pathlib import Path

import pytest

from dexpi_studio.gui.main_window import MainWindow

_REFERENCE_PID: Path = Path(__file__).parent.parent / "data" / "reference_pid.xml"


@pytest.fixture
def window(qtbot, monkeypatch, tmp_path):
    from PySide6.QtCore import QSettings

    # The window saves its layout through QSettings(); keep that out of the user's settings.
    QSettings.setDefaultFormat(QSettings.Format.IniFormat)
    QSettings.setPath(QSettings.Format.IniFormat, QSettings.Scope.UserScope, str(tmp_path))
    # The welcome dialog runs modally from the event loop and would block the test.
    monkeypatch.setattr(MainWindow, "_show_welcome", lambda self: None)
    window = MainWindow()
    qtbot.addWidget(window)
    window.show()
    window._load_file(_REFERENCE_PID)
    assert window._model is not None
    return window


def test_validate_shows_its_results(window, monkeypatch):
    """The results go to the Logs panel, which starts hidden: validating opens it."""
    monkeypatch.setattr(
        "dexpi_studio.gui.main_window.validate_model",
        lambda model: [
            {"level": "error", "message": "[rule_a] broken", "source": "Validation"},
            {"level": "warning", "message": "[rule_b] odd", "source": "Validation"},
        ],
    )
    window._messages_dock.hide()

    window.validate()

    assert window._messages_dock.isVisible()
    assert "1 mandatory and 1 recommended" in window._status_bar.currentMessage()


def test_validate_says_when_there_is_nothing_to_report(window, monkeypatch):
    monkeypatch.setattr(
        "dexpi_studio.gui.main_window.validate_model",
        lambda model: [
            {"level": "info", "message": "No validation issues found.", "source": "Validation"}
        ],
    )

    window.validate()

    assert window._messages_dock.isVisible()
    assert window._status_bar.currentMessage() == "Validation: no issues found."


def test_validate_runs_pydexpi_on_the_loaded_model(window):
    window.validate()

    assert window._messages_dock.isVisible()
    assert window._status_bar.currentMessage().startswith("Validation: ")
