---
title: "How Finance/Service Charges are Credited to GL | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/invoices/how-finance-charge-types-are-used/how-financeservice-charges-are-credited-to-gl"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/invoices/how-finance-charge-types-are-used/how-financeservice-charges-are-credited-to-gl"
---

# How Finance/Service Charges are Credited to GL

When finance/service charges are calculated, the system
 credits the GL account specified for finance charge revenue in AR Receivable
 Types.
The GL account is determined as follows:

- On Account Balances and Non-Contract Invoices — The system credits finance/service charges to the FinChg Rec account defined (in AR Receivable Types) for the finance charge receivable type specified in AR Company Parameters (Finance Charges tab).

- Contract Invoices — If you
 select the Calculate Finance
 Charge interface level for finance charges (in AR Company
 Parameters), the system credits the Open Revenue Acct defined in
 JC Departments for the department assigned to the related contract item.

The system normally debits finance/service charges to the Accounts Receivable account assigned to the receivable type specified on the Finance Charges tab in AR Company Parameters. If calculating finance/service charges by invoice, the system assigns the receivable type to which finance/service charges are being applied.
