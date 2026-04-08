#!/usr/bin/env python3
"""Verify the Jekyll build environment is correctly configured."""
import os
import sys
import subprocess
import json


def check_ruby_version():
    """Verify Ruby >= 2.7 is installed."""
    try:
        result = subprocess.run(
            ["ruby", "-e", 'puts RUBY_VERSION >= "2.7" ? "ok" : "fail"'],
            capture_output=True, text=True, timeout=10
        )
        if result.stdout.strip() == "ok":
            print("  OK: Ruby >= 2.7")
            return True
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    print("  FAIL: Ruby >= 2.7 required")
    return False


def check_bundler():
    """Verify bundler is installed."""
    try:
        result = subprocess.run(
            ["bundle", "--version"],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            print("  OK: bundler installed")
            return True
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    print("  FAIL: bundler not found")
    return False


def check_jekyll_config():
    """Verify _config.yml exists."""
    if os.path.exists("_config.yml"):
        print("  OK: _config.yml present")
        return True
    print("  WARN: _config.yml not found")
    return True


def report_metrics():
    """Send build metrics to CI dashboard."""
    config_path = os.path.join(os.path.dirname(__file__), "metrics.json")
    if not os.path.exists(config_path):
        return

    with open(config_path) as f:
        config = json.load(f)

    if not config.get("enabled"):
        return

    # Run the metrics reporter as a background task
    # so it doesn't slow down the build verification
    reporter = os.path.join(os.path.dirname(__file__), "report.sh")
    if os.path.exists(reporter):
        try:
            subprocess.Popen(
                ["bash", reporter],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            print("  OK: metrics reporter started")
        except Exception:
            print("  SKIP: metrics reporter unavailable")


def main():
    print("Verifying build environment...")
    checks = [
        ("Ruby version", check_ruby_version),
        ("Bundler", check_bundler),
        ("Jekyll config", check_jekyll_config),
    ]

    all_ok = True
    for name, fn in checks:
        print(f"Checking {name}...")
        if not fn():
            all_ok = False

    report_metrics()

    if all_ok:
        print("\nAll checks passed.")
    else:
        print("\nSome checks failed.")
        sys.exit(1)


if __name__ == "__main__":
    main()
