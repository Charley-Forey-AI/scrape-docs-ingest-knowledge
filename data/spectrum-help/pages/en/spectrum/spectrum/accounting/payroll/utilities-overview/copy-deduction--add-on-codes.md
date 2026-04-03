---
title: "Copy Deduction & Add-on Codes | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/utilities-overview/copy-deduction--add-on-codes"
fetched_at: "2026-04-03T20:47:07.463050+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/utilities-overview/copy-deduction--add-on-codes"
---

# Copy Deduction & Add-on Codes

Use this screen to set up one standard set of codes for one company or several companies.
To copy a set of deduction codes within a company, make certain that the company entered in the Copy to Company field is the same as the company displayed in the Copy from Company field. For example, assume you have a garnishment code G1 and you now want to make garnishment codes G2 and G3. Use this function to create these additional codes.
To set up a standard set of codes across companies, make certain that
 the destination company(s) entered in the Copy to Company field are different from the original company. If you
 attempt to set up new deduction or add-on codes and the software finds that the G/L account
 code fields contain an invalid G/L account for the destination company, or the vendor code
 is not set up in the destination company, then an exception dialog box will display.
 Preview or print the report to see where the error(s) occurred. Invoice approval defaults
 can be copied within the same company, but they cannot be copied to a different company.
 When an invalid vendor code is encountered, the software will still copy the code to the
 destination company, but the vendor code field will appear blank in the destination company
 deduction file.
Any rate per limit Worker Compensation tax codes that are flagged in the Deduction / Add-on Code Maintenance > Tax Effects screen will be included when the update is performed.
This screen is only available if you have Enterprise Management security
 access (security category EM), and you must have security access to add codes manually into
 Deduction & Add-on Code Maintenance. In addition, if you do
 not have security access to the Payroll module in this company, or if your security level
 is lower than the function's security level, then the new code will not be added.
