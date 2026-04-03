---
title: "Reconciling Job Costs with the General Ledger | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/troubleshooting/reconciling-job-costs-with-the-general-ledger"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/troubleshooting/reconciling-job-costs-with-the-general-ledger"
---

# Reconciling Job Costs with the General Ledger

The general process of reconciling Job Cost to General Ledger involves using the Cost Type Summary Report to identify the problem cost type, then comparing G/L Transaction Journals and G/L Distribution Report from the relevant module (Payroll for labor, A/P for materials, etc).
The following procedure will guide you through determining what is causing out-of-balance job cost figures.

- [Printing the Cost Type Summary Report](/en/spectrum/spectrum/project-management/job-cost/troubleshooting/reconciling-job-costs-with-the-general-ledger/printing-the-cost-type-summary-report) for the necessary fiscal period.

- [Printing the General Ledger Trial Balance Report](/en/spectrum/spectrum/project-management/job-cost/troubleshooting/reconciling-job-costs-with-the-general-ledger/printing-the-general-ledger-trial-balance-report) for the necessary fiscal period (same fiscal period as was specified in step 3).

- Compare the Cost Type Summary Report and the General Ledger Trial Balance Report. Check to see that the total expense in Job Cost equals the total expense in the General Ledger direct cost accounts.

- Check to ensure that each cost type in Job Cost should equal its counterpart in General Ledger.
Once you have completed the steps above and have confirmed that the Job Cost and General Ledger modules are out of balance, review the Job Cost Type File Listing.

- Review the Job Cost Type File Listing, which can be accessed by clicking Job Cost > Maintenance > Cost Type > Listing.

- In this listing, review all your G/L accounts to see which cost types have been assigned to each.

- The G/L account may be blank if you have each cost type going to multiple G/L accounts. There may be no cost types printed if you have multiple cost types going to the same G/L account. This ensures that the right cost types have the right G/L accounts associated with them and that you have been selecting the correct G/L accounts to reconcile with your job costs expenses. Also this helps to insure no one has made any changes that you are unaware of.

- Additionally, check to make sure the G/L accounts are being used as follows:

- Have you selected the right G/L accounts to compare to each cost type?

- What G/L accounts, if any, have been assigned to your cost types? Are they correct?

- Have you been including these G/L accounts in your reconciliation?

If a journal entry is made to any direct cost accounts, there should be
 a corresponding entry to Job Cost. Normally, any direct cost G/L account will have the
 direct cost field set to Job cost
 in the General Ledger  >  G/L Master File Maintenance screen. As long as this is set to Job cost, you will be prompted to enter a
 job number whenever you post anything to this account. However, it is possible to turn this
 flag off on a particular direct cost G/L account. Have any of the Post to GL? checkboxes (found in the
 General Ledger Installation
 screen) been deselected at any time recently? If so, select these checkboxes.
