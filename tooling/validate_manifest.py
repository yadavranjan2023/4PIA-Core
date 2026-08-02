#!/usr/bin/env python3
"""
4PIA Manifest Linter & Validator
Author: Rani Yadav-Ranjan
Description: Validates YAML frontmatter headers, structural formatting,
             and required metadata keys across all SKILL.md manifests.
"""

import os
import sys

def validate_skill_file(filepath):
    """Validates a single SKILL.md file for proper YAML frontmatter and formatting."""
    print(f"Validating: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    errors = []
    
    # 1. Check starting YAML frontmatter delimiter
    if not content.startswith('---'):
        errors.append("Missing starting '---' YAML frontmatter delimiter.")
    
    parts = content.split('---')
    if len(parts) < 3:
        errors.append("Invalid YAML frontmatter structure. Must be enclosed by '---'.")
    else:
        yaml_text = parts[1]
        
        # 2. Verify required YAML metadata keys
        required_keys = ['name:', 'description:', 'version:']
        for key in required_keys:
            if key not in yaml_text:
                errors.append(f"Missing required YAML header key: '{key.replace(':', '')}'")
    
    # 3. Check for main H1 Heading
    if "# " not in content:
        errors.append("Missing main Title (# Heading) in Markdown content.")
    
    return errors


def main():
    # Find all SKILL.md / *.SKILL.md files using os.walk to ensure hidden folders (.well-known) are scanned
    skill_files = []
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith("SKILL.md"):
                skill_files.append(os.path.join(root, file))
    
    skill_files = sorted(list(set(skill_files)))
    
    if not skill_files:
        print("❌ No .SKILL.md manifests found to validate.")
        sys.exit(1)
        
    total_errors = 0
    print(f"Found {len(skill_files)} skill manifest(s) to validate:\n")
    
    for sf in skill_files:
        errs = validate_skill_file(sf)
        if errs:
            print(f"  ❌ FAIL: {sf}")
            for e in errs:
                print(f"     - {e}")
            total_errors += len(errs)
        else:
            print(f"  ✅ PASS: {sf}")
            
    print("\n--- Validation Summary ---")
    if total_errors == 0:
        print("🎉 All SKILL.md manifests passed validation successfully!")
        sys.exit(0)
    else:
        print(f"💥 Validation failed with {total_errors} error(s).")
        sys.exit(1)


if __name__ == "__main__":
    main()