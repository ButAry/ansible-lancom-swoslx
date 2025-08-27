# Conventions, Tips, and Pitfalls

As you design and develop modules, follow these basic conventions and tips for clean, usable code:

## Scoping your module(s)
- Each module should have a concise and well-defined functionality—basically, follow the UNIX philosophy of doing one thing well.
- Do not add `get`, `list`, or `info` functionality to an existing module—create a new `_info` or `_facts` module instead.
- Your module should encapsulate most logic for interacting with a resource. If the API is complex, consider creating multiple modules for smaller pieces.
- Avoid creating a module that internally calls other modules—that should be done with a role.

## Designing module interfaces
- When addressing an object, use `name` as the option name whenever possible—or support it as an alias.
- Boolean parameters should accept variants like `yes`, `no`, `true`, `false` (handled via `type='bool'`).
- Avoid imperative constructs like `action` or `command`; prefer declarative patterns.

## General guidelines & tips
- Keep each module in a **single file** to ensure compatibility with `ansible-core` auto-transfer.
- **Module names must use underscores**, not hyphens or spaces—hyphens/spaces prevent `ansible-core` import.
- Always use the **`hacking/test-module.py`** script during development to catch common pitfalls early.
- Minimize dependencies. If needed, document them at the module top and handle import failures via a JSON error.
- Avoid writing files directly; instead, write to a temporary file and then use `atomic_move` from `ansible.module_utils.basic`.
- Avoid implementing caches—Ansible isn’t designed for centralized authority. If needed, handle that logic outside the module (e.g., via AWX or a CI server).
- Packaging via RPMs is optional, but if used, install modules under `/usr/share/ansible` on the control machine.

## Functions and Methods
- Each function should be concise and meaningful.
- Follow the “Don’t Repeat Yourself” (DRY) principle.
- Use `snake_case` naming for functions—e.g., `my_function_name`.
- Function names should clearly describe their purpose.
- Always include a **docstring** for functions.
- Excessive nesting can be a sign that the nested logic should be refactored into a function.

## Python tips
- Wrap your main execution logic in a `main()` function.
- Guard execution with:
  ```python
  if __name__ == '__main__':
      main()
  ```
  This allows for better testability.

## Importing and using shared code
- Leverage existing shared code—like `AnsibleModule` and utility functions from `ansible.module_utils`.
- Import modules explicitly—**avoid wildcard imports (`*`)**.
- When importing custom packages, use a `try/except` block and handle failures via `fail_json()` in `main()`. Also, document dependencies in the module’s `DOCUMENTATION` block.

## Handling module failures
- Use `module.fail_json()` to signal failures, including a `failed` key and a descriptive `msg`.
- Avoid triggering tracebacks—Ansible can handle error formatting more gracefully.
- Never call `sys.exit()`—always use `fail_json()`.

## Handling exceptions (bugs) gracefully
- Validate inputs early and fail fast with clear error messages.
- Use defensive programming and simple design.
- Fail predictably—either mimic the underlying tool or use conventional patterns.
- Provide context in error messages (what the module was trying to do).
- Avoid catch-all `except:` unless the underlying API provides detailed error info.

## Creating correct and informative module output
- Output must be valid JSON only.
- Return data must be UTF-8 encoded. If not possible, encode (e.g., base64) or use `errors='replace'`.
- Use a **top-level dictionary (hash)** as the return structure.
- Nest complex data within this top-level dictionary; simple scalars or lists may also be included.
- Do not write to standard error—Ansible merges stdout and stderr and expects valid JSON.
- If there’s a need to capture stderr content, include it in the JSON on stdout (as seen in the `command` module).
- Avoid `print()` in modules—it breaks JSON output.
- Always return useful data—even when there’s no change.
- Ensure consistency in your return values across runs and modules.
- Support `diff` output when in diff mode, where relevant.
- Use only JSON-serializable types (strings, ints, dicts, lists).
- Do not return objects directly in `exit_json()`—convert necessary fields into a dictionary first.
- Return only relevant output—e.g., avoid dumping entire log files.

## Following Ansible conventions
- Use consistent naming and parameter choices across modules.
- Avoid using `message` or `syslog_facility` as option names—they’re reserved internally.
- Provide aliases where module option names differ from API names.
- Modules ending with `_facts` should return data under the `ansible_facts` key.
- `_info`/`_facts` modules should support `check_mode`. Typically done via `supports_check_mode=True`.
- Use module-specific environment variables to avoid naming collisions.
- Keep module options lean—large nested data structures can complicate validation.
- For complex operations, offer an expert module plus smaller atomic modules instead of a single bulky one.
- Favor declarative checking (e.g., `present`/`absent`) over imperative operations.
- Aim for idempotency—re-running the module shouldn't alter the system unless needed. If truly non-idempotent, document the behavior.
- Provide consistent return values, even if some keys aren’t applicable (`NA`/`None`).

## Module Security
- Avoid passing user input directly to shell commands.
- Always check return codes.
- Use `module.run_command`—never `subprocess`, `Popen`, or `os.system`.
- Avoid shell usage unless necessary; if used, set `use_unsafe_shell=True` and quote inputs with `pipes.quote()`.
- For URL fetching, use secure methods like `fetch_url` or `open_url`, not insecure libraries like `urllib2`.
- Mark sensitive values with `no_log=True` so they are redacted. If sensitive data appears in keys, use `sanitize_keys()` to strip them.
