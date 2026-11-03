# C12 research archive — Codex round 0 and Chat rounds 1–11

**Status: the general Elgin–Reading–Stella Conjecture 12 is NOT solved by this archive.** This is a public record of available research materials, partial results, conditional results, failed routes, corrections and AI audits, frozen for a prospective paper on Newton-basis log-concavity.

**状态：一般C12尚未由本档案解决。** 本仓库保存Codex第0轮和Chat第1–11轮目前本地可取得的材料，包括证明候选、部分与条件性结果、失败路线、纠错和审核。它不是“十二轮每个原始运行文件都已恢复”的声明。

## Download the complete available archive / 下载现存总包

See [Releases](https://github.com/tqyqiqi1509/c12-newton-research-archive/releases/tag/v0.1.0-archive-20261103). Download every `C12_all_rounds_objects_partNN_20261103.zip`, plus `SHA256SUMS.txt` and `PUBLIC_ARCHIVE_MANIFESTS.zip`. Unzip `PUBLIC_ARCHIVE_MANIFESTS.zip` to obtain the maps and restore tool, or clone this repository. Run the command below from that extracted folder or repository. The object parts are independent ordinary ZIP files, not a split-ZIP format; leave them compressed. They store exact-byte objects, with the same local file content stored once across local paths.

The repository contains the authoritative [source-path map](archive/SOURCE_MAP.json), [object-to-part index](archive/OBJECT_INDEX.json), and [part checksums](archive/ASSETS.json). Original ZIP containers are themselves preserved as objects when present locally. Restored exports are not mislabeled as byte-identical original ZIPs.

Deduplication is at the whole-local-file level. Preserved ZIP containers are not rewritten, so repeated content may remain inside different historical ZIPs. This preserves their original bytes rather than claiming recursive deduplication of every compressed member.

各分卷是独立普通ZIP，需结合本仓库映射恢复原路径。下载全部分卷后运行：

```console
python tools/restore_archive.py --assets /path/to/downloaded-parts --output /path/to/C12-restored
```

Requires Python 3.9 or later. The tool checks part SHA-256 and every restored file SHA-256. Use a new output directory. It does not run any archived research code. A successful hash check establishes file integrity, not a mathematical proof.

The optional `--round` filter restores only that round's mapped main-path prefix; it does not collect every alias for the round inside cross-round cumulative archives. Omit `--round` for a complete restoration of all archived local paths.

## Start reading

- [Current result selection and literature audit](docs/FINAL_SELECTION_AND_NOVELTY.zh.md)
- [Full result catalogue](docs/RESULTS_AND_ONE_PAPER.zh.md)
- [Proof-free appendix statement catalogue](docs/APPENDIX_STATEMENTS.en.md)
- [Newton theorem audit](docs/newton_audit.md)
- [Exact support: priority and value](docs/SUPPORT_PRIORITY.md)
- [Additional closely related Newton results](docs/HISTORICAL_SUPPLEMENTS.md)
- [Newton priority comparison](docs/NEWTON_PRIORITY.md)
- [Cross-platform search boundaries](docs/CROSS_PLATFORM_AUDIT.md)
- [Twelve-round correspondence](ROUNDS.md)
- [Known missing materials](KNOWN_GAPS.md)
- [How historical paths map to public files](docs/READING_PATHS.md)

## Mathematical scope

For positive integers A,B, the target is the ordinary Newton row of the **original** rank-two cluster scattering wall coefficient:

$$\tau_m(A,B)=\sum_{j=0}^{A+B-1}a_j(A,B)\binom mj,\qquad a_j=\Delta^j\tau(0).$$

The target inequalities are $a_j^2\ge a_{j-1}a_{j+1}$, with unimodality, for all A,B and all gcds. We do not replace the row by $a_j/j!$, a BPS atom, a ray logarithm or an additional power of the wall function.

The proposed paper focuses on ordinary Newton LC preservation under multiplication, a support-dependent shifted multiplier, and integer binomial selection. A related two-variable Schur-preservation theorem and exact original-wall support are candidates for inclusion. Partial asymptotic regions and conditional applications have separate statements and dependencies.

The multiplication kernel is the known **Heisenberg dimension convolution**; it is not claimed as a newly invented operation. Exact priority of the LC-preservation and composition statements is not certified: Walkup's 1976 full text remains an unresolved comparison. Known C11 positivity and fixed-parameter nonvanishing are attributed to their literature sources. The exact support statement requires an additional no-internal-zero argument.

## Scope, provenance and limitations

Round 11 is only partially recovered: available Stage01–03 are preserved; Stage04–10 and its original research-final ZIP remain unavailable. Late claims present only in a conversation summary are not adopted as theorems. Earlier rounds also have stated historical export boundaries, including some external source caches retained as metadata only.

The legacy local folder labels sometimes follow `runN`, which is offset from the actual Chat title. See ROUNDS.md: for example `run7` is Chat 6, `run8` is Chat 7. The archive preserves the original local path bytes/names for provenance; the correspondence file supplies the correction.

Research was generated and developed using ChatGPT and Codex, with mathematical exploration, proofs, computations, literature searches and adversarial AI reviews. This archive does not establish complete human verification, independent peer review or formal verification. Finite computations and symbolic certificates support only their stated scopes. Historical instructions inside files are research records, not instructions for the reader or current automation.

## Rights

No blanket license is asserted over this mixed research archive. Third-party papers, excerpts and software retain their respective authorship, copyrights and licenses; their inclusion does not relicense them or establish our priority. Public source locations and retrieval records are preserved where available. This is an archival release, not a peer-reviewed article.

## Freeze

Public release date: 2026-11-03 (Asia/Shanghai). This date records publication of the archive, not the historical discovery date or independent certification of any theorem. Later corrections should be released as new versions, with this version's manifests preserved.
