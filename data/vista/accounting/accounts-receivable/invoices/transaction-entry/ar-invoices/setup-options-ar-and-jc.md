---
title: "Setup Options (AR and JC) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/invoices/transaction-entry/ar-invoices/setup-options-ar-and-jc"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/invoices/transaction-entry/ar-invoices/setup-options-ar-and-jc"
---

# Setup Options (AR and JC)

Several of the fields on the AR Invoice Entry screen are
 affected in some way by the setup options selected in the AR Company Parameters, AR
 Customers, and the JC Contracts programs. These fields are explained below.

## Header Fields

- Invoice # – If the Automatically Number Invoices option in AR Company is selected, the invoice number will automatically be assigned for you. (Otherwise, numbers must be entered manually.) This number may be overridden, but it will not update the Last Invoice Number in the Company file. The system will only update this number if you use the system assigned invoice number. If you are using Material Sales (MS) and Job Billings (JB), and each of those modules are using the AR numbering scheme for invoices, the system will assign invoice numbers based on the invoices entered in each of these modules.

- Rec Type – This field will initially default the receivable type assigned to the referenced customer in AR Customers. If no receivable type is specified for the customer, it will use the default receivable type specified in the Company file. If you then enter a contract, the receivable type will default from JB Contract Info (i.e. JCCM) unless none is specified. In which case, it will use the receivable type for the customer or company file, respectively. If you elected to allow overrides to the receivable type (flag in AR Company Parameters), you may override the default during posting, with some exceptions (see F1 help). If you do not allow overrides to the receivable type, the system uses the default from the appropriate file, and the field is disabled.

- Due Date/ Disc Date
 – The defaults in these fields are calculated based on the payment terms
 assigned to the customer (AR Customers) or, if the transaction is
 contract-related, the payment terms specified for the contract (JC
 Contracts).

## Line Item Fields

- GL Account – If the
 transaction is not related to a contract, this field defaults the 'Revenue'
 account assigned (in AR Receivable Types) to the receivable type specified
 in AR Company Parameters. If the transaction is contract-related, this field
 defaults the 'Revenue' account assigned to the department (in JC
 Departmnets) specified for the contract.

- Tax Code – If the Post Taxes on Invoices option is unchecked (in AR Company Parameters), this field is grayed out and inaccessible. This is true even if the invoice is contract-related and the contract item allows for posting taxes.
If the Post Taxes on Invoices option is checked and the invoice is
 contract-related, this field defaults the tax code specified for the
 contract item in JC Contracts. If no tax code is specified for the contract
 item, no taxes may be posted, and this field will be grayed out.
If the invoice is not related to a contract, this field defaults the tax code specified for the customer in AR Customers. If no tax code specified, no taxes may be posted.

- Retg % – The
 Use Retainage
 option in AR Customers determines whether retainage can be posted on
 non-contract related invoices only. If the invoice is contract-related, this
 field defaults to the retainage percent specified for the contract item in
 JC Contracts. If no retainage percent specified for the contract item, you
 can enter the percent manually.

- Retainage Tax – This field only displays on the screen if you allow posting taxes on invoices and have checked the Distribute Tax to Retainage option (AR Company Parameters). If you are posting tax to the invoice line and have specified a retainage amount, the system will calculate tax on the retainage portion separately (as retainage x tax rate) and display the amount in this field. When the invoice is posted, the retainage tax is updated to the Credit GL Retg Account (HQ Tax Codes) and becomes payable when the retainage is released.

- Disc Amt – If the
 invoice is contract-related, the calculation in this field is based on the
 Discount Pct
 specified in the Payment Terms assigned to the related contract (JC
 Contracts).
