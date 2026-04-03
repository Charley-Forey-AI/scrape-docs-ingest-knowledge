---
title: "New/Edit Account - Details tab | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/maintenance-overview/account-code-file-maintenance/newedit-account---details-tab"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/maintenance-overview/account-code-file-maintenance/newedit-account---details-tab"
---

# New/Edit Account - Details tab

Use the Details tab to enter settings and defaults for the account.
The fields on this tab vary depending on the account type selected on the [Account Code File Maintenance](/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/maintenance-overview/account-code-file-maintenance) screen. If applicable, this tab provides a list of sub-account cards tracked for this credit card.
Important: Because credit card account codes and card numbers display on posting reports, it is strongly recommended that you do not use the entire account code and credit card number when creating these codes. Instead, it is recommended that you enter the last four, five, or six digits of the account number or use the employee's initials with the last 4 credit card numbers. It is important to use a scheme that will not compromise the actual card numbers. For example, Credit Card Account BOA1234 with Card Number AEO1234 would help prevent fraudulent credit card use.

## Account Type: Bank

If the account you've selected is a bank account, these fields display on the Details tab:
FieldDescription
Cash G/L accountEnter the cash General Ledger account code associated with this account. Note: Entry is prevented when the account code status is set to Not used. A warning displays when the status is set to Inactive.

Clearing data file formatEnter the data file format code associated with this account.
Positive pay file formatEnter the positive pay file format code for this bank account. This code's value will default in Positive Pay File Table Import / Export.
Last check #The software is prompting for the last check number issued for this bank account. If you are already using the Cash Management module, the most recently used check number is displayed, and can be changed if desired. The number is updated automatically as part of payment processing, and will then be used to offer the next higher number as a default the next time you issue checks.
If you are now setting up a new bank account, enter check number 1. The first time you issue checks, the software will default from this field during payment processing, but you will override it with the correct next check number to be issued. From then on, this field will reflect your actual last check number.

Last wire transfer #Enter the last wire transfer number that was used.
Separate check sequence for manual checks?The software is prompting whether you plan to use different check stock for handwritten and computer-generated checks. If you have a separate manual check stock, then this field should be set to Y(es) so the last manual check number will be stored. During Manual Check Entry and pre-paid check entry in A/P Invoice/Create Memo Entry, if this field is set to N(o) the default check number will be provided based on the check number above for both computer-generated and manual checks.
If it is set to Y, the check number for manual entries will default from below. This field should be set to N if you will use the same A/P check stock regardless of whether it is hand-written or printed by the computer during payment processing.
Some new users may have a large supply of unused checks on hand at conversion. While the check format may not be compatible for Spectrum-generated checks, this stock might be useful for manual checks. In this circumstance, the office might set this prompt to Y until the old check stock is exhausted. Thereafter, this prompt can be reset to N.

Last manual check #The software is prompting for the last manual check number issued. If you are already using Cash Management module and the Separate check # for manual checks prompt is set to Y, the most recently used manual check number is displayed, and can be changed if desired. The number is updated automatically as part Manual Check Entry and pre-paid check entry in A/P Invoice/Create Memo Entry, and will then be used to offer the next higher number as a default the next time you issue a manual check.
If you are now setting up a new bank account and will be maintaining separate stock for computer-generated and hand-written checks, enter check number 1. The first time you record a manual check, the software will default from this field during entry, but you will override it with the correct check number issued. From then on, this field will reflect your actual last manual check number used.

Post 'H' for manual (hand) checks?Decide whether to update Accounts Payable payment records with a preceding H designation (for hand check) as part of the check number. If this checkbox is selected, the manual check number will be recorded throughout Spectrum files. For example, as "H12345"; if this checkbox is left clear, the same check would have been stored as "12345". The H is system-generated during posting; the user enters "12345" in either scenario, but this checkbox will determine whether the H is included when updated.
Some users prefer to include the H in the check number in order to identify manual checks at a glance. In reviewing payment records, system-generated checks can be easily distinguished from hand-written checks, and there is a possibility the stored information for the manual check may differ from the actual document. Other users prefer to omit the H for consistency of check numbering; when the H is eliminated, all checks sort sequentially rather than with manual checks at the end.

## Account Type: Credit Card

If the account you've selected is a credit card, these fields display on the Details tab:
FieldDescription
Credit card liability G/L accountAdd or enter the credit card General Ledger account code associated with this credit card account.
 Note: Entry is prevented when the account code status is set to Not used. A warning displays when the status is set to Inactive.

Last transaction sequence #The software is prompting for the last credit card transaction sequence number for this credit card account. If you are already using the Cash Management module, the most recently used sequence number displays and can be changed if desired. The number is updated automatically as part of payment processing and will then be used to offer the next higher number as a default the next time the credit card is used.
If you are now setting up a new credit card account, press Enter to accept the software default. The first time you record a credit card charge, the software will default from this field during payment processing, but you will override it with the correct transaction number. From then on, this field will reflect your actual last transaction number.

Track sub-account card detail?Select this checkbox if multiple credit cards are associated with this credit card account; otherwise, leave this checkbox clear.
This feature is particularly convenient if multiple people within your company. For example, each VP, the HR department, and the IT Manager all have credit cards that are associated with one credit card account.

CardsIf the Track sub-account card detail checkbox is selected, sub-account cards tracked for the credit card are listed below. Use the buttons given to add a new card or to edit or delete an existing card.
