---
title: "About Setting the Calculation Category for D/L Codes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/about-setting-the-calculation-category-for-dl-codes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/about-setting-the-calculation-category-for-dl-codes"
---

# About Setting the Calculation Category for
 D/L Codes

When creating deduction and liability codes (PR
 Deductions/Liabilities) , the calculation category determines the type of
 calculation that occurs during processing.
Use the Calculation Category
 field to determine the category. Once you have finished creating
 deduction/liability codes, you must assign them to the corresponding PR
 forms for automatic calculation.
The following table identifies all calculation categories and the PR forms used for registering the codes.
Calculation Category
Registering Form

Federal
PR Federal Info

State
PR State Information

Local
PR Local Codes

Insurance
PR Insurance Codes

Craft
PR Crafts or PR Craft Classes

Employee
PR Employees or PR Employee Dedns/Liabs

Any
All of the above forms

Note: If you assign a code to an inappropriate form (e.g., registering a State deduction code in PR Federal Info), the system displays an error during processing. However, you may assign a deduction code with the Any category to any of the above mentioned PR forms. However, if you register the code with more than one form, the system may duplicate the calculation.

## Setting the Federal
 Type (US users only)

If you select Federal from the Calculation Category drop-down, you must also
 identify the type of federal deduction or liability in the
 Federal Type
 drop-down. The following options are available: Withholding, FUTA,
 Social Security, and Medicare. When assigning a federal type, you
 can break down amount when making Federal tax payment via EFT.
If you checked the
 Automatic Update to
 Accounts Payable box (Addl Info tab) and the
 vendor's addenda type is set to Tax Payment
 (Addenda Type
 field, AP Vendors, EFT tab), the system creates one addenda tax
 payment record and distributes it to the appropriate addenda field
 for the transaction.

Related information

- [Create Deduction and Liability Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/create-deduction-and-liability-codes)
