# Prolog Project Standards

Prolog is documented as a project and catalog management application with CLI, TUI, and GUI modes, file/folder classification and hashing, duplicate detection, a JSON inventory, idea generation, and editor integration. These standards supplement the README and the actual package implementation.

## Catalog and inventory contract

Document the inventory schema, stable identifiers, classification rules, hashing algorithm, duplicate-detection semantics, and treatment of inaccessible or changing files. Distinguish exact content duplicates from name/path similarity. Explain where inventory data is stored and how it is backed up, exported, or rebuilt.

## Interface parity

Document CLI commands and arguments, TUI navigation and keyboard controls, and GUI workflows separately. Where the interfaces share a workflow, keep the underlying result consistent; document any intentional differences. Do not claim a mode is available unless it is implemented and tested.

## Filesystem safety

Explain which paths are scanned, whether traversal is recursive, how symlinks and permissions are handled, and whether files are modified. Editor launching must not silently rewrite or delete cataloged files. Hashing and scanning should be described as read operations unless the implementation proves otherwise.

## Installation and dependencies

Document the supported Python versions, dependencies, entry points, and installation process from project metadata. Distinguish editable development installation from a user-facing release installation. Do not claim a platform is supported solely because Python runs there.

## Testing and versioning

Test path edge cases, permission errors, large inventories, hash consistency, duplicate detection, malformed JSON, and persistence recovery. Follow the repository's actual version source. Documentation-only updates do not require a version bump unless project rules explicitly require it.
