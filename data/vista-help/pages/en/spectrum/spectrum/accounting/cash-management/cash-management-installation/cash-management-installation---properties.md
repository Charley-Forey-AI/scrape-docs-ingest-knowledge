---
title: "Cash Management Installation - Properties | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/cash-management/cash-management-installation/cash-management-installation---properties"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/cash-management/cash-management-installation/cash-management-installation---properties"
---

# Cash Management Installation - Properties

Use this tab to select default properties settings for the
 Cash Management module.
These settings can be changed as needed at any time.
Field
Description

Allow entry of opening balance?
The software is prompting you to decide whether to allow the operator to enter the beginning cash balance per bank and credit card statement. As a rule, this checkbox should be clear.
Normally, the beginning balance is automatically rolled forward from the previous month. The only time this checkbox should be selected is during conversion when the first month's bank or credit card reconciliation is recorded. From then on, this checkbox should be clear, requiring the ending balance from the prior months to display as the beginning balance in the new statement.

Require reconciliation to balance with G/L in order to update?
This option is used to require the calculated General Ledger balance in Bank Reconciliation Entry to match the actual ending balance in the associated General Ledger cash account before permitting the reconciliation to be updated. If you require the difference on the G/L side of the reconciliation to be zero before the G/L reconciliation can update, select this checkbox.
This checkbox is used to determine whether the calculated G/L reconciliation balance is required to match the actual G/L balance in the associated cash account prior to updating. If this checkbox is selected, then the Cash Management bank reconciliation will not update until the difference between the G/L reconciliation calculated balance and the actual General Ledger balance is zero. In most cases, this checkbox will be selected.
If it is deemed necessary that the Cash Management reconciliation should be updated without the G/L reconciliation difference being zero, then simply clear this checkbox.

Direct checks dollar limit
The software is prompting for the maximum dollar for any single direct check issued. This limit can be used as a security measure to control the size of a direct checks issued.
For example, it may be set to 500 if the operator should be restricted to transactions of $500 or less. If no dollar amount is entered, then no limit will be imposed.

Inter-company G/L account code
Enter the G/L account code you plan to title "inter-company receivable" (or similar name) in your Spectrum chart of accounts. Be sure to include this G/L account number when you enter your chart of accounts.
The software will automatically update inter-company transactions to this G/L account code when you designate alternate company code(s) during wire transfer entry. Entry is required in this field even if you do not plan to perform multi-company transactions. This account will be the debit entry for multi-company wire transfer lines.
