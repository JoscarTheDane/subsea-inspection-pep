# Subsea Inspection PEP

Project Execution Plan (PEP) doctrine for offshore subsea / diving
structural inspection tenders — the agent skill that writes PEPs which
answer the tender's operational questions instead of filling a generic
template.

**The core rule:** a tender PEP must demonstrate you understood *this*
job — depth and workscope, access, LOTO, vessels, emergency response,
personnel, mobilisation, communications, hazmat, and the right NDT
methodology for the conditions. Where the SOW doesn't contain an answer,
the doctrine marks it `[TBC]` for contractor-specific data — never
invents one.

Built from real API RP 2SIM Level 2/3 survey campaigns (Gulf of Guinea
style: Escravos / Forcados / Warri delta, 2–60 m water depth) and
Atlantic Marine / Shell example PEPs.

## Repository layout

```
README.md                        this file
LICENSE                          MIT + The Commons Clause
subsea-inspection-pep/
  SKILL.md                       the skill — full doctrine
  references/
    pep-document-structure.md    document structure & section formats
  scripts/
    pep_docx_helpers.py          python-docx helpers for the .docx output
```

## What the skill covers

- **Required data points** (11): depth & workscope, location details,
  facilities/subject, LOTO, vessels & equipment, emergency response,
  personnel, mobilisation, communications, hazmat/environment, NDT
  methodology.
- **NDT doctrine — ACFM over MPI** when the SOW admits poor/zero
  visibility, currents >1 knot, or visibility-dependent MPI. ACFM is
  zero-visibility capable, current-immune, gives quantitative crack
  sizing in one scan, works through 5 mm of coating, needs no particle
  or UV. MPI kept as contingency where conditions permit.
- **Document format**: restricted/ECCN header, revision history, ToC,
  abbreviations table, Calibri, blue headings, `#003366` table headers
  with white text. Output via python-docx.
- **Reference integration**: IMCA D-series references are cross-checked
  against the current register (see the companion `imca-recall` project);
  non-IMCA refs (DMAC, IOGP, IMO, API, ISO) are flagged as external.
- **Interface-first delivery rule**: content is produced in chat as
  paste-ready text for the operator to review — the agent never writes
  into the live .docx unless explicitly asked.

## Usage

### 1. Install as an agent skill

Copy the skill folder into your agent's skill tree (e.g. Hermes):

```sh
cp -r subsea-inspection-pep ~/.hermes/skills/
```

The skill is self-contained markdown + one helper script. No keys, no
paths, no network dependencies.

### 2. Invoke

Ask for a PEP:

> "Write the PEP sections for this SOW" (attach or paste the SOW)

The skill drives the extraction and produces paste-ready section text in
chat. To generate the formatted .docx, use `scripts/pep_docx_helpers.py`
(requires `python-docx`):

```sh
pip install python-docx
```

### 3. PEP + manifest companion

For the same campaign, the equipment load-out manifest skill lives in
its own repo: [`equipment-manifest-generator`](https://github.com/JoscarTheDane/equipment-manifest-generator)
(email-in/CSV-out pipeline). The two skills share the same SOW but
deliver different artifacts: the PEP answers *how we run the job*; the
manifest answers *what we ship*.

## Sibling projects

| Project | What it does |
|---|---|
| [equipment-manifest-generator](https://github.com/JoscarTheDane/equipment-manifest-generator) | equipment load-out / tick-off CSV pipeline |
| [hse-doc-generator](https://github.com/JoscarTheDane/hse-doc-generator) | HIRA risk-assessment Excel pipeline |
| [imca-recall](https://github.com/JoscarTheDane/imca-recall) | local RAG over the IMCA guidance register |

## License

MIT + [The Commons Clause](https://commonsclause.com/) — see `LICENSE`.
