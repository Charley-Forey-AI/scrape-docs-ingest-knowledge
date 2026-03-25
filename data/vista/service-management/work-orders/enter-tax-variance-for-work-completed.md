---
title: "Enter Tax Variance for Work Completed | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/enter-tax-variance-for-work-completed"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/enter-tax-variance-for-work-completed"
---

# Enter Tax Variance for Work Completed

If you need to record both sales and use tax when capturing work completed, you can do so when entering AP invoices or SM Work Completed Misc lines.
You will generally use tax variance when an SM-related cost transaction requires both sales tax paid to the vendor and use tax due to a local jurisdiction, where one imposes a higher tax rate than the other.When this occurs, the use tax posted for the transaction will be the difference between the calculated use tax amount and the sales tax already paid to the vendor.
You can only apply tax variance to AP transactions (via AP Transaction Entry or AP Unapproved Invoice Entry) for SM work order lines (type 8-SM Work Order) or PO lines posted to an SM work order (type 6-PO), or to work completed Misc lines entered directly in the Work Completed grid in SM Work Orders or the SM Work Completed Misc form.
Note: These instructions discuss using AP Transaction Entry and the Work Completed grid in SM Work Orders. However, you can also enter tax variance transactions in AP Unapproved Invoice Entry and in the SM Work Completed Misc form.

1. In AP Transaction Entry for an SM Work Order

1. Create a new invoice and enter the header information.

1. Add a new line, using line type 8-SM Work Order.

1. Select the appropriate SM Co, work order, and scope, and then enter additional information as needed.

1. In the Tax Type field, select 1-Sales.

1. In the Tax Code field, enter a tax code that represents the tax rate charged by the vendor. For example, if you normally pay a 10% tax rate, but the vendor only charged you 3% tax, enter a tax code with a 3% tax rate.

1. In the Tax Basis field, enter the tax basis or accept the default value.

1. Save the line.

1. Enter a second transaction line on the same invoice to the same SM Co, work order, scope, and SM Cost Type.

1. Skip to the Gross field and set to 0.00.

1. In the Tax Type field, select type 2-Use.

1. In the Tax Code field, enter a tax code that represents the remaining tax percent owed. In our example, the vendor charged you 3% tax, so you still owe 7% in tax. Therefore, enter a tax code with a 7% tax rate.

1. In the Tax Basis field, enter the same tax basis you entered on the first transaction line.

1. Save the entry and post the batch.

1. In AP Transaction Entry for an SM Purchase Order

1. In PO Purchase Order Entry or SM Purchase Order Entry, create a new SM purchase order and add one line with Sales tax.

1. Post the PO batch.

1. In AP Transaction Entry, create a new invoice and then initialize the PO.

1. Leave the information as defaulted, but change the tax code to a tax code that represents the tax percent charged by the vendor. Using the example above, you would enter a tax code with a 3% tax rate.

1. Enter a second transaction line to the same PO/PO Item with a 0.00 gross amount, and set the Tax Type to 2-Use.

1. In the Tax Code field, enter a tax code that represents the remaining tax percent owed. In our example, the vendor only charged 3%, so you would enter a tax code with a 7% tax rate.

1. In the Tax Basis field, enter the same tax basis you entered on the first transaction line.

1. Save the line and post the batch.

1. In SM Work Orders, Work Completed Grid

1. Open SM Work Orders and enter the work order number.

1. Select the Work Completed tab.

1. Enter a new line with a line type of 3-Misc and select the appropriate work order scope.

1. Enter the transaction information as normal, setting the Cost Tax Type to 1-Sales.

1. In the Tax Code field, enter a tax code that represents the tax rate paid to the vendor. Using our example above, you would enter a tax code with a 3% tax rate.

1. Enter the remaining information and save the line.

1. Enter a new line of type 3-Misc to the same work order scope and SM CT (if one was entered).

1. Leave the Cost Qty, Cost UC, and Cost Subtotal fields blank.

1. Set the Tax Type to 2-Use.

1. In the Tax Code field, enter a tax code that represents the remaining tax percent owed. In keeping with the example above, if you only paid 3% to the vendor, you would enter a tax code with a 7% tax rate here.

1. In the Cost Tax Basis field, enter the same cost tax basis you entered for the first line.

1. Enter the remaining information and save the line.

Using the examples above, between the Sales and Use tax transactions, you have fully costed the 10% tax you normally pay. Additionally, once the transactions are posted, the system appropriately updates GL for each transaction line. You can see the GL detail using the Posted Detail tab in SM Work Orders.Please note that for miscellaneous lines entered in AP and SM, the Posted Detail shows one debit line that includes the sales tax, one debit line for the cost side of the use tax entry, and one credit line representing the accrual of the use tax liability.
 For PO lines invoiced in AP, the grid shows one debit line that includes the sales tax and one debit line for the cost side of the use tax entry; no credit entry is shown for the use tax, as tracking accrual of the use tax liability for PO-related transactions is handled in AP.
