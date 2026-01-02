# CSC 249 Strategic Development Analysis

## Executive Summary

The existing content is richer than it first appears: agent_a has high-quality assignment specifications, and agent_b has working code implementations (particularly strong in modules 3-6). The key challenge is pedagogical consolidation without losing the "build first" philosophy.

---

## 1. Consolidation Strategy: 16 Modules to 8 Modules

### Recommended Mapping

| New Module | Original Modules | Weeks | Rationale |
|------------|------------------|-------|-----------|
| **M01** | M1 (Objects) + M2 (AI Collab) | 1-2 | Foundation: OOP basics + AI workflow established together |
| **M02** | M3 (Analysis) + M4 (Recursion) | 3-4 | Analytical thinking: Big O and recursion are complementary |
| **M03** | M5 (Arrays/Sorting) | 5-6 | Arrays and sorting are substantial enough standalone |
| **M04** | M6 (Stacks/Queues) + M7 (Linked Lists) | 7-8 | Linear structures: Natural grouping of sequential ADTs |
| **M05** | M8 (Hashing) | 9-10 | Hashing deserves dedicated time; complexity often underestimated |
| **M06** | M9 (Trees/BST) + M10 (Heaps) + M11 (Balanced) | 11-12 | Hierarchical structures: Tree family consolidated |
| **M07** | M12 (Graphs Intro) + M13 (Graph Algorithms) | 13-14 | Network structures: Graphs require both representation and algorithms |
| **M08** | M14-M16 (Final Project) | 15-16 | Integration: Capstone as originally designed |

### Why This Mapping Works

1. **Preserves pedagogical coherence**: Each new module has a clear thematic identity
2. **Maintains "build first" philosophy**: No module becomes purely theoretical
3. **Balances workload**: Heavier topics (Trees, Graphs) get 2-week modules
4. **Keeps AI collaboration prominent**: Integrated into M01 rather than lost as a separate module
5. **Preserves the AlgoCratic theme**: Department assignments still map cleanly

### Key Consolidation Decisions

**M01 Merge (Objects + AI Collaboration)**:
- Original M2's "Field Guide" assignment becomes a scaffolded intro activity in week 1
- Code translation exercise moves to M03 (Arrays) where students have more code to translate
- Result: Students learn AI collaboration *in context* rather than as isolated skill

**M04 Merge (Stacks/Queues + Linked Lists)**:
- All three are linear, node-based or sequential structures
- Linked list implementation naturally leads into how stacks/queues can be implemented
- Existing `M6_StacksQueues_Assignment.md` becomes Part A; Linked Lists becomes Part B

**M06 Merge (Trees consolidated)**:
- Balanced trees are conceptual only per original design (visualization focus)
- Heaps can be taught as "trees with different rules"
- This is the riskiest merge pedagogically; may need careful scaffolding

---

## 2. Starting Point Analysis

### Option Comparison

| Option | Pros | Cons | Risk Level |
|--------|------|------|------------|
| **Start with M03-M06** (most content) | Hit the ground running; code exists | Patterns not established; may need rework | Medium |
| **Start from M01** (establish patterns) | Clean foundation; templates reusable | Slower start; existing code sits unused | Low |
| **Start with infrastructure** (manifest, templates) | Enables tracking from day one | No actual content delivered; feels slow | Low |

### Recommendation: Hybrid Approach

**Phase 1**: Create the course-manifest.yaml and module directory structure
- This takes minimal time and enables CDTS tracking immediately
- Creates the "shape" of the final course
- All subsequent work slots into correct locations

**Phase 2**: Develop M01 as the template module
- Establishes patterns for:
  - Assignment specification format
  - Dual-language code organization
  - AlgoCratic theming approach
  - Rubric structure
  - PR submission workflow
- Every subsequent module follows this template

**Phase 3**: Port existing content into M03-M05
- agent_b's sorting, linked lists, and hashing code fits well
- agent_a's M6_StacksQueues_Assignment.md maps to new M04

### Why Not Start with Existing Content First?

The existing content uses **inconsistent naming conventions** (m3-sorting, m4-lists, m5-hashing, m6-trees in agent_b vs. M1, M2, M6 in agent_a). Starting with infrastructure establishes the authoritative naming before content migration prevents confusion.

---

## 3. Content Reuse Assessment

### agent_a Content (Specifications)

| File | Reusability | Adaptation Needed |
|------|-------------|-------------------|
| `CSC249_Course_Outline.md` | **Reference only** | Module numbers change; use as design document |
| `M2_Assignment_Spec.md` | **70% reusable** | Split: Field Guide to M01, Translation to M03 |
| `M6_StacksQueues_Assignment.md` | **90% reusable** | Renumber to M04 Part A; excellent template |
| `GitHub_Workflow_Guide.md` | **100% reusable** | Move to resources/ folder |

### agent_b Content (Code Implementations)

| Directory | Reusability | Adaptation Needed |
|-----------|-------------|-------------------|
| `m3-sorting/` | **80% reusable** | Clean up IDE files; add Python versions where missing |
| `m4-lists/` | **85% reusable** | Strong dual-language; needs tutorial docs |
| `m5-hashing/` | **75% reusable** | Password hashing examples excellent; needs main tutorial |
| `m6-trees/` | **70% reusable** | BSP discussion is bonus content; core BST usable |
| `m7-graphs/` | **40% reusable** | Only markdown notes; code needed |
| `m1-objects/`, `m8-projects/` | **Placeholder only** | READMEs exist; content TBD |
| `algocratic/` | **100% reusable** | Theme documents ready to use |

**Estimate: 60% of code content can transfer directly; 40% needs documentation wrapping.**

---

## 4. Risk Assessment

### High-Risk Items

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| **M06 (Trees) consolidation too dense** | Students overwhelmed | Medium-High | Build in "conceptual checkpoints"; make heaps optional if needed |
| **Dual-language maintenance burden** | Content drift between C++/Python | High | Establish single-source pattern; generate one from other where possible |
| **AI collaboration documentation overhead** | Students game the system | Medium | Integrate into natural workflow; make it part of PR template |

### Medium-Risk Items

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| **8-module pacing too fast for community college** | Students struggle | Medium | Build in flexibility in M04 and M06 |
| **Existing code lacks error handling** | Students copy broken patterns | Medium | Review and harden all starter code |
| **AlgoCratic theme may not land** | Students confused by fictional framing | Low-Medium | Make theme clearly optional; provide "straight" versions |

### Critical Dependency Risk

**The biggest risk is scope creep during content creation.** The existing M6_StacksQueues_Assignment.md is 473 lines with extensive scaffolding. If every module receives this treatment, development time explodes.

**Mitigation**: Establish "assignment spec template" that is deliberately leaner; rich scaffolding is optional extension.

---

## 5. Recommended First Actions

### Action 1: Create course-manifest.yaml and Directory Structure

**Deliverable**: Working manifest at repo root + empty module-01 through module-08 directories

**Why first**:
- Enables CDTS tracking from day one
- Forces commitment to 8-module structure
- Takes less than 1 hour
- All subsequent work has a home

### Action 2: Develop M01 as Reference Implementation

**Deliverable**: Complete M01 (Objects + AI Collaboration) with all deliverables

**Contents**:
- `module-01/README.md`: Module overview
- `module-01/tutorials/`: CitizenRecord class tutorial (C++ and Python)
- `module-01/labs/`: "Build your first class" guided lab
- `module-01/homework/`: AI Field Guide assignment (adapted from M2)
- Assignment specification document
- Grading rubric

**Why second**:
- Establishes all patterns before scaling
- Tests the consolidation approach (M1+M2 merge)
- Creates reusable templates for other modules
- Validates dual-language workflow

### Action 3: Port Strongest Existing Content to M03 (Sorting)

**Deliverable**: Complete M03 using existing agent_b code

**Why third**:
- agent_b/m3-sorting has developed code
- Tests content migration workflow
- Sorting is self-contained (no dependencies on other modules)
- Validates dual-language pattern with real code

---

## 6. Where This Leaves Us

### Current State Summary

| Module | Code Ready | Spec Ready | Effort to Complete |
|--------|------------|------------|-------------------|
| M01 | None | Partial (M2 spec) | Medium |
| M02 | None | None | High |
| M03 | Yes | None | Low-Medium |
| M04 | Yes | Yes (M6 spec) | Low |
| M05 | Yes (Python) | None | Medium |
| M06 | Partial (no heaps) | None | Medium-High |
| M07 | None | None | High |
| M08 | None | None | High |

### Recommended Starting Point

**Start with M04 (Linear Structures)** as proof-of-concept because:
1. Has both code (agent_b/m4-lists) AND spec (agent_a/M6_StacksQueues_Assignment.md)
2. Can demonstrate the full pattern: spec + code + rubric
3. Validates the migration and consolidation workflow
4. Low risk, high confidence of completion

Then use M04 as the template for completing other modules.

---

## Summary Decision Matrix

| Question | Recommendation | Confidence |
|----------|----------------|------------|
| **Module consolidation** | Use the 8-module mapping above | High |
| **Starting point** | M04 as proof-of-concept, then infrastructure | High |
| **Content reuse** | 60-85% depending on module | Medium |
| **Biggest risk** | M06 consolidation and scope creep | High |
| **First concrete action** | Complete M04 end-to-end as template | High |

---

*Document generated for CSC 249 course development planning.*
*Last updated: 2026-01-01*
