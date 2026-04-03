---
title: "Multi-Currency | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/multi-currency"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/tools/multi-currency"
---

# Multi-Currency

The Multi-Currency (MC) module enables processing certain transactions in local currencies, necessary if you do business involving more than one currency.
Here is a simplified look at how this module works:

- Spectrum follows US Generally Accepted Accounting Principles (GAAP), including Foreign Currency Matters, Accounting Standards Codification (ASC) 830.

- A single reporting currency may be designated for each company in Spectrum online Help. General Ledger and Job Cost are reported and stored in the reporting currency.

- Bank and credit card accounts in Cash Management can each have a currency code assigned to them, which could be different than the reporting currency of the company. Any transactions for that account are converted to the currency of that account when they post to Cash Management, so that the reconciliation can be done in the currency of that account.

- Vendors may also be assigned a currency different than the reporting currency of the company. All invoices, subcontracts, and purchase orders for that vendor are tracked in the currency of that vendor.

- Job committed costs and unposted transactions are converted to the reporting currency of the company, so that all job costs are in the same currency.

- Payroll is done in the reporting currency of the company; any multi-company transactions are converted to the reporting currency of the job company when posted to Job Cost or General Ledger.

- Multi-company A/P invoices are converted to the reporting currency of the job company.

- As GAAP requires that payables and receivables held in a non-reporting currency must be revalued at period end, the system uses currency specific G/L accounts for balance sheet items.

Related information

- [System-wide Multi-Currency Rules](/en/spectrum/spectrum/tools/multi-currency/system-wide-multi-currency-rules)
