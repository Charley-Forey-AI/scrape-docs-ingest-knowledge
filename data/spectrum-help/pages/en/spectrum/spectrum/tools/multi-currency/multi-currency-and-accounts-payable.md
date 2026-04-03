---
title: "Multi-Currency and Accounts Payable | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/multi-currency/multi-currency-and-accounts-payable"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/tools/multi-currency/multi-currency-and-accounts-payable"
---

# Multi-Currency and Accounts Payable

Vendors are assigned one currency to record Accounts Payable
 and Purchase Order transactions.
When the Multi-Currency module is enabled, the system will allow a vendor to
 be assigned an 'override currency' when the vendor conducts business in a currency that
 differs from the reporting currency. By rule, all transactions for a vendor with an
 override currency shall be processed in that other currency. This override currency will
 be known as the 'Vendor currency'.

## Processing Rules

- Transactions originating in Accounts Payable and Purchase Order will be
 recorded in these modules using the vendor currency. Amounts will be
 translated into the reporting currency for General Ledger, Job Cost (and
 others in later phases).

- Transactions posting to Accounts Payable from other modules (that is, Payroll)
 will be recorded using the reporting currency. No translation into the
 vendor currency will occur.

- The exchange rate is determined and stored when the transaction is
 updated.

- When processing payments, the software will calculate gain or loss from
 currency fluctuations and post differences to the General Ledger. The G/L
 date assigned to the invoice and the check date are used as the transaction
 dates for exchange rate gain/loss calculations. The gain or loss is booked
 to the G/L code defined on the account code itself.

- By rule, there are no gains or losses on currency transactions on instant
 manual checks and on credit card purchases as the invoice G/L date and check
 date will be the same.

- By rule, there is no currency gain or loss when voiding a check. This means
 that the software will reverse the A/P check out exactly as it was written
 and also reverse out any currency gains or losses previously booked to the
 G/L.

## Gain/Loss Formula

(FX rate on Invoice less the FX rate on Check date) X Amount paid in vendor
 currency.

## Aged Paybles Report

The A/P Aged Payables Report is already in each vendor's currency. Running it for ALL
 vendors will comingle different currencies together, making the report meaningless.
 Selecting one currency will select all transactions for that currency.

## G/L Distribution Report

The G/L Distribution History Report will allow the user to print information for
 vendors assigned to a particular override currency, selecting either to see values
 in that currency or translated to the Reporting currency.

## Merge Vendors

Protection has been added to the Change Vendor Code utility so that when 'merging
 vendors', users will be prevented from merging vendors assigned different
 currencies.

## Copy Vendors to Another Company

Special handling will be added to the Copy Vendors to Another Company utility when
 copying vendors among Spectrum companies that use different reporting
 currencies.

## Reports

Aged Payables Report
The A/P Aged Payables Report is already in each vendor's currency.
 Running it for ALL vendors will comingle different currencies together, making the
 report meaningless. Selecting one currency will select all transactions for that
 currency.
G/L Distribution Report
The G/L Distribution History Report will allow the user to print
 information for vendors assigned to a particular override currency, selecting either
 to see values in that currency or translated to the Reporting currency.
Merge Vendors
Protection has been added to the Change Vendor Code utility so
 that when 'merging vendors', users will be prevented from merging vendors assigned
 different currencies.
Copy Vendors to Another Company
Special handling will be added to the Copy Vendors to Another
 Company utility when copying vendors among Spectrum companies that use different
 reporting currencies.
