---
title: "Multi-Currency and Cash Management | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/multi-currency/multi-currency-and-cash-management"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/tools/multi-currency/multi-currency-and-cash-management"
---

# Multi-Currency and Cash Management

The Cash Management module maintains currency by account.
 Each bank account and credit card account can be assigned a transaction currency. This will be
 known as the "Account currency."
Processing Rules

- Transactions originating in Cash Management (direct checks, wire
 transfers and reconciliation adjustments) do not having timing issues that would
 result in a currency gain or loss.

- Transactions posting to Cash Management from Accounts Payable will
 be recorded using the account currency, even if the source transaction is tracked in
 that other module in a different currency. Any timing issues will be calculated in
 the source module.
Click the links below to learn how Multi-Currency impacts each of
 the following areas:

Account Code Maintenance
To assign the currency code to the bank or credit card account, navigate
 to the Cash Management > Maintenance > Account Code File Maintenance > Edit Account, Details tab. Select the 'Override currency?' checkbox and enter the currency code.
 Also enter the Gain/Loss G/L account for currency fluctuations here as well.

- On the main screen, you can group accounts with the same currency
 together by sorting the Accounts listbox by currency code.

- By rule, a <BLANK> currency code is deemed to be the
 reporting currency.

- The currency tracking section only displays when the
 Multi-Currency module is enabled.

Example:
Note: Best practice — Include the currency in both the code AND
 description. Because various accounts will have different currencies, it is important to
 understand that running reports for 'ALL' will produce reports with different currencies
 commingled together. It is recommended to use 'smart coding' when creating account codes
 as it will make it easier to run reports for a specific currency. Adding the currency to
 the description will make it easier for others to understand the currency being used
 elsewhere in the system. For example, when creating an Instant Manual Check in Vendor
 Invoice Entry, including the currency in the account's description makes it easier for
 the user to select the appropriate account.
Bank Account & Credit Card Reconciliation

- Reconciliation of the bank account and credit card account will be
 performed in the account's currency.

- Reconciliation adjustments will be also be recorded in the
 account's currency, but will be translated into the reporting currency when updated
 to the General Ledger.
Processing Rules

- The account and reporting currency codes display on the screen.


- Reconciliation adjustments will be made using the account's
 currency, but will be translated into the reporting currency when updated to the
 General Ledger. This means that the Reconciliation Adjustments Register will print in
 the reporting currency only.

- When the account currency is not the same as the reporting
 currency, the 'Require G/L to be in balance' rule will not be enforced when
 multi-currency is enabled. As it is feasible that there will be some rounding
 differences when converting the local currency into the reporting currency, the
 decision was made to not prevent the user from updating a truly "balanced"
 reconciliation.

Direct Check / Void Direct Check
Direct checks are written in the currency assigned to the bank account.
 Void direct check uses the same rule.
Processing Rules

- Direct checks are be recorded in the currency specified for the
 account, but will be translated to the Reporting currency when updated to General
 Ledger and Job Cost.

- The Direct Check Register prints in the reporting currency,
 showing values as they will post to General Ledger.

- By rule, there are no gains or losses on currency fluctuations on
 direct checks and on void direct checks.

Wire Transfer / Void Wire Transfer
Wire transfers use the currency associated with the accounts used. Void
 wire transfer uses the same rule.
Processing Rules

- Wire transfers will be recorded in the currency specified for the
 account, but will be translated to the reporting currency when updated to General
 Ledger and Job Cost.

- Multi-company wire transfers will be converted to the reporting
 currency of the destination company during the update.

- The Wire Transfer Registers will print in the reporting currency,
 showing values as they will post to General Ledger.

- By rule, there are no gains or losses on currency fluctuations on
 wire transfers and on void wire transfers.
