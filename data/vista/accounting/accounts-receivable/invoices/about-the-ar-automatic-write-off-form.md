---
title: "About the AR Automatic Write-Off Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-automatic-write-off-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-automatic-write-off-form"
---

# About the AR Automatic Write-Off
 Form

Use the AR Automatic Write-Off form to write off account balances, invoice balances,
 and finance charges that are considered uncollectible.
You can access this form by selecting
 File > Auto
 WriteOff Process from the AR Invoice Entry form.
Use the Use Date or Days Older Than and
 Write Off Transaction Filter sections to restrict the
 transactions included in the write-off process. For specific information about
 each option in these sections, see the F1 help.

## Write-Off Type

The Write Off Type determines
 whether you will be writing off finance charges, invoice balances, or
 account balances. If you are writing off finance charges, the system enables
 two additional checkboxes that control how finance charges are written off.
 These checkboxes are discussed below.

- FC By (%), Apply to All Lines – When you select this
 checkbox, system multiplies the specified FC Amount or FC Percentage
 value against each line of the invoice equally. The system bases the
 write off amount for each line on the line's amount and the
 percentage.For example, with a FC Amount
 or FC Percentage of 50.00, the write-off amounts for each line
 are calculated as follows:

FC
 Due
Write-Off Amount

Line #1
36.00
18.00 (36.00 x 50.00)

Line #2
27.00
13.50 (27.00 x 50.00)

Line #3
42.00
21.00 (42.00 x 50.00)

- FC By (%), Amt Applied Starting at Line 1 – When you
 select this checkbox, the system multiplies the FC Amount or FC
 Percentage value against the total remaining finance charge amount for
 the invoice to determine the dollar amount to be written off against
 each line. The system distributes the write-off amount beginning with
 line #1 and progressing to each successive line until the specified
 amount has been distributed in full. Remaining lines are left
 untouched.For example, with a FC Amount or
 FC Percentage of 50.00, the write-off amounts for each line are
 calculated as follows:

FC
 Due
Write-Off Amount
Applied

Line #1
36.00

36.00

Line #2
27.00
52.50 (105.00 x 50.00)
16.50

Line #3
42.00

0.00

If you do not use either of the
 FC By (%).. checkboxes, the system handles the finance charge write-off
 process as follows:

- If the FC Amount or FC Percentage value is 0.00, the
 system sums the finance charges for each line. If there is a finance
 charge due for the line, the system compares the finance charge due
 with the line's actual amount due (less retainage), and creates a
 write-off transaction for each line either equal to the finance charge
 due or the line's actual amount due, whichever is less.

- If the FC Amount or FC Percentage value is greater
 than 0.00, the system distributes the write-off amount to each line
 beginning with line #1 and progressing to each successive line until
 the specified write-off amount is fully applied. Remaining lines are
 left untouched.

If you are writing off invoice balances, the system uses the Balances Less
 Than amount to determine which balances to write off. Any positive or
 negative invoices with a total due (including retainage) less than this
 amount are written off. For example, if you are writing off by invoice
 balance and you specify Balances Less Than $25.00, the system writes off
 any invoice with a balance between -$25.00 and $25.00.
Invoice #
Balance
Write-Off?

1001
$15.00
Y

1002
-$12.50
Y

1003
-$35.00
N

Note: Although you can specify a range of
 invoices to write off, it is recommended that you specify a single invoice.
 This will ensure that the system writes off only the invoices that you want.
 Performing this on a range of invoices may inadvertently cause an invoice to
 be written off that should not have been.
The same applies when writing off account balances, except that the process
 applies to the overall account balance. In this case, the system sums all
 invoices for the customer having a transaction date older than the days /
 date specified. If the sum of all applicable invoices is less than or equal
 to the Balances Less Than amount, the system cycles through those invoices
 and applies a write-off transaction against any lines that are not paid in
 full.
Note: This feature may be useful after writing
 off individual invoices to catch small remaining unapplied balances. In
 addition, this is the only option that includes/writes-off “Payment
 On-Account” transactions.
Once the system generates the
 write-off transactions, they are available in AR Invoice Entry for review
 and limited editing, and can be processed as normal.
