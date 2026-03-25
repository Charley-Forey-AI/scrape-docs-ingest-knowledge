---
title: "Add JC Cost Detail to a T&M Billing | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/add-jc-cost-detail-to-a-tm-billing"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/add-jc-cost-detail-to-a-tm-billing"
---

# Add JC Cost Detail to a T&M Billing

You can add previously deleted cost detail lines, as well as new cost detail lines, to bill lines for a T&M billing without affecting changes made to existing lines.
Note: Lines added using this method must meet the same criteria as when manually adding a line; that is, the transactions detail must be valid for the template seq/line.

1. Open JB T&M Bill Edit and select the bill month and bill number to work with.

1. To add cost detail at the bill level, do the
 following:

1. Select File >  Job Cost DetailThe JB T&M Bill All JCDetail Lines form
 displays.

1. Click Refresh Cost Detail.The JB T&M JC Detail Fill Grid form displays.

1. Proceed to Step 4.

1. To add cost detail at the bill line/sequence level, do the following:

1. Click Bill
 Lines.The JB T&M Bill Line Sequences form displays.

1. In the upper grid, select the bill line to work with.

1. In the Line
 Seq field (lower grid), select the sequence to update or
 press F4 for a
 list of valid sequences for the bill line.

1. Click JCDetail.the JB T&M Bill JCDetail by Seq form displays.

1. Click Fill Grid.The JB T&M JC Detail Fill Grid form displays.

1. Proceed to Step 4.

1. In the Cost Detail Beginning Date field, enter the beginning date in a range of transactions to add.

1. In the Cost Detail Ending Date field, enter the ending date in a range of transactions to add.

1. In the Cost Detail Cutoff Month field, enter the detail cutoff date; that is, the last date of posted cost detail that you want included in the grid.

1. If you want to use a different cutoff date for pulling in labor cost detail:

1. Select the Use Different labor cutoff date checkbox.

1. In the Labor Cutoff Date field, enter the cutoff date through which to pull labor costs from Job Cost.

1. Click Fill Grid.

1. Click Close.

The system adds all new or previously deleted lines posted within the specified date range to the applicable grid (JB T&M Bill All JCDetail Lines or JB T&M Bill JCDetail by Seq, depending on how you accessed the JB T&M JC Detail Fill Grid form). The system then updates the bill line sequence, bill line, and invoice totals accordingly.
For more information, click the links below.
[JB T&M JC Detail Fill Grid](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-jc-detail-fill-grid)
[JB T&M Bill All JCDetail Lines Form](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-bill-all-jcdetail-lines-form)
[JB T&M Bill Edit Form](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-bill-edit-form)
