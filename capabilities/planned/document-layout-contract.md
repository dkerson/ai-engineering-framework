# Document Layout Contract

> Status: Planned
> Category: Documentation, Product Design, Knowledge Hub
> Version: 0.1.0

## Purpose

Prevent generated HTML documents from depending on fragile renderer heuristics.

When a mission generates visual HTML, the output should declare an explicit layout contract before it is stored or rendered.

## Contract Fields

Minimum fields:

- `layoutSlug`
- `layoutVersion`
- `documentType`
- `renderMode`
- `sanitizationProfile`
- `allowsScripts`
- `templateSource`
- `validationStatus`

## Recommended Flow

1. Select the document type.
2. Resolve the layout by project, area, folder, and use case.
3. Generate HTML against the selected template.
4. Inject machine-readable layout metadata.
5. Validate structure, script policy, logo sizing, and first-screen readability.
6. Store raw content, normalized content, hash, and layout version.
7. Render from the stored contract, not from CSS/class-name guessing.

## Evidence

Umbra KB Irisys/Biblioteca exposed repeated failures where generated HTML:

- rendered Markdown instead of the intended HTML;
- lost template styling;
- required frontend fallback CSS;
- needed special handling for presentation documents with scripts;
- flickered because iframe HTML was regenerated too often.

## Promotion Criteria

Promote to Ready when two or more projects reuse the contract and at least one automated visual validation exists.

## Related Future Artifacts

- `skills/document-layout-contract/SKILL.md`
- `checklists/document-layout-contract/html-validation.md`
- `templates/document-layout-contract/layout-registry.md`
- `rules/document-layout-contract/render-from-contract.md`
