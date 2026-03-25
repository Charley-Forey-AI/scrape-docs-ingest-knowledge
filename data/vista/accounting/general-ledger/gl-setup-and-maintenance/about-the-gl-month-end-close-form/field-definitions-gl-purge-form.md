---
title: "Field Definitions: GL Purge Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/general-ledger/gl-setup-and-maintenance/about-the-gl-month-end-close-form/field-definitions-gl-purge-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/general-ledger/gl-setup-and-maintenance/about-the-gl-month-end-close-form/field-definitions-gl-purge-form"
---

# Field Definitions: GL Purge Form

The following is a list of field descriptions for the GL
 Purge form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Close Options

Select which ledger to close.

- Close Sub Ledgers—Select this option to close subsidiary ledgers.

- Close General Ledger—Select this option to close the general ledger.

[](/en/vista/vista/accounting/general-ledger/gl-setup-and-maintenance/about-the-gl-month-end-close-form)GL Month End Close

## Accounts Payable

This checkbox is enabled only if closing sub
 ledgers and you unchecked the All Others sub ledgers box.
Check this box to close the sub ledgers for Accounts Payable. Checking this box will restrict posting in AP, as well as batches created in other modules containing AP transactions (PR AP Update, SL Update, MS Hauler and Material Payments, and IM uploads of AP transaction data).
Leave this box unchecked if you are not closing AP at this time.
Note: This box is checked automatically and disabled when you select to close all other sub ledgers. In order to close all other sub ledgers, you must close AP and AR.
[](/en/vista/vista/accounting/general-ledger/gl-setup-and-maintenance/about-the-gl-month-end-close-form)GL Month End Close

## Accounts Receivable

This checkbox is enabled only if closing sub
 ledgers and you unchecked the All Others sub ledgers box.
Check this box to close the sub ledgers for Accounts Receivable. Checking this box will restrict posting in AR, as well as batches created in other modules containing AR transactions (JB Progress Billing, JB T&M Bill Init, JB Interface, JB Batch Process, MS Invoice Edit, MS Invoice Initialize, and IM uploads of AR transaction data).
Leave this box unchecked if you are not closing AR at this time.
Note: This box is checked automatically and disabled when you select to close all other sub ledgers. In order to close all other sub ledgers, you must close AP and AR.
For related information, see [About the GL Month End Close Form](/en/vista/vista/accounting/general-ledger/gl-setup-and-maintenance/about-the-gl-month-end-close-form#ID-0000e35d--en__ID-0000e35d).

## All Others

This checkbox is enabled only if closing sub ledgers.
Check this box to close all other sub ledgers. Since closing all ‘other’ sub ledgers requires also closing AP and AR, checking this option will automatically check and disable the Accounts Payable and Accounts Receivable sub ledger options.
Leave this box unchecked if you are closing only AP and/or AR sub ledgers.

[](/en/vista/vista/accounting/general-ledger/gl-setup-and-maintenance/about-the-gl-month-end-close-form)GL Month End Close

## Through Month

Enter the month through which to close the sub ledgers or general ledger. If you are closing General Ledger, make sure that the Through Month is not greater than the last month closed in Sub Ledgers. (The top of the screen displays the last month closed in Sub Ledgers and in General Ledger.)
Note: You may reopen a month by entering any previously closed month. Close Check
Click this button to run the close check. You must run this check before you can close the month; this will determine if any unposted batches exist. If the check encounters any open batches, a message displays indicating that the month is not ready to close. You will need to process the batches listed on each of the tabs before you can close the month.
Once the month is ready to close, the OK button is enabled. Click OK to finish the close process.

[](/en/vista/vista/accounting/general-ledger/gl-setup-and-maintenance/about-the-gl-month-end-close-form)GL Month End Close
