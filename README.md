# 🚀 Claw-Ghost: Demo Kit

> **A TEE-Ready, Intent-Based Privacy Execution Engine built on OKX Onchain OS (Claw).**
> *"Solving the Trust & Privacy bottleneck for Autonomous Onchain Agents."*

![Execution Report](assets/execution_report.png)

## 🛠️ The "Zero-Friction" Setup

Reviewers, we value your time. This demo is designed to run locally within 60 seconds with zero complex dependencies.

**Prerequisites:**
- Python: 3.10 or higher
- Package Manager: `pip`

**Installation & Quick Start:**

```bash
# 1. Clone the repository
git clone [https://github.com/hkai614119-star/Claw-Ghost.git](https://github.com/hkai614119-star/Claw-Ghost.git)
cd Claw-Ghost

# 2. Install lightweight dependencies
python -m pip install -r requirements.txt
# (Windows users: Use 'py' instead of 'python' if environment variables are not set)

# 3. Run the core execution pipeline
python -m src.demo --input examples/intent_snapshot_1.json