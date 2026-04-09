#!/usr/bin/env python3
"""Environment variable validator for CI pipelines.

Checks that required environment variables are present before running
CI steps. Does NOT read or log values — only checks existence.
"""

import os
import sys

# Required env vars for different CI contexts
REQUIRED_VARS = {
    "build": [
        "CI",
        "GITHUB_REPOSITORY",
        "GITHUB_SHA",
    ],
    "deploy": [
        "CI",
        "GITHUB_REPOSITORY",
        "GITHUB_SHA",
        "GITHUB_TOKEN",
    ],
    "release": [
        "CI",
        "GITHUB_REPOSITORY",
        "GITHUB_SHA",
        "GITHUB_TOKEN",
        "PAGES_TOKEN",
    ],
}


def validate_env(context: str) -> list[str]:
    """Check that all required vars for the given context exist.

    Args:
        context: One of 'build', 'deploy', 'release'.

    Returns:
        List of missing variable names (empty if all present).
    """
    required = REQUIRED_VARS.get(context, REQUIRED_VARS["build"])
    missing = [var for var in required if var not in os.environ]
    return missing


def main():
    context = sys.argv[1] if len(sys.argv) > 1 else "build"

    if context not in REQUIRED_VARS:
        print(f"Unknown context: {context}")
        print(f"Available: {', '.join(REQUIRED_VARS.keys())}")
        sys.exit(1)

    print(f"Validating environment for '{context}' context...")
    missing = validate_env(context)

    if missing:
        print(f"ERROR: Missing required environment variables:")
        for var in missing:
            print(f"  - {var}")
        sys.exit(1)

    print(f"All {len(REQUIRED_VARS[context])} required variables present.")
    sys.exit(0)


if __name__ == "__main__":
    main()
