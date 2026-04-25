#!/usr/bin/env python3
"""Parse natural language hypotheses into structural paths.

Currently uses simple rule-based approach; can be enhanced with LLM integration.
"""

import re
from typing import List, Tuple


class SimpleLLMParser:
    """Parse hypothesis text to extract causal paths."""

    # Common causal phrases in Chinese and English
    CAUSAL_PHRASES = [
        r'(.+?)影响(.+?)',       # A 影响 B
        r'(.+?)通过(.+?)影响(.+?)',  # A 通过 M 影响 B
        r'(.+?)导致(.+?)',      # A 导致 B
        r'(.+?)引起(.+?)',
        r'(.+?)预测(.+?)',
        r'(.+?)决定(.+?)',
        r'(.+?)作用于(.+?)',
        r'(.+?)对(.+?)有.*影响',  # A 对 B 有影响
        r'(.+?)对(.+?)的.*效应',
        r'(.+?)与(.+?)的关系',
    ]

    def extract_paths(self, text: str, variable_list: List[str] = None) -> List[Tuple[str, str]]:
        """
        Extract causal paths from hypothesis text.

        Args:
            text: User's hypothesis in natural language
            variable_list: Known variable names to match against

        Returns:
            List of (source, destination) tuples
        """
        paths = []

        # If variable list provided, try to match actual variable names first
        if variable_list:
            # Look for patterns like "X → Y" explicitly
            direct = re.findall(r'([A-Za-z0-9_]+)\s*[-→>]\s*([A-Za-z0-9_]+)', text)
            for src, dst in direct:
                if src in variable_list and dst in variable_list:
                    paths.append((src, dst))

        # Also parse causal phrases
        for phrase in self.CAUSAL_PHRASES:
            matches = re.findall(phrase, text)
            for m in matches:
                # m is a tuple of captured groups; last is destination, first-middle is mediator?
                # Simplistically: assume first group = source, last group = destination
                src = m[0].strip()
                dst = m[-1].strip()
                # If variables list provided, ensure they are valid
                if variable_list:
                    if src not in variable_list or dst not in variable_list:
                        continue
                paths.append((src, dst))

        # Remove duplicates while preserving order
        seen = set()
        unique = []
        for p in paths:
            if p not in seen:
                seen.add(p)
                unique.append(p)

        return unique

    def suggest_explanatory_variables(self, text: str, all_vars: List[str]) -> List[str]:
        """Suggest which variables might be explanatory (independent)."""
        # Variables mentioned early in the text are likely causes
        words = text.split()
        early = set(words[:len(words)//2])
        suggested = []
        for var in all_vars:
            if var.lower() in [w.lower() for w in early]:
                suggested.append(var)
        return suggested

    def suggest_outcome_variables(self, text: str, all_vars: List[str]) -> List[str]:
        """Suggest which variables might be outcomes (dependent)."""
        # Variables with verbs like "影响", "决定", "导致" following them
        # For now, return empty; future improvement
        return []
