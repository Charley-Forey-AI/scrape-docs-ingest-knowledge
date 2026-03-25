---
title: "About the AR Release Retainage Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-release-retainage-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-release-retainage-form"
---

# About the AR Release Retainage Form

You can use the AR Release Retainage form to release retainage
 that you held back for payment. You can release retainage for all invoices related to a
 customer or for a specific customer contract.
You can only release retainage if the following conditions apply:

- Retainage was previously applied to the contract or invoice.

- You have not fully paid or released retainage.

- You entered the invoices directly into AR, that is, you did not interface them from JB.

Once you specify a customer, all invoices for that customer (contract and non-contract) are displayed in the grid. Additional inputs allow you to restrict display of invoices to all invoices for a specific JC company or all invoices for a JCCo and Contract.
Although retainage is applied to individual items on an invoice, you will release retainage at the invoice level. The system will then determine the amount to release for each item on the invoice based on the method used to release retainage and the amount released.

## Releasing Retainage

You can release retainage manually or automatically. If releasing retainage manually, once you have entered the filter criteria and released retainage invoice information, click the chevron button. Then for each invoice in the grid, manually enter the release percent or release amount. Once you move off the line, the record is saved and you can then access the line detail (via the Release Details button) to adjust the release amounts for each invoice line as applicable.
To release retainage automatically, check the Auto Calculate Release Retainage option, specify the date through which to release billed retainage, and select the method by which to calculate the retainage to release. There are two release methods available:

- Percentage – With this method, you specify the percentage to release, which is applied to all invoices. For each invoice, the system releases the specified percentage of the total open retainage for the invoice. It then distributes that amount to the items, beginning with the first item and continuing with subsequent items until the released amount is fully distributed. For example, you have an invoice with a total of $2000 in open retainage, with item retainage as follows:Item 1 : 600.00 Item 2: 700.00 Item 3: 700.00
You release 45% of the invoice's total open retainage, which calculates to $900. The system applies this amount to the items as follows:Item
Open Retg
Release Amt
Release Pct

1
600.00
600.00
100.00%

2
700.00
300.00
42.86%

3
700.00
0.00
0.00%

Since the amount does not fully cover the retainage for all three items, it releases the first item fully, applies the remainder to Item 2, and releases nothing for Item 3.

- Amount - With this method, you specify a flat amount to release. The system will release retainage beginning with the oldest invoice and continuing through each successive invoice until the total amount you specified has been released. For example, if you specified to release $3500 of open retainage, it would be released as follows:
Mth
Invoice
Open Retg
Release Amt
Release Pct

01/08
100
1800.00
1800.00
100.00%

03/08
101
1000.00
1000.00
100.00%

06/08
102
2500.00
700.00
28.00%

 For Invoice #100 and #101, retainage is fully released for each item. However, since only part of the retainage was released for Invoice #102, the system applies the release amount to the first item and if a balance remains, continues to apply to remaining items until amount is fully applied.

Regardless of whether you release retainage manually or automatically, once retainage is released, the following occurs:

1. The system creates a single credit transaction for the total release amount. This transaction is assigned a transaction type of Release Retainage and a transaction number. A transaction line is created for each invoice line being released, with each line applied to the transaction number and line number of the original invoice.

1. The system then creates a single invoice (using the invoice number specified in the release retainage header) with one item for each line on the transaction. If multiple lines point to the same contract item, they will be combined into a single invoice item.

Once you process the batch, the invoice is then available for printing using the AR Invoice report. AR Release Retainage form closes and the system releases the retainage accordingly. The system creates a single invoice (using the invoice number from the Invoice # field in the header section) with one line item for the total amount of released retainage. To print this invoice, use the AR Invoice report in the AR Reports folder.

## Retainage Tax

If you are using the Distribute Tax to Retainage feature (AR Company Parameters), retainage tax is calculated separately during invoice entry and updated to the Credit GL Retg Account (defined in HQ Tax Codes). This tax is not due for payment until retainage is released using this program.
When releasing retainage for an invoice, you will note that the Open Retainage amount includes the retainage tax amount. For example, if the retainage amount is $100.00 and the retainage tax is $15.50, the Open Retainage will show as $115.50.
During the retainage release process, the system releases the retainage tax in direct proportion to the amount of retainage being released (e.g. if you release 10% of retainage, it will also release 10% of retainage tax). If applicable, the released retainage tax is broken out into GST and PST amounts and updated to the appropriate GL accounts (debits retainage tax payable account and credits tax payable account).
When generating the released retainage invoices, the system calculates tax at the current rate (based on the current date and the tax code's Effective Date for tax rates). Therefore, the credit to the tax payable account may differ from the amount debited from the retainage tax payables account (as shown in example below).
 Debit
Credit

AR Receivables 115.50
Retg Receivables 115.50

GST Retg Tax Payables 5.00
GST Tax Payables 5.00 7.50 (GST Rate changed)

PST Retg Tax Payables 10.50
PST Tax Payables 10.50 16.00 (PST Rate changed)

Once the system has calculated the amount to release, you can view the amount released for each item on the invoice by clicking Release Details and modifing as necessary.
To prevent taxes from being calculated on retainage for specific invoices, the following must apply:

- For non-contract invoices, the Tax Code field must be blank for the customer (in AR Customers) and for all lines on the applicable invoice.

- For contract invoices, the Tax Code field must
 be blank for the contract/contract items in JC Contracts/JC Contract
 Items and for all lines on the applicable invoice.

## Aging Released Retainage

Invoices created by released retainage (AR Release Retainage) can be aged the same as invoices created in AR Invoice Entry, if the Release Retainage to Current A/R checkbox in AR Company Parameters is selected. The system treats the retainage invoice as a regular invoice and is aged by the release date and due date.
If you do not select the Release Retainage to Current A/R checkbox, the system still creates an invoice, but does not recognize it as a regular invoice. The released retainage will appear on the aging report in the Retainage column.Note: If you use different GL accounts for regular A R and Retainage Receivable, and you select the Release Retainage to Current A/R checkbox, the new released retainage invoice uses the regular AR account. In other words, releasing retainage moves the amount from Retainage Receivable to Accounts Receivable.
