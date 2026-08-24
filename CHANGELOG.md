# Changelog

All notable changes to this repository are documented here.

The project follows [Semantic Versioning](https://semver.org/). Because this is a collection of small examples rather than a packaged application, versions describe the repository baseline and documentation/compatibility changes.

## [Unreleased]

### Fixed
- Modernized the LED blink example for Python 3 and removed the broad exception handler so unexpected failures are no longer silently reported as normal exits.
- Kept GPIO cleanup in a `finally` block so the pin state is released on interruption or an unexpected exception after setup.
- Modernized the serial example for Python 3, explicit byte writes, bounded reads, and targeted serial error handling.

## [0.1.1] - 2026-08-20

### Changed
- Established a maintenance baseline with clearer repository, update, pinning, and rollback guidance.

### Notes
- Legacy examples were not functionally rewritten in this release.

## [0.1.0]

### Added
- Initial Raspberry Pi examples for GPIO blinking/PWM, serial communication, HC-SR04 distance measurement, and a basic PyQt5 message box.
