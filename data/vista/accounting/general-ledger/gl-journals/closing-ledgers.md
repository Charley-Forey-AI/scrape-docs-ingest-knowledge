---
title: "Closing Ledgers | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/general-ledger/gl-journals/closing-ledgers"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/general-ledger/gl-journals/closing-ledgers"
---

# Closing Ledgers

The act of closing a month indicates that it is complete and accurate and that no additions or corrections are needed.
Once closed you will still be able to run journal and trial balance reports, as well as financial statements on the period, but you will no longer be able to post or make corrections to the month. The last month the subsidiary ledgers and the General Ledger are closed is stored in the company file automatically when GL Month End Close is run.
 The flexibility of the month-end close process allows you either to close all subsidiary ledgers at one time or to close AP and/or AR independently from other ledgers. This allows you to restrict entry in AP and/or AR, while leaving other modules open for month-end activities (such as posting cost and other month-end adjustments, and running allocations).
 The General Ledger may be closed in any month equal or prior to the subsidiary ledgers. When you direct the system to close ledgers, a search is made to make sure that all of the batches containing data for that module/month have been posted. Any unposted batches found will be listed for you because all batches pertaining to the modules being closed and the period must be posted before the ledgers can be closed.
 Monthly closing is not required before moving on to another month. In GL Company Parameters, you specify the number of months that ledgers can be open. This allows you complete control over how far into the past and future entries may be posted. The number of months open in Company Parameters refers to the number of months the subsidiary ledgers may be open. The General Ledger may be left open for as many additional months as desired.
 The number of months open in GL Company Parameters may be changed by someone having access to this program (typically the Controller or System Administrator). Therefore, as an example, it might be set at 3 or 4 months when first going on line to allow time for bringing balances forward and reconciling all systems, and for getting comfortable with the new system. Then restrict access to 2 months, perhaps, for normal monthly processing. When you get to year-end, open it up 3 or 4 months again to allow for year-end closing.
 The General Ledger is typically kept open for the whole year to allow adjusting entries to be made if needed. However, if you prefer to close the GL on a monthly basis, you may do this. Once a month is closed in the subsidiary ledgers or the General Ledger, no further entries may be made to the month. A month may be reopened after it has been closed by “backing up” the month in GL Month End Close. Because of this flexibility, you may want to restrict access to this form to only the Controller or the System Administrator.
