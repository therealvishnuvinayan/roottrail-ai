# RootTrail AI

A small Python learning prototype for summarizing synthetic incident and order data.

## Purpose and status

RootTrail AI began as an independent Python and AI engineering learning project.
**Development is paused at an early prototype stage** after a shift in focus to
BizBrain AI. This repository preserves the foundational Python exercises and tests.

The current code performs deterministic data aggregation. It is not a completed
agentic AI system or a production-ready incident investigation platform.

## Implemented features

- Count total, resolved, and unresolved incidents.
- List unresolved high-severity incident IDs in their original order.
- Count order item entries and total units.
- Select the latest order event by timestamp, regardless of list order, accounting
  for UTC offsets and fractional seconds.
- Return `None` for the latest event when an order has no events; empty item lists
  produce zero counts.
- Run examples locally without credentials or external services.

Summary functions read their input without modifying it.

## Technologies and prerequisites

- Python **3.11 or newer**, including the standard-library `datetime` module.
- Plain lists, dictionaries, functions, and type hints; no runtime dependencies.
- `pytest` for development tests, listed in `requirements-dev.txt`.
- Git to clone the repository, plus Python's `venv` and `pip` for test setup.

## Setup and execution

```sh
git clone https://github.com/therealvishnuvinayan/roottrail-ai.git
cd roottrail-ai
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
```

On Windows, create the environment with `py -3 -m venv .venv` and activate it in
PowerShell with `.venv\Scripts\Activate.ps1`. Run the remaining `python` commands
from the repository root. Installing pytest is only necessary for tests.

```sh
python hello.py
python incident_summary.py
python order_fixtures.py
python order_summary.py
```

The scripts use built-in synthetic fixtures; they do not prompt for input.
`hello.py` prints a prototype greeting and `Environment ready!`.
`order_fixtures.py` prints `3`.

## Examples

The five records in `incident_summary.py` include two resolved incidents and three
unresolved incidents. Running the script prints:

```text
{'total': 5, 'resolved': 2, 'unresolved': 3, 'high_unresolved_ids': ['INC-001', 'INC-005']}
```

`ORDER_NS_1042` in `order_fixtures.py` contains this order:

```python
{
    "order_id": "NS-1042",
    "status": "delayed",
    "items": [
        {"sku": "LAPTOP-01", "quantity": 2},
        {"sku": "MOUSE-01", "quantity": 1},
    ],
    "events": [
        {"name": "EV-001", "type": "order_created", "time": "2026-10-16T21:24:45Z"},
        {"name": "EV-002", "type": "supplier_delay", "time": "2026-10-16T21:26:45Z"},
    ],
}
```

Running `python order_summary.py` prints the following dictionary twice: once for
that fixture and once for the fixture with its events reversed.

```text
{'order_id': 'NS-1042', 'status': 'delayed', 'item_count': 2, 'total_units': 3, 'latest_event': 'supplier_delay'}
```

`item_count` counts entries in the items list, while `total_units` sums quantities.
These outputs are Python dictionary representations, not JSON reports.

## Tests

With the virtual environment active:

```sh
python -m pytest -q
```

Tests cover incident filtering and order, empty inputs, unit counting, reversed
events, timezone offsets, fractional seconds, timestamp ties, invalid timestamps,
and preservation of input records.

## Repository structure

```text
roottrail-ai/
├── README.md
├── docs/
│   └── PROJECT_BOUNDARIES.md  # Scope, original vision, and data boundaries
├── hello.py                  # First environment-check example
├── incident_summary.py       # Incident fixture and aggregation
├── order_fixtures.py          # Synthetic orders and unit counting
├── order_summary.py           # Order aggregation and timestamp comparison
├── requirements-dev.txt       # Test dependency
├── test_incident_summary.py
└── test_order_summary.py
```

## Learning outcomes

The exercises practice Python control flow, nested data structures, reusable
functions, imports, type hints, timestamp parsing, and testing. They also illustrate
why input order differs from event chronology and how to test without mutating
shared fixtures.

## Known limitations

- Input is held in memory; there is no file ingestion, persistence, UI, or API.
- Records must follow the fixture schemas. Incident `resolved` values must be
  booleans, and quantities are expected to be non-negative integers. General
  schema and business-rule validation are not implemented.
- Event times must be ISO 8601 strings accepted by `datetime.fromisoformat`, with
  an explicit UTC offset or `Z`. Invalid or timezone-free timestamps raise
  `ValueError`; missing required fields can raise `KeyError`.
- Equal event timestamps select the first event in the input list.
- The code summarizes supplied data; it does not infer root causes or investigate
  real incidents. No performance or deployment claims are made.

## Original vision — planned, not implemented

The original learning plan envisioned AI-assisted incident investigation across
fictional operational systems: read-only integrations, specialized agents,
evidence gathering, retrieval-augmented generation, structured reports, automated
evaluation, and a deployable application. Those capabilities were not implemented.
There is no FastAPI service, LLM integration, AI agent, RAG pipeline, or database.
The original vision is historical context, not an active delivery commitment.

## Independence and synthetic data

This is an independent personal learning project, separate from employer or client
work. All included incident and order examples are synthetic and contain no real
customer or company records. See [Project boundaries](docs/PROJECT_BOUNDARIES.md)
for scope and ownership constraints.
