---
title: "Accounts Receivable Installation - G/L Codes | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/installation-overview/accounts-receivable-installation---gl-codes"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/installation-overview/accounts-receivable-installation---gl-codes"
---

# Accounts Receivable Installation - G/L Codes

Use this tab to select General Ledger code settings for the Accounts Receivable module. These settings can be changed as needed at any time.
Field
Description

Default Account Receivable trade G/L account code
Enter the primary G/L account code you plan to title "Accounts Receivable" (or similar name) in your Spectrum chart of accounts. Be sure to include this G/L account number when you enter your chart of accounts. Enter your AR G/L account even if you do not have General Ledger module installed on your computer.
The software will offer this G/L account code when you enter invoices and credit memos, but you may override this account code as needed.

Retention receivable G/L account code
Enter the G/L account code you plan to title "retention receivable" (or similar name) in your Spectrum chart of accounts. This G/L account code may not be the same code designated as your Accounts Receivable. Be sure to include this G/L account number when you enter your chart of accounts. Enter your retention receivable account even if you do not have the General Ledger module installed on your computer or plan to record retention.
The software will automatically update retention amounts to this G/L account code when you designate retention during Invoice Entry, and post cash receipts or adjustments against retention balances.

Default contract sales G/L account code
Enter the primary G/L account code you plan to title "contract revenue" (or similar name) in your Spectrum chart of accounts. Be sure to include this G/L account number when you enter your chart of accounts. Enter your default contract sales G/L account even if you do not have General Ledger module installed on your computer.
The software will offer this G/L account code when you add A/R contracts. The software will also use this G/L account code when automatically creating contract entries when jobs are added, but you may override this account code in the Contracts and during Invoice Entry as needed.
If the Validate job division with G/L dept? checkbox is selected in the Job Cost Installation screen, the department of the G/L account code specified here will be overwritten by the division of the job when the A/R contract is created.

Default non-contract sales G/L account code
Enter the primary G/L account code you plan to title "other revenue" (or similar name) in your Spectrum chart of accounts. Be sure to include this G/L account number when you enter your chart of accounts. Enter your default non-contract sales G/L account even if you do not have General Ledger module installed on your computer.
The software will offer this G/L account code when you add A/R invoices that do not reference a contract.

Use deferred retention revenue account?
Select this checkbox to set up a deferred retention revenue account. (This account is usually classified in the liability section of your Balance Sheet.) This checkbox is typically selected for companies that do not want to recognize the retention portion of billings as revenue on the Income Statement at the time of invoicing.
If this checkbox is left clear, invoices updated using Sales Journal Update will be credited the full amount of the revenue to the G/L account code designated on the line detail of the invoice.
If this checkbox is selected, the credit entry will be split across two G/L account codes: the current portion will be credited to the account code specified on the line of the invoice; and the retention portion will be credited to the G/L account code in the contract file.
At the time the retention balance becomes due, a G/L Journal Entry will typically be required to reclassify the amount to the desired revenue account.

Deferred retention revenue G/L account code
This selection only applies if the Use deferred retention revenue account checkbox is selected.
Enter the primary G/L account code you plan to title "retention revenue" (or similar name) in your Spectrum chart of accounts. Be sure to include this G/L account number when you enter your chart of accounts. Enter your retention revenue account even if you do not have General Ledger module installed on your computer.
The software will offer this G/L account code when you enter retention in the Contracts > Properties window, but you may override this account as needed.

Cost Center information
If cost centers are enabled for this company, the following fields will display. If the Allow G/L account overrides by cost center checkbox is selected, the Overrides button is displayed, allowing the Operator to assign override G/L account codes.

Invoice / Credit Memo cost center inter-posting G/L account code
Enter the General Ledger account code to use for posting between invoice/credit cost centers.

Cash Receipts cost center inter-posting G/L account code
Enter the General Ledger account code to use for posting between cash receipts cost centers.
