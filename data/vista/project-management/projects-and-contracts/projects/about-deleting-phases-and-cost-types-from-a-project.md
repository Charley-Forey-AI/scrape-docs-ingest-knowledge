---
title: "About Deleting Phases and Cost Types from a Project | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projects-and-contracts/projects/about-deleting-phases-and-cost-types-from-a-project"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projects-and-contracts/projects/about-deleting-phases-and-cost-types-from-a-project"
---

# About Deleting Phases and Cost Types from a Project

You can delete phases and cost types from a project in PM
 Project Phases, as long as they meet the specified criteria.
You can delete a cost type from a phase as
 long as the cost type has a zero balance in every month. If you try to delete a cost
 type with balances not equal to zero, you will receive an error message informing you
 which detail does not meet the 'net to zero' requirements. You must make any necessary
 adjustments before you can delete the cost type. In addition, if the cost type exists in
 PMSL (Subcontract Detail) or PMMF (Material Detail), but it has not been assigned a SL,
 PO, MO, or Quote number, the subcontract and/or material detail record will be deleted
 along with the cost type.
You can also delete a phase and its cost
 types, as well as associated subcontract and/or material detail from a project at the
 same time if:

- no subcontract number is assigned to
 the subcontract detail for the phase/cost type (in PM SL Detail)

- no PO, MO, or Quote number is
 assigned to the material detail for the phase/cost type (in PM Material Detail)


- project has not been interfaced

- If the project has been interfaced,
 you can still delete a phase if:

- all cost types for the phase net to
 zero and you delete each cost type manually (in PM Cost Types Detail)

- no subcontract or material detail
 has been interfaced.
