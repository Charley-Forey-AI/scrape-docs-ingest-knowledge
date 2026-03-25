---
title: "About Setting Requisition Audit Options | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/about-setting-requisition-audit-options"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/about-setting-requisition-audit-options"
---

# About Setting Requisition Audit Options

The requisition audit options section in PO Company Parameters (Requisition Info tab) controls updates to the master audit file (HQMA) when you make additions, changes, or delete date from a selected PO form.
The audit options determine when new records of changes are added to the HQ Master Audit (HQMA) database table. For example, if you change a setting on the company parameters form, the system creates a new record of the change in the HQMA table.
You can view records in the HQMA table using the HQ Audit Detail report in the HQ module. See [About Viewing the Master Audit Log](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/view-the-audit-log) for more information about viewing audit records in the HQMA table.
 The following list discusses each audit option and the form(s) it affects:

- Requisitions – When you check this box, the system saves audit records for all additions, changes, and deletions to header and detail levels in PO Requisition Entry.

- Review – When you check this box, the system saves audit records for all additions, changes, and deletions to quote or requisition lines in PO Requisition Reviewer.

- Quote – When you check this box, the system saves audit records for all additions, changes, and deletions to header and detail levels in PO Quote Edit.

Note: To view the master audit file, run the HQ Audit Detail report.
