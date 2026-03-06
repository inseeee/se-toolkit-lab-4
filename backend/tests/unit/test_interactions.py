"""Unit tests for interaction filtering logic."""

from app.models.interaction import InteractionLog
from app.routers.interactions import filter_by_max_item_id


def _make_log(id: int, learner_id: int, item_id: int) -> InteractionLog:
    return InteractionLog(id=id, learner_id=learner_id, item_id=item_id, kind="attempt")


def test_filter_returns_all_when_max_item_id_is_none() -> None:
    interactions = [_make_log(1, 1, 1), _make_log(2, 2, 2)]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=None)
    assert result == interactions


def test_filter_returns_empty_for_empty_input() -> None:
    result = filter_by_max_item_id(interactions=[], max_item_id=1)
    assert result == []


def test_filter_returns_interactions_below_max() -> None:
    interactions = [_make_log(1, 1, 1), _make_log(2, 2, 3)]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=2)
    assert len(result) == 1
    assert result[0].id == 1
def test_filter_includes_interaction_with_different_learner_id():
    """Test that filtering by item_id includes interactions where learner_id differs."""
    from app.routers.interactions import _filter_by_item_id
    interactions = [
        type('Interaction', (), {'item_id': 1, 'learner_id': 2})(),
        type('Interaction', (), {'item_id': 2, 'learner_id': 1})(),
    ]
    filtered = _filter_by_item_id(interactions, 1)
    assert len(filtered) == 1
    assert filtered[0].item_id == 1
    assert filtered[0].learner_id == 2
# ===== AI-generated tests =====

def test_filter_by_item_id_returns_empty_list_when_no_match():
    """Test that filtering by item_id returns empty list when no interactions match."""
    from app.routers.interactions import _filter_by_item_id
    interactions = [
        type('Interaction', (), {'item_id': 2, 'learner_id': 1})(),
        type('Interaction', (), {'item_id': 3, 'learner_id': 2})(),
    ]
    filtered = _filter_by_item_id(interactions, 1)
    assert len(filtered) == 0

def test_filter_by_item_id_returns_all_when_item_id_is_none():
    """Test that filtering with item_id=None returns all interactions."""
    from app.routers.interactions import _filter_by_item_id
    interactions = [
        type('Interaction', (), {'item_id': 1, 'learner_id': 1})(),
        type('Interaction', (), {'item_id': 2, 'learner_id': 2})(),
    ]
    filtered = _filter_by_item_id(interactions, None)
    assert len(filtered) == 2

def test_filter_by_item_id_handles_empty_list():
    """Test that filtering an empty list returns empty list."""
    from app.routers.interactions import _filter_by_item_id
    filtered = _filter_by_item_id([], 1)
    assert len(filtered) == 0

def test_create_interaction_with_minimum_values():
    """Test creating interaction with minimum values (boundary test)."""
    from app.models.interaction import InteractionLogCreate
    interaction = InteractionLogCreate(
        learner_id=1,
        item_id=1,
        kind="a"
    )
    assert interaction.learner_id == 1
    assert interaction.item_id == 1
    assert interaction.kind == "a"
def test_filter_excludes_interaction_with_different_learner_id():
    """Test that filtering by item_id excludes interactions with different item_id."""
    from app.routers.interactions import _filter_by_item_id
    interactions = [
        type('Interaction', (), {'item_id': 2, 'learner_id': 1})(),
        type('Interaction', (), {'item_id': 3, 'learner_id': 2})(),
    ]
    filtered = _filter_by_item_id(interactions, 1)
    assert len(filtered) == 0
