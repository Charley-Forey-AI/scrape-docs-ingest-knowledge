---
title: "About Calculating Taxes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/about-calculating-taxes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/about-calculating-taxes"
---

# About Calculating Taxes

The PO Purchase Order Entry form calculates sales, use, or value added tax for each transaction line on a PO that has a valid tax code assigned to it.
Tax codes are set up in HQ Tax Codes,
 and are used by Accounts Payable, Accounts Receivable, and Purchase Order forms.
To generate sales, use, or value added
 tax for each item on the purchase order, specify both a valid type (Sales, Use, or
 VAT) in the Tax Type field and a valid code in the Tax
 Code field. The tax amount then displays in the Tax
 Rate field.

- Sales Tax - To calculate sales tax for items on a purchase
 order (PO Purchase Order Entry), you must select "Sales" as the Tax Type and
 enter a valid tax code. Taxes, although calculated for each item, do not
 display on the screen. The tax amount will show on the Purchase Order when
 printed, and will also show when invoicing in AP. The calculation of sales
 tax for each item on a purchase order depends on the PO type.

- Job POs - In HQ Tax Codes, you can specify a phase and/or
 cost type to which taxes expensed to a job will be posted. If the tax code
 specified for the job is assigned a tax phase and/or cost type, the tax
 amounts generated for the purchase order will be accumulated and directed to
 the appropriate tax phase/cost type for the job. If no phase/cost type is
 assigned to the tax code, tax amounts will be posted to the phase/cost type
 specified on the purchase order.

- Inventory POs - Inventory sales tax can either be expensed
 separately or added into the cost of inventory/ materials. This is set up in
 the Inventory Company file. If the Posting Burdened Unit Cost option is
 selected, generated tax amounts will be accumulated for each tax code on the
 basis of inventory location and GL account. If the Posting Burdened Unit
 Cost option is not selected, and a GL account is specified in the GL Account
 For Tax field, sales tax is calculated for each tax code/GL account on the
 PO.

- Expense POs - Sales tax for goods purchased with an
 Expense PO is calculated for each tax code/GL account combination on the
 PO.

- Equipment and Work Order POs - For Equipment and Work
 Order POs, sales tax is calculated for each tax code and equipment/cost
 code/cost type combination. The equipment/cost code/cost type determines to
 which GL account the tax will be posted.

- Use Tax - Use tax is a tax liability calculated on a
 payable transaction that is paid to a taxing authority (usually at a later
 time) instead of to the vendor (as with sales tax). For example, a
 contractor working out of state knows that a vendor should have charged
 sales tax and may accrue the liability for tax auditing purposes. Use tax
 can be calculated for purchase order items in Purchase Order Entry. If you
 wish to calculate and accumulate use tax for purchased goods, select “Use”
 as the Tax Type and specify a valid tax code. The use tax is calculated, but
 because it is not paid to the vendor, it is not added to the total of the
 purchase order. Instead, when the AP invoice is posted, the tax amount is
 stored in the appropriate GL account and will display on Use Tax reports.
 When it is time to pay the use tax, you can run a report to determine the
 amount owed to the taxing authority.

- Value Added Tax -Value Added Tax (VAT) is paid on goods
 and services at each stage of production or distribution, and is based on
 the value added at each stage. This tax is tracked in the GL and reduces the
 payment to a taxing authority through an Input Tax Credit (ITC). You do not
 directly expense this tax. When you create a PO with a VAT code tracking
 Goods and Services Tax (GST), the system excludes the tax amount from the
 invoice total. When you receive the PO, the system debits the tax amount in
 the account you specified for tracking ITCs (Debit GL Account field, HQ Tax
 Codes, Add’l Options tab). When you pay the taxing authority, the amount in
 the ITC account is subtracted from the amount you owe. For more information,
 refer to Processing VAT Transactions in Related Topics below.Note: (for Canadian users) If you are using
 a multi-level code tracking both GST and Provincial Sales Tax (PST), the
 system includes the PST amount in the invoice total; the PST amount is
 directly expensed.

Related information

- [Post Sales, Use, and Value Added Tax](/en/vista/vista/accounting/accounts-payable/invoices/taxes-and-discounts/post-sales-use-and-value-added-tax)
