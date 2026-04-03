---
title: "A/P Transaction Register - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-transaction-register/ap-transaction-register---cost-center-information"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-transaction-register/ap-transaction-register---cost-center-information"
---

# A/P Transaction Register - Cost Center Information

If the cost center feature is enabled in the
 Enterprise Installation screen, the starting screen includes a
 selection for a cost group, and you have the ability to set up separate inter-post and
 inter-company G/L accounts.

- The A/P Transaction Registers will include invoices only if the operator
 requesting the report has permission to access the associated cost center. The
 cost center used for comparison purposes with the operator's allowed codes is the
 cost center recorded on the main screen of Vendor Invoice
 Entry.

- The Summary Transaction Register provides the cost center assigned to each
 invoice. This is the cost center recorded on the main screen of Vendor
 Invoice Entry. The Transaction Register and the Detail Transaction
 Register reports show both the invoice cost center and the cost centers assigned
 to the detail distribution.

- Spectrum determines whether all distribution lines of the invoice are assigned
 to the same cost center as in the invoice header. For multi-company entries, the
 software will read the company code of the distribution line, and then determine
 if that company code has been assigned a particular inter-company G/L account. For
 entries in the invoice company, the Accounts Payable
 Installation setup of the invoice company is used, and for the
 entries to the company referenced in the distribution, the Accounts
 Payable Installation setup of that other company is applied.
 Inter-post entries are not applicable for these transaction lines.

- When cost centers are used and the Enterprise
 Installation option for Allow G/L account overrides by
 cost center is selected, Spectrum will assign inter-posting amounts
 and discount taken amounts to multiple General Ledger accounts by cost center
 based on a list of override G/L accounts in Accounts Payable
 Installation. In addition, Spectrum will assign Accounts Payable
 trade, subcontract, retention, cash and discount amounts to multiple General
 Ledger accounts, by cost center based on a list of override G/L accounts in the
 respective Override windows in Accounts Payable
 Installation.

- When overrides are set up, Spectrum automatically substitutes the designated
 G/L account specified in Accounts Payable Installation as
 an override for lines referencing the cost center with the override account. The
 operator is not required to possess cost center authorization in order to write to
 this override G/L account in order to update.

- When cost centers are set to Yes in the current company, the applicable inter-post account
 entries are generated for credit card transactions and pre-paid invoices.
 Likewise, when cost centers are used, the registers and update only include
 'credit card' invoices and credit memos that the operator is allowed to
 access.

- When the cost center is assigned to the Current VAT and Retention VAT G/L entries, detailed above, the software will not validate whether the invoice cost center is authorized for the particular G/L account (from the VAT Tax Code Table).
