---
title: "Chart Of Accounts Design | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/general-ledger/gl-accounts/chart-of-accounts-design"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/general-ledger/gl-accounts/chart-of-accounts-design"
---

# Chart Of Accounts Design

Because the GL module allows up to 20 characters for the account code, you should be able to use your existing account code structure, if desired.
If you are considering designing a new chart of accounts, the following are some helpful guidelines.
 Accounts that will be combined on a financial statement should be numbered sequentially to allow ease of formatting wherever possible. For instance, you might have cash accounts 1000, 1010, 1020, and 1030. These can easily be included in one line on a financial statement. Although numbering your accounts in this way makes formatting financial statements easier, you are in no way required to follow these guidelines.
 Although you may use any numbering convention you desire, the following is a typical numbering scheme for each type of account:
 1000s–Assets
 2000s–Liabilities
 3000s–Capital
 4000s–Income
 5000s–Direct Cost of Sales
 6000s–Equipment Expenses
 7000s–Indirect Cost of Sales
 8000s–Administrative Expenses
 If you will be combining two or more companies’ General Ledger information to produce consolidated financial statements, you must use the same chart of accounts for each company. Although you do not have to actually use every account in every company, you must set up like accounts with the same numbers across companies for the amounts to combine in the consolidated company. Most importantly, accounts that are not the same must not share the same account number in differing companies, because it is impossible to separate the amounts in the consolidated company. Accounts that are the same, but have different numbers, will be separate in the consolidated company, but can be left separate or combined on a consolidated statement.
Heading Accounts can be set up to identify a group of accounts, such as Current Assets or Long-Term Liabilities. Typically, heading accounts are numbered so they appear before the group of accounts they define. Heading accounts can help make your General Ledger Trial Balance and other standard reports more readable.If you use masking to print all accounts with a particular numbering convention, the heading accounts will be included as well.
Memo Accounts can be set up to record numbers, such as hours or tons, for use on financial statements. By defining an account as a Memo Account, it will not be included in any standard General Ledger report, but can be printed and/or used in calculations on your financial statements.
 When designing your chart of accounts, you should define only one profit/loss account (type P) for your retained earnings. This account will have a beginning balance for the current year and will be updated each time you close the year. There should not be any posting to this account during the year. If you need a monthly retained earnings balance on any financial statement (such as a monthly balance sheet), it must be done as a calculation on your financial statements.

Related information

- [Use of Subaccounts in Account Structure](/en/vista/vista/accounting/general-ledger/gl-accounts/use-of-subaccounts-in-account-structure)
