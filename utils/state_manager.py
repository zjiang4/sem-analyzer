#!/usr/bin/env python3
"""Session state management for SEM Analyzer skill."""

import uuid
from datetime import datetime
from typing import Dict, Any, Optional, List
from dataclasses import dataclass, asdict
import json

@dataclass
class SessionState:
    """Represents a user session (Consultant version)."""
    user_id: str
    session_id: str
    created_at: str
    updated_at: str

    # Data & models
    data: Optional[Any] = None  # pandas DataFrame
    data_path: Optional[str] = None
    draft: Optional[Any] = None  # ModelDraft
    results: Optional[Dict] = None

    # State machine
    state: str = "initial"  # initial → data_loaded → clarifying_variables → hypothesis_collected → model_confirmed → results_ready → reporting

    # Variables & design (collected from user)
    variables: Dict[str, Dict] = None  # {name: {type, description, indicators}}
    missing_handling: str = 'FIML'
    hypotheses: List[Dict] = None  # [{'type':'direct','cause':X,'effect':Y}] or mediation

    # Decision log for report
    decision_log: List[Dict] = None

    # Conversation control
    clarification_step: int = 0
    pending_question: Optional[str] = None

    # Injected capabilities
    textbook_retriever: Any = None
    advanced_fitter: Any = None

    # Internal history (auto)
    history: List[Dict] = None

    def __post_init__(self):
        if self.history is None:
            self.history = []
        if self.variables is None:
            self.variables = {}
        if self.hypotheses is None:
            self.hypotheses = []
        if self.decision_log is None:
            self.decision_log = []

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict) -> 'SessionState':
        return cls(**data)

    def add_history(self, action: str, details: Any):
        """Add entry to session history (convenience method)."""
        from datetime import datetime
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "details": details
        }
        if self.history is None:
            self.history = []
        self.history.append(entry)


class SessionManager:
    """Manages user sessions."""

    def __init__(self):
        self.sessions: Dict[str, SessionState] = {}

    def get_or_create(self, user_id: str, session_id: Optional[str] = None) -> SessionState:
        """Get existing session or create new one."""
        key = session_id or f"{user_id}_{uuid.uuid4().hex[:8]}"

        if key in self.sessions:
            session = self.sessions[key]
            session.updated_at = datetime.now().isoformat()
            return session

        # Create new session
        session = SessionState(
            user_id=user_id,
            session_id=key,
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat()
        )
        self.sessions[key] = session
        return session

    def save_draft(self, session: SessionState, draft: Dict):
        """Save model draft to session."""
        session.draft = draft
        session.state = "latent_defined"
        session.updated_at = datetime.now().isoformat()

    def save_results(self, session: SessionState, results: Dict):
        """Save analysis results to session."""
        session.results = results
        session.state = "results_ready"
        session.updated_at = datetime.now().isoformat()

    def get_draft(self, session: SessionState) -> Optional[Dict]:
        return session.draft

    def get_results(self, session: SessionState) -> Optional[Dict]:
        return session.results

    def update_state(self, session: SessionState, state: str):
        """Update session state."""
        session.state = state
        session.updated_at = datetime.now().isoformat()

    def add_history(self, session: SessionState, action: str, details: str):
        """Add entry to session history."""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "details": details
        }
        session.history.append(entry)
