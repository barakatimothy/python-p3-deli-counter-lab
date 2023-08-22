katz_deli = []

def line(queue):
    if not queue:
        return "The line is currently empty."
    else:
        queue_str = ', '.join(queue)
        return f"The line is currently: {queue_str}"

def take_a_number(queue, name):
    queue.append(name)
    position = len(queue)
    return f"Welcome, {name}. You are number {position} in line."

def now_serving(queue):
    if not queue:
        return "There is nobody waiting to be served!"
    else:
        serving = queue.pop(0)
        return f"Now serving {serving}."

def test_line_when_empty():
    assert line(katz_deli) == "The line is currently empty."

def test_take_a_number():
    assert take_a_number(katz_deli, "Alice") == "Welcome, Alice. You are number 1 in line."

def test_now_serving():
    katz_deli.append("Bob")
    assert now_serving(katz_deli) == "Now serving Bob."
    assert katz_deli == []

def test_line_with_people():
    katz_deli.extend(["Carol", "David", "Eve"])
    assert line(katz_deli) == "The line is currently: Carol, David, Eve"


