# Ansible and Python 3

Ansible maintains a single code base that runs on both Python 2 and Python 3 because the goal is to manage a wide variety of machines. Contributors to Ansible should follow the advice in this guide to ensure their code runs on the same supported versions.

Three types of Ansible code must be considered:

1. **Controller-side code** – runs on the machine where you invoke `ansible`.
2. **Modules** – code that gets transmitted to and executed on managed nodes.
3. **Shared `module_utils` code** – common utilities used both by modules and, sometimes, controller code.

> These three code types use different strategies for handling strings, especially regarding Python 2 vs Python 3 compatibility (see **Understanding strings in Python 2 and Python 3**).

---

## Minimum version of Python 3.x and Python 2.x

- **Controller-side (control node)** supports Python 3.5+ and Python 2.7+.
- **Module-side (managed nodes)** supports Python 3.5+ and Python 2.6+.

 Python 3.5 was chosen as the minimum version because it was the earliest Python 3 version adopted as the default in an LTS Linux distribution (Ubuntu 16.04).  
 Modules may drop support for Python 2.6 if they depend on libraries that require higher versions—but avoid forcing a higher version without reason.

---

## Developing Ansible code that supports both Python 2 and Python 3

A great resource is Lennart Regebro’s book *Porting to Python 3*, which describes various strategies. Ansible uses a **single code base** approach to support both versions.

### Understanding strings in Python 2 vs Python 3

- **Python 2**: Strings (`str`) are byte arrays; `unicode` is for text. Mixing different encodings can lead to silent bugs unless non-ASCII is used.
- **Python 3**: `bytes` and `str` (text) are distinct and cannot be mixed implicitly—explicit conversion is needed to avoid errors.

Make sure your code defines a clear string handling strategy—especially if you're working on modules or `module_utils`, which have different expectations.

---

### Control node string strategy: the Unicode Sandwich

At the boundaries between your code and the external world (e.g., file reads, network I/O, environment variables), handle bytes explicitly:

- **Convert incoming bytes → text** before internal processing.
- **Convert text → bytes** when sending data outward.

This "sandwich" approach keeps text in the core of the logic while managing bytes at the edges.

---

## Compatibility tips, tricks, and idioms

- **Use forward-compatibility boilerplate**:
  ```python
  # Make coding more python3-ish
  from __future__ import (absolute_import, division, print_function)
  __metaclass__ = type
  ```
  This ensures new-style classes and consistent behavior across Python versions.

- **Prefix byte-oriented variables with `b_`** to clarify intent.

- **Import Ansible’s bundled `six` library** (no external dependency):
  ```python
  from ansible.module_utils import six
  ```

- **Use the modern exception syntax**:
  ```python
  try:
      ...
  except ValueError as e:
      module.fail_json(msg="Error: %s" % e)
  ```
  Avoid the outdated syntax used in older Python–only code.

- **Update octal literals** from the old `0755` to the Python 3-compatible `0o755`.

---

## String formatting for control node code

- Use `str.format()` with numbered placeholders for compatibility with Python 2.6:
  ```python
  "Hello {0}, welcome to {1}".format(user, location)
  ```

- Use percent-formatting for byte strings (since `format()` doesn't work on bytes). Example:
  ```python
  b"User %s logged in" % username_bytes
  ```

---

### Summary

Ansible supports both Python 2 and Python 3 across varying code types with differing requirements for string handling. Follow the guidelines above—Unicode Sandwich, compatibility boilerplate, clear typing, and cross-version formatting—to write maintainable, dual-compatible code.
