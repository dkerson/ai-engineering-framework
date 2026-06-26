# Knowledge Metadata Template

| Field | Type | Required |
|-------|------|----------|
| id | uuid | yes |
| title | string | yes |
| type | faq \| article \| manual \| pdf \| doc | yes |
| version | semver | yes |
| permissions | string[] | yes |
| tags | string[] | no |
| source_uri | string | no |
| updated_at | datetime | yes |
