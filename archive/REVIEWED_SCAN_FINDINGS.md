# Review of the 13 AWS-pattern findings

Date: 2026-11-03, Asia/Shanghai. This is a static, local review of the exact payloads named in `PUBLICATION_SCAN.json`. No matching marker value or complete signed URL is reproduced in this report. No URL or marker was used to make any network or authentication request.

## Decision

**`can_publish_original_bytes: true` — 13 findings checked, 0 unresolved.**

All 13 matches are access-key-ID-shaped strings embedded entirely in the `X-Amz-Credential` parameter of expired, previously recorded S3 signed download URLs. They are not secret access keys. Each finding has exactly one marker occurrence, and all raw occurrences are accounted for by the URL parameter. No marker appears as a separate credential or configuration value. No secret-access-key assignment was found in these payloads.

The original bytes can be retained; these 13 pattern matches do not require redaction, deletion or rewriting of the research archives. The original scan record should remain intact, with this review attached as its adjudication rather than removing the matches from history.

## Evidence groups

| Findings | Source context | Host | Signing date | Expiry UTC |
|---|---|---|---|---|
| 10 | Publisher chapter: *Unimodality, Log-concavity, Real-rootedness and Beyond*; research search outputs and source-export metadata | `s3-euw1-ap-pe-df-pch-content-store-p.s3.eu-west-1.amazonaws.com` | 2025-11-13 | 2025-11-15 22:20:04 |
| 2 | Library source: *On the Combinatorics of the Free Lie Algebra With Multiple Brackets* | `s3.amazonaws.com` / Ex Libris source path | 2026-08-11 | 2026-08-12 06:22:49 |
| 1 | Library dissertation source: *Exceptional collections, clusters, t-structures, and the relationship between them* | `s3.amazonaws.com` / Ex Libris source path | 2026-05-24 | 2026-05-25 05:31:00 |

All expiry times precede even the start of 2026-11-03 in Asia/Shanghai. The classification is supported both by URL query parsing and by the neighboring literature titles/resource paths. This does not claim that the underlying S3 buckets are publicly readable without a signature; the pertinent fact is that these are historical literature-download records, their signed access has expired, and their visible access-key identifiers are not secret signing keys.

## Per-payload binding

`REVIEWED_SCAN_FINDINGS.json` records, for every one of the 13 findings:

- the original local or nested-ZIP member path;
- SHA-256 of the payload actually read;
- marker counts and whether every occurrence is confined to the signed URL credential parameter;
- host, signing date and computed expiry time, without credential values or signatures;
- absence of secret-access-key assignment and private-configuration evidence in the reviewed payload;
- the classification `expired_public_source_presigned_url_false_positive`.

This independent review read only the flagged exact payloads; it did not rerun the main 299,615-payload scan. The result adjudicates these 13 findings and does not assert exhaustive detection of every possible secret or certify mathematical correctness.
