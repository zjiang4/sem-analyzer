#!/usr/bin/env python3
"""
Textbook Knowledge Retriever v3 — loads pre-built handbook index.

Returns rich teaching content (summaries, content excerpts, source info)
at every step of the SEM analysis workflow.

Index is pre-built by build_handbook_index.py from 8 SEM textbook Markdown files.
"""

import os
import re
import json
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass

SKILL_DIR = Path(__file__).parent.parent.resolve()


@dataclass
class TeachingSection:
    """A section from a textbook with teaching content."""
    id: str
    source: str
    source_short: str
    title: str
    level: int
    content: str
    summary: str
    keywords: List[str]

    def format_brief(self) -> str:
        return f"  * {self.title} ({self.source_short})"

    def format_with_summary(self) -> str:
        return f"  **{self.title}** ({self.source_short})\n    {self.summary}"

    def format_teaching(self, max_content: int = 600) -> str:
        excerpt = self.content[:max_content]
        excerpt = re.sub(r'#{1,6}\s+', '', excerpt)
        excerpt = excerpt.strip()
        if len(self.content) > max_content:
            excerpt += '...'
        return (f"**{self.title}** ({self.source_short})\n"
                f"{self.summary}\n\n"
                f"Excerpt:\n{excerpt}")


class HandbookIndex:
    """Pre-built index of 8 SEM textbooks with keyword + stage retrieval."""

    def __init__(self, index_path: Optional[str] = None):
        self.sections: Dict[str, dict] = {}
        self.keyword_index: Dict[str, List[str]] = {}
        self.stage_index: Dict[str, List[str]] = {}
        self.source_index: Dict[str, List[str]] = {}
        self.metadata: dict = {}

        if index_path is None:
            index_path = str(SKILL_DIR / 'handbook_index.json')

        if os.path.exists(index_path):
            self._load(index_path)
        else:
            print(f"[sem-analyzer] Handbook index not found at {index_path}")

    def _load(self, path: str):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.sections = data.get('sections', {})
        self.keyword_index = data.get('keyword_index', {})
        self.stage_index = data.get('stage_index', {})
        self.source_index = data.get('source_index', {})
        self.metadata = data.get('metadata', {})
        n = len(self.sections)
        print(f"[sem-analyzer] Loaded handbook index: {n} sections, "
              f"{len(self.keyword_index)} keywords, "
              f"{len(self.stage_index)} stages")

    def _to_section(self, sec_id: str) -> Optional[TeachingSection]:
        d = self.sections.get(sec_id)
        if not d:
            return None
        return TeachingSection(
            id=d['id'],
            source=d['source'],
            source_short=d['source_short'],
            title=d['title'],
            level=d['level'],
            content=d['content'],
            summary=d['summary'],
            keywords=d.get('keywords', []),
        )

    def get_by_stage(self, stage: str, top_k: int = 3) -> List[TeachingSection]:
        """Get sections relevant to an analysis stage."""
        sec_ids = self.stage_index.get(stage, [])
        results = []
        for sid in sec_ids[:top_k]:
            sec = self._to_section(sid)
            if sec:
                results.append(sec)
        return results

    def retrieve(self, query: str, top_k: int = 5) -> List[Tuple[TeachingSection, int]]:
        """Keyword-based retrieval with scoring."""
        terms = re.findall(r'\b\w{4,}\b', query.lower())
        scores: Dict[str, int] = {}
        for term in terms:
            for sid in self.keyword_index.get(term, []):
                scores[sid] = scores.get(sid, 0) + 1
        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        results = []
        for sid, score in ranked[:top_k]:
            sec = self._to_section(sid)
            if sec:
                results.append((sec, score))
        return results

    def format_teaching_for_stage(self, stage: str, max_sections: int = 2,
                                  include_excerpt: bool = True) -> str:
        """Format teaching content for inclusion in a step response."""
        sections = self.get_by_stage(stage, top_k=max_sections)
        if not sections:
            return ""
        lines = ["\nRecommended reading:"]
        for sec in sections:
            if include_excerpt:
                lines.append(f"  **{sec.title}** ({sec.source_short})")
                lines.append(f"    {sec.summary}")
            else:
                lines.append(f"  * {sec.title} ({sec.source_short})")
        return "\n".join(lines)

    def get_teaching_content(self, stage: str, max_chars: int = 1500) -> str:
        """Get full teaching content for a stage (for detailed educational responses)."""
        sections = self.get_by_stage(stage, top_k=2)
        if not sections:
            return ""
        parts = []
        total = 0
        for sec in sections:
            content = sec.format_teaching(max_content=max_chars // 2)
            if total + len(content) > max_chars:
                break
            parts.append(content)
            total += len(content)
        return "\n\n".join(parts)


# Backward-compatible alias
TextbookIndex = HandbookIndex
