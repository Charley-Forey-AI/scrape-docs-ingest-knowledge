---
title: "Field Definitions: GL Initialize Budgets Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/general-ledger/gl-budgets/about-the-gl-initialize-budgets-form/field-definitions-gl-initialize-budgets-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/general-ledger/gl-budgets/about-the-gl-initialize-budgets-form/field-definitions-gl-initialize-budgets-form"
---

# Field Definitions: GL Initialize Budgets Form

The following is a list of field descriptions for the GL
 Initialize Budgets form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Fiscal Year End

 Enter the calendar month/year of the fiscal year ending for which to initialize this budget.
 If you accessed this form by selecting the Initialize Budgets option from the File menu of GL Budgets, this field defaults the currently selected fiscal year. May be overridden.

##  Budget Code

 Enter the Budget Code (from Budget Codes Maintenance) to initialize.
 If you accessed this form by selecting the Initialize Budgets option from the File menu of GL Budgets, this field defaults the currently selected budget code. May be overridden.

##  GL Account Mask

 Enter the desired GL Account code mask. Only accounts corresponding to this mask will be initialized for this budget.
 If you accessed this form by selecting the Initialize Budgets option from the File menu of GL Budgets, this field defaults the currently selected GL account. May be overridden.

##  Based On:

Existing Data – Select this option to initialize budgets based on existing account balances or budget amounts.
Selected Amounts – Select this option to initialize budgets based on specific amounts defined by time frame (monthly, quarterly, or annual).

##  Existing Data

Actuals – Select this option to base the new budget on the actual balances of the fiscal year specified below. All accounts except inactive and heading accounts will be initialized
Budgets – Select this option to base the new budget on existing budget amounts for a specified fiscal year end and budget. Only accounts with existing budgets for the fiscal year ending (specified below) will be initialized.

##  Existing Data: Fiscal Year Ending

The Fiscal Year Ending field on the GL Initialize Budgets, Info tab, Existing Data section.
 For budgets based on actual account balances or another budget code, enter the appropriate fiscal year ending month/year.

##  Existing Data: Budget Code

The Budget Code field on the GL Initialize Budgets, Info tab, Existing Data section.
 The field is enabled when the Budgets option is selected in the Existing Data section.
Enter the budget code on which to base the new budget you are creating.

##  Modify By

Percent — Select this option to modify budget amounts by a percentage (specified to the right).
Amount — Select this option to modify budget amounts by a fixed amount (specified to the right).

##  Percent

 Enter the percentage by which to modify the budget amount during initialization.

##  Amount

 Enter the flat amount by which to modify the budget amount during initialization. (Important: The amount you enter will adjust the accounts’ budgeted amount according to its normal balance. For example, if you want to increase a credit amount, then enter a positive amount.)

##  Selected Amounts

- Month – Select this option to initialize the budget based on a monthly amount. When selected, a Monthly Amount input is displayed below, allowing you to specify the monthly budget amount.

- Quarter – Select this option to initialize the budget based on quarterly amounts. When selected, quarterly inputs are displayed below, allowing you to specify a budget amount for each quarter.

- Annual – Select this option to initialize the budget based on an annual amount. When selected, an Annual Amount input is displayed below, allowing you to specify the annual budget amount.

##  Monthly Amount

 Enabled only when initializing budgets using the Month option.
 Specify the budget amount to initialize to each month in the specified fiscal year.

##  First Quarter

 Enabled only when initializing budgets using the Quarter option.
 Specify the budget amount for the first quarter. Keep in mind that when initialized, this amount will be divided equally among the months in the first quarter. (For example, if you specify 500,000.00 for the quarter, each of the months in the quarter will be budgeted for 166,667.00.)

##  Second Quarter

 Enabled only when initializing budgets using the Quarter option.
 Specify the budget amount for the second quarter. Keep in mind that when initialized, this amount will be divided equally among the months in the second quarter. (For example, if you specify 500,000.00 for the quarter, each of the months in the quarter will be budgeted for 166,667.00.)

##  Third Quarter

 Enabled only when initializing budgets using the Quarter option.
 Specify the budget amount for the third quarter. Keep in mind that when initialized, this amount will be divided equally among the months in the third quarter. (For example, if you specify 500,000.00 for the quarter, each of the months in the quarter will be budgeted for 166,667.00.)

##  Fourth Quarter

 Enabled only when initializing budgets using the Quarter option.
 Specify the budget amount for the fourth quarter. Keep in mind that when initialized, this amount will be divided equally among the months in the fourth quarter. (For example, if you specify 500,000.00 for the quarter, each of the months in the quarter will be budgeted for 166,667.00.)

##  Annual Amount

 Enabled only when initializing budgets using the Annual option.
 Specify the budget amount for the entire year. When initialized, this amount is divided equally among all 12 months of the year. (For example, if you specify 1,500,000.00 for the annual budget amount, each monthly budget amount will be 125,000.00.)

##  Selected Amounts: Dr/Cr

 For the specified monthly, quarter, or annual amount (depending on the selected budget time frame), indicate whether the amount is a debit (Dr) or credit (Cr).

## Initialize Budget Notes

Check this box to initialize budget notes. During initialization, all budget notes existing for the source budget will be copied to the new budget.
Leave this box unchecked to exclude budget notes when initializing the new budget. Budget notes from the source budget will not be copied to the new budget.
