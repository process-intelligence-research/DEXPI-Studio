# Changelog

## 0.1.0

First public release of DEXPI Studio, a desktop application for DEXPI P&IDs built on
[pyDEXPI](https://github.com/process-intelligence-research/pyDEXPI) 2.1, free software under the
GNU Affero General Public License v3.

### Features

- Open DEXPI 2.0 and 2.0.1 XML and JSON files, and Proteus XML (DEXPI 1.3)
- Render the P&ID with pyDEXPI; navigate with a touchpad (pinch to zoom, two fingers to move,
  double tap to fit) or a mouse
- Collapsible, searchable model tree, a properties panel, and selection shared between tree and
  diagram
- Validate with pyDEXPI's rules; results in the Logs panel
- Summary of equipment, piping and instruments with their tags
- Compare two models with pyDEXPI's diff
- Exports, with pyDEXPI's options:
  - GraphML, Neo4j CSV and LLM context at any graph level, including a process model's flow
  - Equipment, line, instrument, piping component and valve tables as Excel, CSV or JSON, in
    English, German, Dutch or Chinese
  - SVG, PNG and PDF images
  - DEXPI 2.0.1 XML and JSON
  - A stable text projection for reviewing model changes in Git
- Optional ChatP&ID assistant, which sends the context you select to the AI provider you
  configure
- Ready-to-run builds for Windows, macOS (Apple silicon) and Linux

### Architecture

- Clean core/GUI separation
- Core layer does not import PySide6
- All functionality delegated to pyDEXPI — no duplication
