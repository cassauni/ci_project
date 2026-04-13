from __future__ import annotations

from typing import Callable


def add(a: float, b: float) -> float:
 return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b


def power(a: float, b: float) -> float:
    return a**b


def modulo(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a % b


OPERATIONS: dict[str, Callable[[float, float], float]] = {
    "+": add,
    "add": add,
    "-": subtract,
    "sub": subtract,
    "*": multiply,
    "mul": multiply,
    "x": multiply,
    "/": divide,
    "div": divide,
    "^": power,
    "pow": power,
    "%": modulo,
    "mod": modulo,
}


def calculate(a: float, b: float, operation: str) -> float:
    key = operation.strip().lower()
    if key not in OPERATIONS:
        raise ValueError(f"Unsupported operation: {operation}")
    return OPERATIONS[key](a, b)


def _parse_number(raw_value: str) -> float:
    normalized = raw_value.replace(",", ".")
    try:
        return float(normalized)
    except ValueError as exc:
        raise ValueError(f"Invalid number: {raw_value}") from exc


def run_cli() -> None:
    print("Calculator started. Enter expressions like: 2 + 2")
    print("Supported operations: +, -, *, /, ^, %")
    print("Type 'exit' to finish")

    while True:
        user_input = input("> ").strip()
        if user_input.lower() in {"exit", "quit", "q"}:
            print("Bye")
            return

        parts = user_input.split()
        if len(parts) != 3:
            print("Use format: <number> <operation> <number>")
            continue

        left_raw, operation, right_raw = parts
        try:
            left = _parse_number(left_raw)
            right = _parse_number(right_raw)
            result = calculate(left, right, operation)
            print(result)
        except (ValueError, ZeroDivisionError) as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    run_cli()
