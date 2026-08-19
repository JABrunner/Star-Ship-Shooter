# Docker Agent Environment — Setup Notes

Baseline setup for running a Claude Code agent against this project inside Docker.

## Build

```
docker build -t star-ship-agent .
```

## Run

Only the `Star-Ship-Shooter` project directory is bind-mounted — nothing else on the host is exposed to the container.

```
docker run --rm -it -v "${PWD}:/workspace/Star-Ship-Shooter" -w /workspace/Star-Ship-Shooter star-ship-agent
```

Mount location inside the container: `/workspace/Star-Ship-Shooter`

## Network access

- `--network none` was tested and successfully blocked all network access from the container.
- However, in that mode Claude Code could not reach `api.anthropic.com`, so **interactive Claude Code sessions require network access** — do not add `--network none` when running the agent interactively.
- `--network none` remains useful for **offline, test-only container runs** (e.g. just running pytest, no Claude session), since the test suite itself needs no network access:

```
docker run --rm -it --network none -v "${PWD}:/workspace/Star-Ship-Shooter" -w /workspace/Star-Ship-Shooter star-ship-agent
```

## Smoke test

Command:

```
python -m pytest tests/ -v
```

Result (after the fix below):

```
12 passed, 1 warning in 9.37s
```

## Issue found and fixed

The first container test run failed at collection because `main.py` had an unused `import mixer` statement (line 5). This had gone unnoticed because the host machine happened to have an unrelated third-party `mixer` package installed, masking the missing dependency. Inside the clean container, `mixer` was not installed and import resolution failed for all three test modules.

After explicit approval, the agent removed only that unused import (no other code changes). All 12 tests then passed as shown above.

## Filesystem security

- Only the `Star-Ship-Shooter` project directory is bind-mounted into the container.
- The Windows host's home directory, Desktop, Downloads, SSH directories, credentials, and all other host locations are **not** mounted and are not accessible from inside the container.

## Persistence

- Changes made under `/workspace/Star-Ship-Shooter` persist back to the host (it's a bind mount).
- Everything else in the container is ephemeral: the container is run with `--rm`, so any container-only temporary files or state are discarded when the container exits.

## Secrets / external services

The project requires no environment secrets, API keys, databases, or other local services to build, run, or test.

## Headless Pygame

Pygame needs a display/audio device to initialize, which isn't available in the container. The Dockerfile sets:

```
SDL_VIDEODRIVER=dummy
SDL_AUDIODRIVER=dummy
```

## Versions

- Python 3.10
- pygame 2.1.2
- pytest 9.1.1
