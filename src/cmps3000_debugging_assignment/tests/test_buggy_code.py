from cmps3000_debugging_assignment.buggy_code import Order, main


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
    assert order.calculate_total() == 0


def test_apply_discount():
    order = Order("Alice", [("Book", 2, 15.00), ("Pen", 5, 1.50)])
    assert order.apply_discount("SAVE10") == 0.1
    assert order.apply_discount("SAVE20") == 0.2
    assert order.apply_discount("SAVE30") is None


def test_print_summary(capsys):
    order = Order("Alice", [("Book", 2, 15.00), ("Pen", 5, 1.50)])
    order.print_summary()
    captured = capsys.readouterr()

    assert "Order Summary for Alice" in captured.out
    assert "2 x Book @ $15.00" in captured.out
    assert "5 x Pen @ $1.50" in captured.out
    assert "Total: $ 37.5" in captured.out


def test_print_summary_empty(capsys):
    order = Order("Alice", [])
    order.print_summary()
    captured = capsys.readouterr()

    assert "Order Summary for Alice" in captured.out
    assert "Total: $ 0" in captured.out


def test_main_function(capsys):

    main()
    captured = capsys.readouterr()

    assert "Order Summary for Alice" in captured.out
    assert "3 x Notebook @ $5.00" in captured.out
    assert "Total: $ 45" in captured.out
    assert "Discount rate: None" in captured.out
