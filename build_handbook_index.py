#!/usr/bin/env python3
"""
Build a tree-structured textbook index from handbook Markdown files.
Inspired by BookRAG's DocumentTree, but uses Markdown heading hierarchy
instead of LLM-based outline extraction.

Outputs: handbook_index.json (self-contained, no runtime LLM needed)
"""

import os
import re
import json
import hashlib
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict, field


@dataclass
class Section:
    id: str
    source: str
    source_short: str
    title: str
    level: int
    content: str
    summary: str
    keywords: List[str] = field(default_factory=list)
    children_ids: List[str] = field(default_factory=list)
    parent_id: Optional[str] = None

    def to_dict(self):
        return {
            'id': self.id,
            'source': self.source,
            'source_short': self.source_short,
            'title': self.title,
            'level': self.level,
            'content': self.content[:2000],
            'summary': self.summary,
            'keywords': self.keywords,
            'children_ids': self.children_ids,
            'parent_id': self.parent_id,
        }


SOURCE_SHORTNAMES = {
    'Advanced_Structural_Equation_Modeling_Issues': 'SEM Reference A',
    'Growth_Modeling_Structural_Equation': 'SEM Reference B',
    'Handbook_of_Structural_Equation_Modeling': 'SEM Reference C',
    'Longitudinal_Data_Analysis_Using_Structural': 'SEM Reference D',
    'Longitudinal_Structural_Equation_Modeling_20': 'SEM Reference E',
    'Longitudinal_Structural_Equation_Modeling_with_Mplus': 'SEM Reference F',
    'Principles_and_practice_of_structural_equation': 'SEM Reference G',
    'Structural_Equation_Modeling_for_Health_and_Medicine': 'SEM Reference H',
}

SEM_GLOSSARY = {
    'factor', 'latent', 'covariance', 'correlation', 'regression',
    'parameter', 'estimate', 'chi-square', 'chi', 'cfi', 'tli', 'rmsea',
    'srmr', 'aic', 'bic', 'indicator', 'measurement', 'structural',
    'path', 'mediation', 'moderation', 'missing', 'bootstrap',
    'estimation', 'robust', 'validity', 'reliability', 'multilevel',
    'longitudinal', 'growth', 'item', 'response', 'irt', 'sem',
    'model', 'fit', 'loading', 'intercept', 'residual', 'variance',
    'invariance', 'metric', 'scalar', 'configural', 'identification',
    'endogenous', 'exogenous', 'direct', 'indirect', 'total',
    'effect', 'moderator', 'mediator', 'observed', 'confirmatory',
    'exploratory', 'cross-loading', ' Heywood', 'multicollinearity',
    'normality', 'outlier', 'sample', 'power', 'degree',
    'likelihood', 'maximum', 'ml', 'gls', 'wls', 'dwls',
    'fiml', 'listwise', 'pairwise', 'imputation', 'em',
}

STOPWORDS = {
    'the', 'and', 'for', 'with', 'from', 'this', 'that', 'were', 'which',
    'through', 'chapter', 'section', 'index', 'preface', 'contents',
    'acknowledgments', 'editorial', 'board', 'vol', 'ed', 'edition',
    'handbook', 'advanced', 'approaches', 'methods', 'perspective',
    'using', 'based', 'also', 'such', 'can', 'may', 'will', 'are',
    'been', 'has', 'had', 'was', 'its', 'not', 'all', 'more', 'than',
    'each', 'when', 'where', 'what', 'how', 'why', 'who', 'some',
    'into', 'over', 'only', 'very', 'just', 'about', 'above',
    'between', 'after', 'before', 'other', 'these', 'those',
    'should', 'would', 'could', 'their', 'there', 'being',
    'however', 'therefore', 'thus', 'hence', 'although',
}


def _short_name(source_file: str) -> str:
    for key, short in SOURCE_SHORTNAMES.items():
        if key in source_file:
            return short
    return source_file[:30]


def _extract_keywords(title: str, content: str) -> List[str]:
    text = (title + ' ' + content[:500]).lower()
    words = re.findall(r'\b[a-z]{4,}\b', text)
    kws = []
    seen = set()
    for w in words:
        if w in seen or w in STOPWORDS:
            continue
        seen.add(w)
        kws.append(w)
        if len(kws) >= 20:
            break
    priority = [w for w in kws if w in SEM_GLOSSARY]
    others = [w for w in kws if w not in SEM_GLOSSARY]
    return priority + others[:10]


def _make_summary(content: str, max_len: int = 200) -> str:
    text = content.strip()
    text = re.sub(r'#{1,6}\s+', '', text)
    text = re.sub(r'\n{2,}', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    sentences = re.split(r'(?<=[.!?])\s+', text)
    summary = ''
    for s in sentences:
        if len(summary) + len(s) + 1 > max_len:
            break
        summary += (' ' if summary else '') + s
    return summary if summary else text[:max_len] + '...'


def _is_noise(title: str) -> bool:
    t = title.lower().strip()
    noise = [
        r'^index$', r'^author index$', r'^subject index$', r'^preface',
        r'^contents', r'^acknowledgments?', r'^editorial',
        r'^cover design', r'^library of congress', r'^copyright',
        r'^table of contents', r'^references$', r'^bibliography',
        r'^about the author', r'^about the editors',
    ]
    return any(re.search(p, t) for p in noise)


def parse_md_to_sections(filepath: Path) -> List[Section]:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    source = filepath.name
    short = _short_name(source)

    headings = []
    heading_re = re.compile(r'^(#{1,3})\s+(.+)$')
    for i, line in enumerate(lines):
        m = heading_re.match(line.strip())
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            if not _is_noise(title):
                headings.append((i, level, title))

    if not headings:
        return []

    sections = []
    MIN_CONTENT = 100

    for idx, (start, level, title) in enumerate(headings):
        end = headings[idx + 1][0] - 1 if idx + 1 < len(headings) else len(lines) - 1
        content = ''.join(lines[start:end + 1]).strip()

        if len(content) < MIN_CONTENT:
            continue

        sec_id = hashlib.md5(f"{source}:{start}:{title}".encode()).hexdigest()[:12]
        summary = _make_summary(content)
        keywords = _extract_keywords(title, content)

        sections.append(Section(
            id=sec_id,
            source=source,
            source_short=short,
            title=title,
            level=level,
            content=content,
            summary=summary,
            keywords=keywords,
        ))

    # Build parent-child relationships
    id_by_idx = {}
    for i, s in enumerate(sections):
        id_by_idx[i] = s.id

    for i, sec in enumerate(sections):
        for j in range(i - 1, -1, -1):
            if sections[j].level < sec.level:
                sec.parent_id = sections[j].id
                sections[j].children_ids.append(sec.id)
                break

    return sections


def build_index(handbook_dir: str, output_path: str):
    hb = Path(handbook_dir)
    all_sections = []
    keyword_index: Dict[str, List[str]] = {}
    stage_index: Dict[str, List[str]] = {}
    source_index: Dict[str, List[str]] = {}

    for md_file in sorted(hb.glob('*.md')):
        sections = parse_md_to_sections(md_file)
        print(f"  {md_file.name[:50]}...  {len(sections)} sections")
        for sec in sections:
            all_sections.append(sec)
            source_index.setdefault(sec.source_short, []).append(sec.id)
            for kw in sec.keywords:
                keyword_index.setdefault(kw, []).append(sec.id)

    STAGE_KEYWORDS = {
        'data_preparation': ['data', 'preparation', 'missing', 'sample', 'cleaning',
                             'normality', 'outlier', 'screening'],
        'model_specification': ['model', 'specification', 'path', 'diagram', 'hypothesis',
                                'conceptual', 'theory'],
        'measurement_model': ['factor', 'measurement', 'validity', 'reliability', 'indicator',
                              'loading', 'confirmatory', 'exploratory', 'cfa', 'efa'],
        'structural_model': ['structural', 'path', 'coefficient', 'mediation', 'moderation',
                             'direct', 'indirect', 'effect'],
        'model_fitting': ['estimation', 'fitting', 'ml', 'gls', 'wls', 'maximum', 'likelihood',
                          'robust', 'estimator'],
        'fit_indices': ['fit', 'index', 'cfi', 'tli', 'rmsea', 'srmr', 'chi', 'chi-square',
                        'goodness'],
        'model_modification': ['modification', 'residual', 'mi', 'correction', 're-specification',
                               ' Heywood'],
        'multigroup_analysis': ['multigroup', 'invariance', 'metric', 'scalar', 'configural',
                                'group', 'comparison'],
        'growth_modeling': ['growth', 'longitudinal', 'trajectory', 'slope', 'intercept',
                            'latent growth', 'time', 'wave'],
        'reporting': ['report', 'writing', 'result', 'interpretation', 'apa', 'table',
                      'figure', 'publication'],
        'bootstrap': ['bootstrap', 'resampling', 'confidence', 'interval', 'bca',
                      'bias', 'corrected'],
    }

    for stage, kws in STAGE_KEYWORDS.items():
        sec_scores: Dict[str, int] = {}
        for kw in kws:
            for sec_id in keyword_index.get(kw, []):
                sec_scores[sec_id] = sec_scores.get(sec_id, 0) + 1
        ranked = sorted(sec_scores.items(), key=lambda x: x[1], reverse=True)
        stage_index[stage] = [sid for sid, _ in ranked[:15]]

    index_data = {
        'sections': {s.id: s.to_dict() for s in all_sections},
        'keyword_index': keyword_index,
        'stage_index': stage_index,
        'source_index': source_index,
        'metadata': {
            'total_sections': len(all_sections),
            'total_sources': len(source_index),
            'total_keywords': len(keyword_index),
            'stages': list(STAGE_KEYWORDS.keys()),
        }
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)

    print(f"\nIndex saved to {output_path}")
    print(f"  {len(all_sections)} sections from {len(source_index)} sources")
    print(f"  {len(keyword_index)} unique keywords")
    print(f"  {len(stage_index)} analysis stages")
    return index_data


if __name__ == '__main__':
    hb_dir = os.path.join(os.path.dirname(__file__), 'handbooks')
    out_path = os.path.join(os.path.dirname(__file__), 'handbook_index.json')
    build_index(hb_dir, out_path)
