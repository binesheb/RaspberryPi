# Raspberry Pi Projects

A small collection of focused Raspberry Pi learning examples covering GPIO, PWM, serial communication, ultrasonic distance measurement, and a basic PyQt5 interface.

> **Status:** historical/learning repository. The examples were originally added in 2018–2019 and are preserved as a reference baseline rather than presented as a modern Raspberry Pi framework.

## Included examples

- **LedBlink** — toggles GPIO 18 and includes a basic PWM duty-cycle example.
- **Serial** — simple serial send/receive examples, modernized for Python 3.
- **distance** — measures distance with an HC-SR04 sensor and transmits the result over serial. This legacy example still uses Python 2 syntax and should be treated as reference-only until it is explicitly audited and modernized.
- **PyQt5** — minimal Python/Qt message-box example.

## Before running

These scripts directly interact with hardware. Pin numbering, permissions, Python versions, and library APIs may differ on current Raspberry Pi OS releases.

1. Inspect the script before wiring hardware.
2. Confirm the GPIO mode and physical pin mapping.
3. Use a virtual environment for Python dependencies where practical.
4. Test with non-critical hardware first.
5. Check the example's supported Python version before running it; do not assume every legacy example is Python 3 compatible.

## Updating

### Manual update

From an existing clone:

```bash
git fetch --tags --prune
git pull --ff-only
```

`--ff-only` avoids silently creating a merge commit when local changes are present.

### Reproducible versions

For a stable snapshot, pin to a tag or known commit instead of tracking `master`:

```bash
git checkout <tag-or-commit>
```

### Rollback

To return to a previously known revision:

```bash
git checkout <previous-tag-or-commit>
```

### Automatic updates

Automatic self-updating is intentionally **not enabled**. These examples can control GPIO and attached devices, so unattended updates could change hardware behaviour without validation. A future automatic update mechanism should use tested tagged releases, compatibility checks, and an explicit rollback path.

## Versioning and releases

Repository maintenance follows [Semantic Versioning](https://semver.org/): patch releases cover safe fixes and documentation, minor releases add backward-compatible examples or capabilities, and major releases may change compatibility or structure. See [CHANGELOG.md](CHANGELOG.md) for release notes.

## Next modernization steps

- Audit the remaining legacy examples, especially the HC-SR04 distance example, against current Raspberry Pi OS and supported Python versions.
- Add dependency metadata and per-example setup instructions.
- Add safe GPIO cleanup and validation where legacy scripts need it.
- Establish tested tagged releases before introducing unattended updates.

## Scope

This repository intentionally remains a set of small, independent examples. Larger Raspberry Pi products should keep their own architecture, deployment, and update mechanisms rather than coupling themselves to this learning repository.
