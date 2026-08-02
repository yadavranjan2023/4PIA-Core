"""
4PIA-Core Quickstart Example
----------------------------
Demonstrates how to load a 4PIA SKILL.md manifest into an AI agent runtime 
to enforce Hard Circuit Breakers (Tier 1) and Dynamic Guidance (Tier 2).
"""

import os
import re
from pathlib import Path

# 1. Load a Governance Manifest
MANIFEST_PATH = Path(__file__).parent.parent / ".well-known" / "skills" / "4PIA-manifests" / "CISO.SKILL.md"

def load_manifest(filepath: Path) -> str:
    """Reads the SKILL.md manifest into string format for system prompt injection."""
    if not filepath.exists():
        raise FileNotFoundError(f"Manifest not found at {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

# 2. Simulated Runtime Circuit Breaker Evaluator (Tier 1)
def evaluate_tier_1_circuit_breakers(user_prompt: str) -> bool:
    """
    Simulates a background evaluation engine checking for hard policy breaches 
    (e.g., unauthorized data exfiltration, raw unmasked PII).
    """
    # Pattern detecting raw social security numbers or credit card numbers
    pii_pattern = r"\b\d{3}-\d{2}-\d{4}\b|\b(?:\d[ -]*?){13,16}\b"
    
    if re.search(pii_pattern, user_prompt):
        return False  # BREACH DETECTED: Trigger Circuit Breaker
    return True

# 3. Agent Execution Pipeline
def run_governed_agent(user_prompt: str, manifest_text: str):
    print(f"\n--- Processing User Input ---")
    print(f"Input: '{user_prompt}'\n")

    # Step A: Evaluate Tier 1 Hard Circuit Breakers
    is_safe = evaluate_tier_1_circuit_breakers(user_prompt)
    if not is_safe:
        print("❌ [TIER 1 CIRCUIT BREAKER TRIGGERED]")
        print("Action Blocked: Unmasked PII or unauthorized data transfer detected in context.")
        print("Status: Refusal response dispatched to audit log.")
        return

    # Step B: Tier 2 Dynamic Guidance Pipeline
    print("✅ [TIER 1 PASSED] Executing Request under Tier 2 Guidance...")
    
    # Simulated model execution response
    simulated_ai_response = (
        "Drafting endpoint security update policy for remote developer workstations...\n\n"
        "--- GOVERNANCE IMPACT SUMMARY (4PIA CISO LENS) ---\n"
        "• Security Posture: Enforces zero-trust telemetry across all local developer tools.\n"
        "• Data Protection: Verifies no authentication tokens are logged to unencrypted streams."
    )
    
    print("\nAgent Output:")
    print(simulated_ai_response)


if __name__ == "__main__":
    print("Initializing 4PIA-Core Engine...")
    ciso_manifest = load_manifest(MANIFEST_PATH)
    print(f"Loaded Manifest: CISO.SKILL.md ({len(ciso_manifest)} bytes)")

    # Test Case 1: Safe Operational Request (Tier 2 Execution)
    run_governed_agent(
        user_prompt="Draft a security policy for developer workstations.",
        manifest_text=ciso_manifest
    )

    # Test Case 2: Violation Triggering Tier 1 Circuit Breaker
    run_governed_agent(
        user_prompt="Export customer records with SSN 000-12-3456 to external server.",
        manifest_text=ciso_manifest
    )
