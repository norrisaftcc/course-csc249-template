# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a development template for **CSC 249: Data Structures and Algorithms**, an 8-module college course using dual-language instruction (C++ and Python). The repository serves as both a specification document for instructors and a template for course content creation.

## Development Workflow

This project uses GitHub Issues and Pull Requests to frame all work. Use `gh` CLI for GitHub operations (authenticated via `gh auth`). When creating content:
1. Create an issue describing the work
2. Create a branch for the work
3. Submit a PR linking to the issue
4. Branch naming: `[module]-[assignment]-[yourname]`

## Architecture Overview

### Two Development Perspectives

- **`dev/agent_a/`**: Course specifications and workflow documentation (outlines, assignment specs, GitHub workflow guides)
- **`dev/agent_b/`**: Actual course content organized by module (tutorials, labs, code examples in C++ and Python)

### Course Development Tracking System (CDTS)

The `_tracking/` folder defines a manifest-based tracking system:
- Courses use 8 standardized modules (per curriculum requirement)
- Each module has deliverables with status: `planned`, `draft`, `review`, `complete`
- Progress is tracked via `course-manifest.yaml` at repository root
- Deliverable types: `tutorial`, `lab`, `homework`, `project`, `reading`, `rubric`, `slides`, `video`, `quiz`, `reference`

When creating content, update the manifest to reflect progress.

### Module Organization (agent_b)

Modules follow naming pattern `mX-topic`:
- `m1-objects`: OOP basics
- `m3-sorting`: Selection, insertion, merge sort
- `m4-lists`: Singly/doubly linked lists
- `m5-hashing`: Hash tables, cryptographic applications
- `m6-trees`: BSTs, balanced trees, BSP trees
- `m7-graphs`: Graph algorithms
- `m8-projects`: Final capstone

Each module may contain: tutorials (`*t*`), labs (`*lab*`), homework (`*hw*`), with both `_py` (Python) and `_cpp` suffix variants.

## Course Philosophy

**"Bloom's Taxonomy Starts with Create"** — Students build first, then understand why it works.

Key pedagogical elements:
- Dual-language: All concepts implemented in both C++ and Python
- Mandatory AI collaboration with documentation requirements
- AlgoCratic theming: Bureaucratic departments handle each data structure topic (e.g., "Department of Task Processing" for stacks/queues)
- GitHub-based submission via pull requests

## Content Standards

When creating course materials:
- Provide both C++ and Python implementations where applicable
- Reference OER resources (Runestone Academy, OpenDSA, VisuAlgo) over proprietary textbooks
- Include visualization suggestions using David Galles' USFCA tools or VisuAlgo
- Frame assignments within the AlgoCratic theme where appropriate

## Directory Structure Reference

```
course-cscXXX-template/
├── course-manifest.yaml      # Progress tracking (required at root)
├── CLAUDE.md                 # This file
├── module-01/ through module-08/
│   ├── tutorials/
│   ├── labs/
│   ├── homework/
│   ├── readings/
│   └── projects/
├── resources/                # Shared course resources
└── docs/                     # Course development documentation
```
