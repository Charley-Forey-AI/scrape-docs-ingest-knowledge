---
title: "Use of Subaccounts in Account Structure | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/general-ledger/gl-accounts/use-of-subaccounts-in-account-structure"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/general-ledger/gl-accounts/use-of-subaccounts-in-account-structure"
---

#  Use of Subaccounts in Account Structure

Embedding subaccounts into your chart of accounts structure has specific implications in financial statements creating using Management Reporter (component of Performance Point Server 2007).

- Subaccounts – These are GL accounts that have additional numbers at the end of natural account. They do not carry the same meaning through all GL accounts. If subaccounts are used, they will need to be in the second section of a GL format, next to the main GL number.

For example, GL uses subaccounts, but does not use divisions or profit centers. A format of ‘4R.2RN’ would be seen with a GL Account of 1000.01—with the ‘.01’ section representing the AP checking account. If the natural inventory account is ‘1200’, and the you have different inventory accounts for Warehouse inventory (1200.01) and North Slope’s inventory (1200.02), the second parts (.01 and .02) can have different meanings depending on the account to which they are attached.

- Division or Profit Center - These are used to post Expense and Income into a Profit and Loss (P&L) statement by division. The division number would have the same meaning regardless of the natural account it is attached to. For example, you might use 5100.01 to post Labor expenses to a job in a concrete division. The second part, ‘.01’, represents the concrete division or profit center.

 In Vista™ software, we must indicate the parts that are being used as subaccounts. This helps translate the meaning of the GL account structure to Management Reporter. If your GL account includes a main (or natural) account, subaccount, and a division, then your GL structure might be 4R.1R.2RN. The 4R would be the main account, the 1R would be the subaccount, and the 2RN would be the division or profit center. The subaccount must be placed next to the main account because Management Reporter will list this as 6R.2RN. The 6R includes the 4-digit main account, the period separator, and the 1-digit subaccount, and the 2RN would be the division or profit center.
 The following describes how your GL account code format relates to Management Reporter.

## Subaccounts vs. Division or Profit Center

 The ‘Main GL Code’ is the first section of a GL account code. Without subaccounts, the main GL code describes the GL account. With subaccounts, the main account is not used for anything; it cannot be described by itself and has no functionality in Management Reporter.
 In Management Reporter, the ‘Natural GL Code’ is the first section of the GL account code and describes the GL account.Without subaccounts, the natural and the main GL accounts are exactly the same. When using subaccounts, the first section includes the account number and the subaccount number. For example: 5000.01 is the natural GL account code.
 In Vista software, if you are using subaccounts (as defined in GL Account Parts), Part 1 will be defined as the natural GL account code. If you are not using subaccounts, Part 1 will be defined as the main GL account code.
Table 1. Example 1DescriptionWithout SubaccountsGL Account Part Entries Without SubaccountsWith SubaccountsGL Account Part Entries With Subaccounts
 Full Account
 1000.0302
 n/a

 1000.01.0302

 Natural GL Code
 1000
 Part 1: 1000 Cash

 1000.01
 Part 1: 1000.01 Cash

Profit Center
 03
 Part 2: 03 Oregon

 03
 Part 2: 03Oregon

 Department
 02
 Part 3: 02 Hiway

 02
 Part 3: 02Hiway

Note: You do not describe 1000 in any table when using a subaccount. The base, natural, or main GL number is 1000.01; to combine all 1000 accounts in Management Reporter, wildcards would be used (1000.&&).
Table 2. Example 2DescriptionWithout SubaccountsGL Account Part Entries Without SubaccountsWith SubaccountsGL Account Part Entries With Subaccounts
 Full Account
 5000.0302
 n/a

 5000.01.0302

 Natural GL Code
 5000
 Part 1: 5000 Expense

 5000.01
 Part 1: 5000.01 Expense

Profit Center
 03
 Part 2: 03 Oregon

 03
 Part 2: 03Oregon

 Department
 02
 Part 3: 02 Highway

 02
 Part 3: 02 Highway

Note: You do not describe 5000 in any table when using a subaccount. The base, natural, or main GL number in this example is 5000.01; to combine all 5000 accounts in Management Reporter wildcards would be used (5000.&&).
