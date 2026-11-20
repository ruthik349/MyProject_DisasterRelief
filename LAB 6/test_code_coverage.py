import pytest
from coffee_shop_order import process_order_batch, check_espresso_machine


def order(**overrides):
    data = {"paid": True, "size": "medium", "customizations": [],
            "strict_allergy": False, "is_member": False}
    data.update(overrides)
    return data


def test_paid_medium_with_standard_addon_and_tax():
    result = process_order_batch([order(customizations=[{"type": "standard", "cost": 0.5}])], 0.1)
    assert result == {"total": 5.5, "status": "COMPLETED"}


def test_unpaid_order_is_skipped():
    assert process_order_batch([order(paid=False)], 0.0) == {"total": 0.0, "status": "NO_SALE"}


def test_all_three_sizes_and_unknown_size():
    result = process_order_batch([order(size="small"), order(size="large"), order(size="xxl")], 0.0)
    assert result == {"total": 9.0, "status": "COMPLETED"}


def test_syrup_cost_is_capped_at_one_point_five():
    result = process_order_batch([order(customizations=[{"type": "syrup", "cost": 2.0}])], 0.0)
    assert result["total"] == 6.0


def test_strict_allergy_alert_voids_item():
    result = process_order_batch([order(strict_allergy=True, customizations=[{"type": "allergen_alert"}])], 0.0)
    assert result == {"total": 0.0, "status": "NO_SALE"}


def test_non_strict_allergy_alert_rejects_modifier_but_keeps_item():
    result = process_order_batch([order(customizations=[{"type": "allergen_alert"}])], 0.0)
    assert result == {"total": 4.5, "status": "COMPLETED"}


def test_negative_customization_is_rejected_without_changing_total():
    result = process_order_batch([order(customizations=[{"type": "standard", "cost": -1}])], 0.0)
    assert result == {"total": 4.5, "status": "COMPLETED"}


def test_member_discount_applies_after_customizations():
    result = process_order_batch([order(is_member=True, customizations=[{"type": "standard", "cost": 0.5}])], 0.0)
    assert result["total"] == 4.5


def test_audit_rejected_after_more_than_four_rejections():
    result = process_order_batch([order(size="bad") for _ in range(5)], 0.0)
    assert result == {"total": 0.0, "status": "AUDIT_REJECTED"}


def test_invalid_batch_inputs_raise_value_error():
    with pytest.raises(ValueError):
        process_order_batch("not-a-list", 0.1)
    with pytest.raises(ValueError):
        process_order_batch([], -0.1)


def test_espresso_machine_no_data_optimal_and_shutdown():
    assert check_espresso_machine([]) == "NO_DATA"
    assert check_espresso_machine([[95.0, 97.0, 96.0, 97.0]]) == "OPTIMAL"
    assert check_espresso_machine([[97.0, 98.0]]) == "SHUTDOWN"
