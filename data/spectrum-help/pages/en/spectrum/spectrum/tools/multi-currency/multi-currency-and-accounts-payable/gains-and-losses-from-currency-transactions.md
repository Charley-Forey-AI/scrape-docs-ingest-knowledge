---
title: "Gains and Losses from Currency Transactions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/multi-currency/multi-currency-and-accounts-payable/gains-and-losses-from-currency-transactions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/tools/multi-currency/multi-currency-and-accounts-payable/gains-and-losses-from-currency-transactions"
---

# Gains and Losses from Currency Transactions

When a vendor invoice is paid in a non-reporting currency, it
 must be revalued using the exchange rate in effect on the check date. The difference between
 the translated value of the original invoice less the translated value at check date will
 create a gain or loss from currency transactions.
(Invoice FX Rate less Check FX Rate) X Amount Paid in Vendor
 Currency

- A positive value indicates a currency gain and will be booked
 as a Credit.

- A negative value indicates a currency loss and will be booked
 as a Debit.

Gains and losses will be booked to the 'Gain / loss G/L account' from
 Account Maintenance.
Gain/Loss Example:
A vendor invoice for $100.00 CAD has a G/L date of 11/15/15. This
 invoice was paid in full on 01/05/16.
Invoice G/L date 11/15/15 (1.00 USD = 1.301234 CAD → 1.00 CAD =
 0.768501 USD)
Check date 01/05/16 (1.00 USD = 1.320910 CAD → 1.00 CAD = 0.757054
 USD)
(FX rate on Check Date less FX rate on G/L date) X Amount paid in
 vendor currency
(0.768501 – 0.757054) X 100 = $1.14 USD
The cost of Canadian currency decreased between the G/L date of the
 invoice and the Check date. Here we have a gain on currency transactions.
The system will book this loss using the 'Gain/loss G/L account'
 defined on the bank account code.
Example:
