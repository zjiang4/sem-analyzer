#!/usr/bin/env python3
"""
SEM Analyzer Skill - Interactive SEM analysis via natural language.

Entry point that handles user interactions and routes to appropriate modules.
Auto-installs missing dependencies on load.
"""

import json
import os
import sys
import subprocess
import traceback
from pathlib import Path
from typing import Dict, Any, Optional

SKILL_DIR = Path(__file__).parent.resolve()
sys.path.insert(0, str(SKILL_DIR))


def _ensure_dependencies():
    """Check and auto-install required packages."""
    required = {
        'semopy': 'semopy',
        'pandas': 'pandas',
        'numpy': 'numpy',
        'scipy': 'scipy',
    }
    missing = {}
    for module, package in required.items():
        try:
            __import__(module)
        except ImportError:
            missing[module] = package

    if missing:
        print(f"[sem-analyzer] Installing missing dependencies: {list(missing.values())}")
        for package in missing.values():
            try:
                subprocess.check_call(
                    [sys.executable, '-m', 'pip', 'install', '-q', package],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
                print(f"  ✓ {package} installed")
            except subprocess.CalledProcessError as e:
                print(f"  ✗ Failed to install {package}: {e}")
                raise ImportError(
                    f"Could not auto-install '{package}'. "
                    f"Please run: pip install {package}"
                )
        print("[sem-analyzer] All dependencies ready.")


_ensure_dependencies()

from utils.state_manager import SessionManager
from interaction.clarifier import Clarifier
from interaction.model_confirm import ModelConfirm
from interaction.report_formatter import ReportFormatter
from interaction.followup_processor import FollowupProcessor
from core.data_loader import DataLoader
from core.data_validator import DataValidator
from core.model_draft import ModelDraft
from core.sem_fitter import SemFitter
from core.advanced_fitter import AdvancedFitter
from core.textbook_retriever_v2 import TextbookIndex

class SemAnalyzerSkill:
    """Main skill class for SEM analysis."""

    def __init__(self):
        self.sessions = SessionManager()
        self.clarifier = Clarifier()
        self.model_confirm = ModelConfirm()
        self.report_formatter = ReportFormatter()
        self.followup_processor = FollowupProcessor()
        self.advanced_fitter = AdvancedFitter()
        self.textbook_index: Optional[TextbookIndex] = None

    def _get_textbook_index(self) -> TextbookIndex:
        """Lazy load pre-built handbook index."""
        if self.textbook_index is None:
            index_path = str(SKILL_DIR / 'handbook_index.json')
            self.textbook_index = TextbookIndex(index_path)
        return self.textbook_index

    def process_message(self, message: Dict[str, Any]) -> str:
        """
        Process user message and return response.

        Expected message format:
        {
            "user_id": "unique_id",
            "content": "user text",
            "attachments": [{"path": "...", "type": "file"}],
            "session_id": "optional_existing_session"
        }
        """
        try:
            user_id = message.get("user_id", "default")
            session_id = message.get("session_id")
            content = message.get("content", "").strip()
            attachments = message.get("attachments", [])

            # Get or create session
            session = self.sessions.get_or_create(user_id, session_id)

            # Route based on session state and content
            response = self._route(session, content, attachments)
            return response

        except Exception as e:
            traceback.print_exc()
            return f"Error: {str(e)}\n\nPlease try again or restart the session."

    def _route(self, session, content: str, attachments: list) -> str:
        """Route to appropriate handler based on session state."""
        # Lazy load textbook retriever and advanced fitter
        if not hasattr(session, 'textbook_retriever'):
            try:
                session.textbook_retriever = self._get_textbook_index()
            except Exception as e:
                session.textbook_retriever = None
                print(f"Warning: Textbook retriever not available: {e}")
        if not hasattr(session, 'advanced_fitter'):
            session.advanced_fitter = self.advanced_fitter

        # If there are file attachments, load data and start clarification
        if attachments:
            for att in attachments:
                if att["type"] in ["csv", "excel", "xlsx"]:
                    try:
                        loader = DataLoader()
                        df = loader.load(att["path"])
                        session.data = df
                        session.data_path = att["path"]
                        return self.clarifier.start_clarification(session)
                    except Exception as e:
                        return f"Failed to load file: {e}"

        # If no data yet
        if session.data is None:
            return ("Please upload a data file (CSV/Excel) first, or paste your data.\n"
                    "You can also describe your analysis needs and I will guide you through.")

        # Route based on session.state
        state = getattr(session, 'state', 'initial')

        if state == "clarifying_variables":
            # Multi-step design discovery
            return self.clarifier.handle_clarification(session, content)

        if state == "model_ready_for_confirmation":
            # User reviewing the draft; handle confirm/modify
            return self.model_confirm.handle_confirmation(session, content)

        if state == "model_confirmed":
            # After model confirmed, handle post-confirmation commands (fit, export, etc.)
            return self.followup_processor.handle(session, content)

        # Fallback: unknown state
        return "Session state is unclear. Type 'restart' to begin a new session."


def main():
    """CLI entry point for testing."""
    skill = SemAnalyzerSkill()

    # Simple test loop
    print("SEM Analyzer Skill - CLI Mode")
    print("Type 'quit' to exit.\n")

    session = None
    while True:
        try:
            user_input = input("User: ").strip()
            if user_input.lower() in ['quit', 'exit']:
                break

            # Simulate message format
            msg = {
                "user_id": "cli_user",
                "session_id": session,
                "content": user_input,
                "attachments": []
            }

            response = skill.process_message(msg)
            print(f"Skill: {response}\n")

            # Update session ID from response if changed
            if "session_id" in msg:
                session = msg["session_id"]

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
