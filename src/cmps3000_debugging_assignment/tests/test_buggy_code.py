from cmps3000_debugging_assignment.buggy_code import Order


def test_add_item():
    order = Order("Alice", [])

    order.add_item("Notebook", 3, 5.00)
    assert len(order.items) == 1

    order.add_item("Pen", 5, 1.50)
    assert len(order.items) == 2


def test_add_item_with_duplicate():
    order = Order("Alice", [])

    order.add_item("Notebook", 3, 5.00)
    assert len(order.items) == 1

    order.add_item("Notebook", 2, 5.00)
    assert len(order.items) == 2


def test_remove_item():
    order = Order("Alice", [("Book", 2, 15.00), ("Pen", 5, 1.50)])
    order.remove_item("Pen")
    assert len(order.items) == 1
    assert order.items[0][0] == "Book"


def test_remove_item_with_empty():
    order = Order("Alice", [])
    order.remove_item("Pen")
    assert len(order.items) == 0


def test_remove_item_with_failure():
    order = Order("Alice", [("Book", 2, 15.00), ("Pen", 5, 1.50)])
    order.remove_item("Pencil")
    assert len(order.items) == 2


def test_remove_item_with_duplicate():
    order = Order("Alice", [("Book", 2, 15.00), ("Pen", 5, 1.50)])
    order.add_item("Pen", 5, 1.50)
    assert len(order.items) == 3

    order.remove_item("Pen")
    assert len(order.items) == 1


def test_order_total():
    order = Order("Alice", [("Book", 2, 15.00), ("Pen", 5, 1.50)])
    assert order.calculate_total() == 37.50


def test_order_total_with_zero_quantity():
    order = Order("Alice", [("Book", 0, 15.00), ("Pen", 5, 1.50)])
    assert order.calculate_total() == 7.50


def test_order_total_with_zero_price():
    order = Order("Alice", [("Book", 2, 0.00), ("Pen", 5, 1.50)])
    assert order.calculate_total() == 7.50


def test_order_total_with_zero_total():
    order = Order("Alice", [("Book", 0, 0.00), ("Pen", 0, 0.00)])
    assert order.calculate_total() == "Empty Order"


def test_apply_discount():
    order = Order("Alice", [("Book", 2, 15.00), ("Pen", 5, 1.50)])
    assert order.apply_discount("SAVE10") == 0.1
    assert order.apply_discount("SAVE20") == 0.2
    assert order.apply_discount("SAVE30") is None
