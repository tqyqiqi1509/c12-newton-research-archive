# Available C12 research materials, rounds 0–11

Public archival freeze: 2026-11-03. General C12 remains open. This release records the available local research files, not a claim that every historical run file has been recovered.

- Local file paths preserved: **36,843**.
- Distinct exact-byte local objects: **8,399**.
- Logical local bytes before deduplication: **7,677,682,709**.
- Distinct local object bytes: **5,252,090,518**.
- Material ZIP parts: **4**, each below 2 GiB.
- Duplicate files were identified by SHA-256 and verified by byte comparison.
- Existing original ZIP files are preserved as exact objects. All local originals remain unchanged.

Download every `C12_all_rounds_objects_partNN_20261103.zip`. Also download `PUBLIC_ARCHIVE_MANIFESTS.zip` and `SHA256SUMS.txt`. Unzip the manifests package and run `python tools/restore_archive.py --assets <download-folder> --output <new-output-folder>`. The ZIP parts can remain compressed; the restore tool reads them directly and verifies the files.

Each part is a standalone ZIP object container. Parts are not independently readable round folders; source paths and round provenance are restored from the maps. The GitHub auto-generated “Source code” ZIP contains the repository documentation/maps/tools only; it does not include the large release assets.

The release preserves the legacy local path names. `ROUNDS.md` corrects the difference between run numbers and Chat titles. Round11 includes available Stage01–03 and recovery audits; late Stage04–10 and the original research-final ZIP remain missing. Historical external-cache and transcript limitations are listed in `KNOWN_GAPS.md`.

The research includes Newton LC closure proofs, support results, partial asymptotic results, conditional interfaces, failed routes, corrections and literature audits. AI review, finite computation and hash verification do not constitute formal or human certification. Priority of the Newton closure statements remains unconfirmed; the known Heisenberg kernel and earlier positivity/nonvanishing results are explicitly attributed in the documentation.

本次公开的是现存材料归档，包含成功与失败路线、纠错和审核。一般C12仍未解决；第11轮后半程原件缺失如实保留。数学证明状态、文件完整性与优先权状态分别说明。
