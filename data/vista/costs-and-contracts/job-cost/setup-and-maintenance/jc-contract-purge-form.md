---
title: "JC Contract Purge Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-contract-purge-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-contract-purge-form"
---

# JC Contract Purge Form

Use the JC Contract Purge form to purge contracts/jobs and contract/job history.
When you purge a contract, all revenue and cost detail stored for that contract (in the Job Cost tables) is deleted. The associated job is removed from JCJM (Job Master), and the contract and all item detail is removed from JCCM (JC Contracts). History records are added to JCHJ (Contract History by Job) and JCHC (JC History by Contract), respectively.Note: Contracts with associated SM Work Orders or SM Service Site records are not deleted.

## Purge Contract History

The Purge Contract History tab allows you to purge contract/job information stored in the JC History by Contract (JCHC) and JC History by Job (JCHJ) tables. This, in turn, allows you to reuse the contract and job numbers (if desired).

- When adding a new contract or job in JC or PM, validation will check to see if the number exists in the contract/job history files. If it does, a message displays informing you that the number was previously used and cannot be reused until the contract is purge from contract/job history. You will then need to purge the contract/job history here before you can reuse the number.

- Purging a contract/job and its contract/job history does not guarantee the contract/job number can be reused. You must also have purged all of the AP/PO/SL detail for that contract/job (in the AP, PO, and SL purge programs) before the contract/job number can be reused.

## Purging Secured Contracts

If you are using data level security and you purge a secured contract (via JC Contract Purge), the security entries are left intact. This allows for associated detail (invoices, payments, reports, and so on) existing elsewhere in the system to be accessed. You can maintain security for the contract/job in VA Data Security, and then purge the security entries in VA Data Security Purge once all existing detail for the contract/job has been purged from all other Viewpoint tables.
After purging Job Cost (JC) records, consider closing and purging its related subcontracts. See [Purge Subcontract Records](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-setupmaintenance/sl-maintenance/purge-subcontract-records).

[About Purging Contract/Jobs](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-purging-contractjobs)
[VA Data Security Access Form](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-data-security-access-form)
[VA Data Security Purge Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-data-security-purge-form)
