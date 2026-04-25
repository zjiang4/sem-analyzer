#!/usr/bin/env python3
"""Test growth model time loadings parsing."""

import sys
import pytest
sys.path.insert(0, '.')

from interaction.followup_processor import FollowupProcessor

@pytest.fixture
def processor():
    return FollowupProcessor()

@pytest.mark.unit
class TestParseTimeLoadings:

    def test_no_numbers_returns_none(self, processor):
        items = ['item1', 'item2', 'item3', 'item4']
        assert processor._parse_time_loadings("增长模型", items) is None
        assert processor._parse_time_loadings("增长模型 载荷", items) is None

    def test_space_separated_numbers(self, processor):
        items = ['item1', 'item2', 'item3', 'item4']
        res = processor._parse_time_loadings("增长模型 0 1 2 3", items)
        assert res == [0,1,2,3]

    def test_comma_separated_after_keyword(self, processor):
        items = ['item1', 'item2', 'item3', 'item4']
        res = processor._parse_time_loadings("增长模型 载荷 0,0.5,1,1.5", items)
        assert res == [0,0.5,1,1.5]

    def test_partial_numbers_returns_none(self, processor):
        items = ['item1', 'item2', 'item3', 'item4']
        # only 2 numbers for 4 items
        res = processor._parse_time_loadings("增长模型 0 1", items)
        assert res is None

    def test_too_many_numbers_returns_none(self, processor):
        items = ['item1', 'item2', 'item3', 'item4']
        res = processor._parse_time_loadings("增长模型 0 1 2 3 4", items)
        assert res is None

    def test_floats_accepted(self, processor):
        items = ['a', 'b', 'c']
        res = processor._parse_time_loadings("增长模型 0 1.5 3", items)
        assert res == [0.0, 1.5, 3.0]

