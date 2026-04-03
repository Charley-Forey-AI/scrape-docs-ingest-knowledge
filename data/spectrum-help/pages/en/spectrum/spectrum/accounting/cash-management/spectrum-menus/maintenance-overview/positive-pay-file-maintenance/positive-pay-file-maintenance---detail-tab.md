---
title: "Positive Pay File Maintenance - Detail tab | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/maintenance-overview/positive-pay-file-maintenance/positive-pay-file-maintenance---detail-tab"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/maintenance-overview/positive-pay-file-maintenance/positive-pay-file-maintenance---detail-tab"
---

# Positive Pay File Maintenance - Detail tab

Use the Detail tab to review file format variables accessible for the export file and all corresponding file information. These variables come from the check reconciliation file (BR.CHK), the bank account file (BR.ACCT) and the company info file (PA.INFO). Individual variables such as check number, check amount, check date and so forth can be selected. In addition, constants and multiple variable strings are also available.
Field
Description

Variable type
Select the variable type from the available drop-down list box.

-  If Single is selected, the Search File Variables window opens and displays all of the available variables in Payroll.

- If Multiple is selected, the Concatenate Multiple Variables window displays. Use this window to combine the information from several fields into one field. For example, you might want to combine the City, State, and Zip fields into one concatenated "address" field.

- If Constant is selected, special plan numbers or other company information that is constant for all employees will be used.

For Single variables, certain files offer different selections and selection type fields:
PR.INCTX, PR.STHIS Type = Federal (0), State (1), County (2), Local (3), and Blank (ALL) Selection = Tax table code
PR.VDCTL, PR.EHVD Type = Add-on/deduction code, Category group Selection = Code or group, as determined by Type
PR.WCCTL, PR.WCHIS Type = N/A Selection = Worker's comp code

- Click the New button to add a new variable record at the end of the list.

- Click the Insert button to add a new variable record prior to the currently selected line.

Description
If the Single or Multiple variable type was selected, the variable description will display in this field.
If the Constant variable type is selected, enter a description for the variable type.

Type
The file type defaults from the database. File types include (A)lphanumeric, (N)umeric, (D)ate, and (K)ey.

Length
The length (number of characters) of the variable displays. This can either be the length in the database, or it can be defined here if the variable type is Constant or Multiple.

Justification
Select the justification type from the drop-down list box: Default, Left or Right.

Fill
If the file type is Numeric and right-justified, enter (Z)ero to fill the leading spaces with zeros, or leave the fill type blank if you want the leading spaces to appear blank.
You can also choose the character that will display for non-existent dates; for example, if you selected the character 0, the date would display as 00/00/0000, according to the display mask.

Display format
Use this field to determine a combination of mask characters (up to 20 characters).
Numbers, with the exception of #RECORDS, display by default as whole pennies with the decimal point assumed. For example, the check amount $123.45 would by default appear as "12345" in the export file. You can override this default as needed.

Alternate field
Additional line transaction information, including the file codes and corresponding descriptions will display to the right of this field, if available.
