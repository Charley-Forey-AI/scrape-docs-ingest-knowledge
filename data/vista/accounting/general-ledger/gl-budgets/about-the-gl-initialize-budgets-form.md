---
title: "About the GL Initialize Budgets Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/general-ledger/gl-budgets/about-the-gl-initialize-budgets-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/general-ledger/gl-budgets/about-the-gl-initialize-budgets-form"
---

# About the GL Initialize Budgets Form

Use the GL Initialize Budgets form to create and set up budgets for any budget code/fiscal year.
 You can access the GL Initialize Budgets form directly from the main menu or from the GL Budgets form by selecting File > Initialize Budgets.
Once you specify which budget code, fiscal year, and account code(s) you wish to set up, you must specify whether to use existing data or selected amounts.

## Initializing Based on Existing Data

If you are initializing based on
 existing data, you must indicate whether to base the initialization on actual GL
 account balances or on another budget code, and whether to modify the budgets by a
 certain percentage or amount.

- Actuals –
 Select this option to initialize based on actual account balances. All
 accounts except inactive and heading accounts will be initialized.

- Budgets –
 Select this option to initialize based on existing budget amounts. Only
 accounts with existing budgets for the specified 'based on' Fiscal Year
 Ending will be initialized. Beginning balances will be initialized for each
 GL account as applicable.

Note: If you specify a flat amount by which to modify
 the budget amount during initialization, the amount that you enter will adjust the
 account’s budgeted amount according to its normal balance. For example, if you want
 to increase a credit amount, then enter a positive amount. Similarly, enter a
 negative amount to decrease a credit amount.

## Initializing Based on Selected Amounts

If you choose to initialize based on
 selected amounts, the inputs will differ than those used when initializing based on
 existing data. Instead, you will have the option to initialize based on a selected
 time frame (i.e. Month, Quarter, or Annual), a specified amount, and Dr/Cr value.

- Month –
 If you select this option, you will need to specify a monthly amount, which
 will be applied to each month on the form. If you need to change certain
 months, you can edit them manually in the desired months.

- Quarter –
 If you select this option, additional inputs will display for entering
 amounts for each quarter. The quarterly amounts will be used to calculate
 the monthly amounts. If you need to change certain months, you can edit them
 manually.

- Annual –
 If you select this option, you will need to specify an annual amount. This
 amount will be used to calculate the monthly amounts. If you need to change
 certain months, you can edit them manually.

Once you specify the initialization
 criteria, click Initialize. If initializing an account with an existing
 budget, be aware that initialization will overwrite the existing budget amounts.

After you complete the initialization process, you can maintain/edit your budget using the GL Budgets form.
