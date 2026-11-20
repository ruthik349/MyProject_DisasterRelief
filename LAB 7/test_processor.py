import math
import pytest
from hypothesis import given, strategies as st
from processor import lookup_drink_code, calculate_average_shot_cost, parse_order_modifiers


@given(st.text())
def test_lookup_drink_code_no_crash_for_arbitrary_text(value):
    try:
        result = lookup_drink_code(value)
        assert result in {3.0, 3.5, 4.0, 4.5, 5.0}
    except ValueError:
        pass


@given(st.none())
def test_lookup_drink_code_rejects_none(value):
    with pytest.raises(ValueError):
        lookup_drink_code(value)


@given(st.sampled_from(["LAT", "CAP", "ESP", "AME", "MOC", "lat", " moc "]))
def test_lookup_drink_code_known_codes(value):
    assert lookup_drink_code(value) > 0


@given(st.text())
def test_calculate_average_shot_cost_no_crash_for_arbitrary_text(value):
    try:
        result = calculate_average_shot_cost(value)
        assert math.isfinite(result) and result >= 0
    except ValueError:
        pass


@given(st.lists(st.floats(min_value=0, max_value=100, allow_nan=False, allow_infinity=False), min_size=1, max_size=20))
def test_calculate_average_shot_cost_matches_generated_values(values):
    csv = ",".join(str(value) for value in values)
    assert calculate_average_shot_cost(csv) == pytest.approx(sum(values) / len(values))


@given(st.sampled_from(["", "abc", "1,,2", "1,-2", "NaN", "inf"]))
def test_calculate_average_shot_cost_rejects_invalid_data(value):
    with pytest.raises(ValueError):
        calculate_average_shot_cost(value)


@given(st.text())
def test_parse_order_modifiers_no_crash_for_arbitrary_text(value):
    try:
        result = parse_order_modifiers(value)
        assert isinstance(result, dict)
        assert all(key and val for key, val in result.items())
    except ValueError:
        pass


@given(st.dictionaries(
    st.text(alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_", min_size=1, max_size=10),
    st.text(alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_", min_size=1, max_size=10),
    min_size=1,
    max_size=10,
))
def test_parse_order_modifiers_round_trips_generated_pairs(values):
    spec = ";".join(f"{key}:{value}" for key, value in values.items())
    assert parse_order_modifiers(spec) == values


@given(st.sampled_from(["milk:oat;milk:soy", "milk", ":oat", "milk:", "milk:oat;;syrup:vanilla"]))
def test_parse_order_modifiers_rejects_malformed_data(value):
    with pytest.raises(ValueError):
        parse_order_modifiers(value)
