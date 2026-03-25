---
title: "About Updating Previous Billed Amounts on Future Bills | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/about-updating-previous-billed-amounts-on-future-bills"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/about-updating-previous-billed-amounts-on-future-bills"
---

# About Updating Previous Billed Amounts on
 Future Bills

You can update the previous billed amounts for future bills when changing values on a T&M billing.
When you change the values of a billing, whether interfaced, active, or in a closed month, you have the option to either manually update previous billed amounts or have the system update the values automatically (recommended).
To have the system automatically update previous
 billed amounts, current contract and contract units, and ACO adds/deducts, select the
 Automatic Update
 of Prev Billed and ChgOrder Amounts on Future Bills checkbox in JB Company
 Parameters. When this box is checked and changes are made to a billing, the system
 automatically updates the previous billed amounts, current contract, and contract units by
 including the value of the change for the current billing to the previous amounts of all
 subsequent (future) billings.
If you elect to manually update these values, do not select the checkbox.
 Each time a billing changes, go to the previous billing and select File > Update Prev Amts, ACO Adds/Deds on Future Bills. The system updates the previous billed amounts by including the value of
 the changed billing to the previous amount of all subsequent billings.
Note: If the previous billing is flagged for deletion (i.e. the Status drop-down is set to D-Delete), select the next previous billing to perform the manual update of previous amounts. The system skips bills marked for deletion during the update process.

You can also update the previous amounts after deleting a billing. There are two methods available for deleting billings:


- Using the Delete
 button – This function can only be used on billings that have not
 been interfaced. If you elect to use this option and the 'auto update previous'
 feature is in use, the system will automatically update the previous amounts for
 all subsequent billings. If you are not using 'auto update previous', select the
 prior billing and use the manual update option ( File > Update Prev Amts, ACO Adds/Deds on Future Bills) to update the previous amounts on all subsequent billings.

- Setting the
 Status to Delete – This function is used for interfaced or
 closed-month billings, but can also be used for active billings. When this option
 is used, the system updates previous amounts automatically (if using the 'auto
 update previous' feature). However, if not using the 'auto update previous'
 feature, select the prior billing and use the manual update option ( File > Update Prev Amts, ACO Adds/Deds on Future Bills) to update the previous amounts on all subsequent billings. The
 system skips bills marked for deletion during the update process, but the previous
 amounts for all other future billings update accordingly.
