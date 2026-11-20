from coffee_shop_order import process_order_batch, check_espresso_machine

def make_order(**kwargs):
    base = {"paid": True, "size": "medium", "customizations": [], "strict_allergy": False, "is_member": False}
    base.update(kwargs)
    return base

def test_01_empty_batch_no_sale():
    assert process_order_batch([], 0) == {"total": 0.0, "status": "NO_SALE"}
def test_02_unpaid_order_skips():
    assert process_order_batch([make_order(paid=False)], 0)["status"] == "NO_SALE"
def test_03_small_size():
    assert process_order_batch([make_order(size="small")], 0)["total"] == 3.0
def test_04_medium_size():
    assert process_order_batch([make_order(size="medium")], 0)["total"] == 4.5
def test_05_large_size():
    assert process_order_batch([make_order(size="large")], 0)["total"] == 6.0
def test_06_invalid_size():
    assert process_order_batch([make_order(size="extra")], 0)["status"] == "NO_SALE"
def test_07_negative_cost_rejected():
    assert process_order_batch([make_order(customizations=[{"type":"x","cost":-2}])], 0)["total"] == 4.5
    assert process_order_batch([make_order(customizations=[{"type":"x","cost":"bad"}])], 0)["total"] == 4.5
    assert process_order_batch([make_order(customizations=["not-a-dict"])], 0)["total"] == 4.5
    assert process_order_batch([make_order(customizations="not-a-list")], 0)["total"] == 4.5
def test_08_syrup_under_cap():
    assert process_order_batch([make_order(customizations=[{"type":"syrup","cost":1}])], 0)["total"] == 5.5
def test_09_syrup_at_cap():
    assert process_order_batch([make_order(customizations=[{"type":"syrup","cost":1.5}])], 0)["total"] == 6.0
def test_10_syrup_over_cap():
    assert process_order_batch([make_order(customizations=[{"type":"syrup","cost":3}])], 0)["total"] == 6.0
def test_11_other_modifier():
    assert process_order_batch([make_order(customizations=[{"type":"milk","cost":0.75}])], 0)["total"] == 5.25
def test_12_non_strict_allergen():
    assert process_order_batch([make_order(customizations=[{"type":"allergen_alert"}])], 0)["total"] == 4.5
def test_13_strict_allergen():
    assert process_order_batch([make_order(strict_allergy=True,customizations=[{"type":"allergen_alert"}])], 0)["status"] == "NO_SALE"
def test_14_member_discount():
    assert process_order_batch([make_order(is_member=True)], 0)["total"] == 4.05
def test_15_non_member_no_discount():
    assert process_order_batch([make_order(is_member=False)], 0)["total"] == 4.5
def test_16_audit_threshold_not_crossed():
    assert process_order_batch([make_order(size="bad") for _ in range(4)], 0)["status"] == "NO_SALE"
def test_17_audit_threshold_crossed():
    assert process_order_batch([make_order(size="bad") for _ in range(5)], 0)["status"] == "AUDIT_REJECTED"
def test_18_tax_applied():
    assert process_order_batch([make_order()], 0.1)["total"] == 4.95
def test_19_invalid_orders_type():
    assert process_order_batch(["not-an-order"], 0)["status"] == "NO_SALE"
    try:
        process_order_batch(None, 0)
    except ValueError:
        assert True
    else:
        assert False
def test_20_invalid_tax_rate():
    try:
        process_order_batch([], -1)
    except ValueError:
        assert True
    else:
        assert False
def test_21_espresso_empty_cycles():
    assert check_espresso_machine([]) == "NO_DATA"
def test_22_espresso_normal_temperature():
    assert check_espresso_machine([[90, 95, 96]]) == "OPTIMAL"
def test_23_espresso_one_high_reading_resets():
    assert check_espresso_machine([[]]) == "OPTIMAL"
    assert check_espresso_machine([[97, 96, 97]]) == "OPTIMAL"
def test_24_espresso_two_consecutive_high_readings():
    assert check_espresso_machine([[97, 98]]) == "SHUTDOWN"
def test_25_espresso_shutdown_across_cycles_not_carried():
    assert check_espresso_machine([[97], [98]]) == "OPTIMAL"
