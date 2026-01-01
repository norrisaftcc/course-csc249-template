# CSC 249 Course Outline

This folder contains the course development planning documents.

## Documents

### [content-mapping.md](content-mapping.md)
Maps existing content from `dev/agent_a/` (specifications) and `dev/agent_b/` (code) to the 8-module CDTS structure. Includes:
- 16-to-8 module consolidation map
- Detailed inventory of what exists per module
- Gap analysis with priority levels
- File inventory appendix

### [strategic-analysis.md](strategic-analysis.md)
Strategic guidance on the development approach:
- Consolidation rationale and tradeoffs
- Starting point recommendations
- Content reuse assessment
- Risk analysis
- Recommended first actions

## Key Findings

| Module | Code Ready | Spec Ready | Status |
|--------|------------|------------|--------|
| M01 | None | Partial | Needs work |
| M02 | None | None | Needs work |
| M03 | Yes | None | Needs spec |
| **M04** | **Yes** | **Yes** | **Near complete** |
| M05 | Yes (Python) | None | Needs spec |
| M06 | Partial | None | Needs heaps + spec |
| M07 | None | None | Critical gap |
| M08 | None | None | Needs work |

## Recommended Starting Point

**M04 (Linear Structures)** has both code and specs ready - use it as the template for other modules.

## Source Materials

- `dev/agent_a/` - Course specifications (16-module outline, assignment specs)
- `dev/agent_b/` - Code implementations (sorting, lists, hashing, trees)
- `_tracking/` - CDTS requirements and manifest template
