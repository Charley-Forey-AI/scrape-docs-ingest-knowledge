---
title: "About Updating Previous Billed Amounts on Future Bills | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-updating-previous-billed-amounts-on-future-bills"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-updating-previous-billed-amounts-on-future-bills"
---

# About Updating Previous Billed Amounts on
 Future Bills

When you change the values of a billing, whether interfaced, active, or in a closed month, you have the option to either manually update previous billed amounts or have the system update the values automatically (recommended).
Either way, such an update only affects the contract for which the update is currently being run.
To have the system automatically update previous billed amounts, as well as current contract and contract units, and ACO adds/deducts, you must set the Automatic Update of Prev Billed and ChgOrder Amounts on Future Bills option in JB Company Parameters to Y (checked). When this option is checked and changes are made to a billing, the system automatically updates the previous billed amounts, current contract, and contract units by including the value of the change for the current billing to the previous amounts of all subsequent (future) billings. For Progress Billings, previous change order additions and deductions will be updated when changes are made to approved change order items in the JB Progress Change Order form.
If you elect to update previous billed amounts manually, you must set the 'auto update' option in JB Company Parameters to N (unchecked). Then, each time you change a billing, you must go to the billing prior to the billing you changed and select the update option from the File menu. In JB Progress Billings, this will be the 'Update Prev Amts, ACO Adds/Deds on Future Bills' option, and in JB T&M Bill Edit, this will be the 'Update PrevAmts on Future Bills' option. As with the automatic update method, the system will update the previous billed amounts, current contract/contract units, and ACO additions/deductions (progress billings) by including the value of the billing you changed to the previous amount of all subsequent billings.
Note: If the previous billing is flagged for deletion (i.e. the Status is set to ‘Delete’), you must go to the next previous billing to perform the manual update of previous amounts. Bills marked for Delete will be skipped during the update process.
