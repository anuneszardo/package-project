# Package Dispatching Service

This project implements a simple package dispatching system used to classify packages based on their **dimensions** and **mass**, determining how they should be handled in a warehouse automation scenario.

The challenge is inspired by real-world logistics and robotic automation decision rules.

---

## Problem Overview

Each package must be dispatched to one of the following stacks:

- **STANDARD** — normal packages
- **SPECIAL** — packages that are bulky *or* heavy
- **REJECTED** — packages that are both bulky *and* heavy

---

## Classification Rules

### Bulky
A package is considered **bulky** if **any** of the following is true:

- Volume (`width × height × length`) ≥ **1,000,000 cm³**
- Any dimension ≥ **150 cm**

### Heavy
A package is considered **heavy** if:

- Mass ≥ **20 kg**

---

## Dispatch Logic

| Bulky | Heavy | Result   |
|------:|------:|----------|
| ❌    | ❌    | STANDARD |
| ✅    | ❌    | SPECIAL  |
| ❌    | ✅    | SPECIAL  |
| ✅    | ✅    | REJECTED |

---

## Implementation

The main entry point is the `sort` function:

```python
def sort(width: float, height: float, length: float, mass: int) -> str:
```

It returns one of:

- `"STANDARD"`
- `"SPECIAL"`
- `"REJECTED"`

The logic is implemented using:
- A `Package` domain model
- Pythonic properties (`is_bulky`, `is_heavy`, `volume`)
- Structural pattern matching (`match / case`)

---

## 📂 Project Structure

```
dispatching/
├── models.py        # Domain models and rules
├── service.py       # Dispatching logic
├── test_service.py  # Unit tests
```

---

## Running Tests

This project uses **pytest**.

```bash
pytest
```

---

## Design Notes

- Clear separation between **business rules** and **dispatch logic**
- Readable and maintainable boolean expressions
- Easy to extend with new dispatch rules
- Fully testable

---

## Requirements

- Python **3.10+** (for `match/case`)
- pytest

---

## Author

Created as a coding exercise to demonstrate clean Python design, readability, and correct handling of edge cases.
