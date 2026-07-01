# Execution Learning Loop

> Purpose: make every meaningful execution capable of improving the framework without allowing uncontrolled self-modification.

## Principle

The framework may learn from executions, but it must separate observation, recommendation and implementation.

```text
Observe -> Classify signal -> Record -> Promote candidate -> Ask approval -> Implement -> Validate -> Version
```

## When To Capture Learning

Capture a learning signal when an execution reveals at least one of these:

- repeated user correction on the same topic;
- wrong assumption that caused rework;
- validation failure caused by missing checklist/rule;
- production incident or user-visible regression;
- recurring domain pattern that should become reusable;
- token waste caused by reading too broadly or repeating a stale hypothesis;
- successful tactic that prevented rework, regression or security risk;
- capability gap discovered in a real consumer project.

Skip capture for purely conversational answers, trivial commands, or one-off facts with no reusable pattern.

## Signal Types

| Signal | Meaning | Typical Destination |
|--------|---------|---------------------|
| learning | What changed in understanding | `LEARNING.md` |
| pattern | Reusable successful approach | `PATTERNS.md` |
| anti-pattern | Repeated bad path or waste | `ANTI_PATTERNS.md` |
| recommendation | Proposed framework/product improvement | `RECOMMENDATIONS.md` |
| roadmap | Larger planned capability | `ROADMAP.md` |
| metric | Operational cost/retry/error evidence | `EXECUTION_METRICS.md` |

## Required Fields

Every captured learning should include:

- date;
- mission name;
- project/context;
- observed evidence;
- root cause or corrected assumption;
- reusable rule;
- promotion status: `observed`, `recommended`, `approved`, `implemented`, `rejected`.

## Promotion Rules

- One high-severity production lesson may create a recommendation immediately.
- Two similar corrections from a user require a learning entry.
- Three similar successful fixes require a candidate pattern.
- Five similar cases require checklist/rule proposal.
- A capability proven in one real consumer project becomes `Stable Candidate`, not automatically `Stable`.
- Capability promotion to `Stable` requires evidence, checklist coverage and at least one validated regression/evaluation set.

## Safety Rules

- Never store secrets, full prompts, private payloads, long code blocks or customer-sensitive data.
- Do not self-edit framework files unless the user explicitly approves implementation.
- Do not promote a local workaround into a universal rule without naming its scope.
- Prefer short evidence over exhaustive transcripts.
- Keep project-specific implementation details in the project; keep reusable behavior in the framework.

## End-Of-Mission Check

Before final response for executable work, ask:

1. Did the user correct us in a way that reveals a reusable rule?
2. Did validation fail because a checklist was missing?
3. Did we avoid a retry or regression through a framework guardrail?
4. Did this mission prove or weaken a capability assumption?
5. Is there a recommendation the user should approve before framework changes?

If yes, record the smallest useful signal.
