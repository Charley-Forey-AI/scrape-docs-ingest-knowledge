---
title: "CA DE9C Electronic Export | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/ca-de9c-electronic-export"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/ca-de9c-electronic-export"
---

# CA DE9C Electronic Export

The state of California requires all companies to file their state unemployment taxes electronically.
The 'California DE9C Electronic Export' creates the file per the state of California's specific Quarterly Contribution export requirements. The file which the system creates has the defined name and is stored in the specified location to be used to upload to the State of California's website.
Use this screen to define the specific date ranges, employer details, and the storage location of the file.
For a description of the field names, see [CA DE9C Electronic Export - Field Descriptions](/en/spectrum/spectrum/accounting/payroll/data-entry/ca-de9c-electronic-export/ca-de9c-electronic-export---field-descriptions).

## Start Screen

Spectrum provides access to specific products and modules based on serialization keys. The California DE9C Electronic Export requires a serialization key to access the menu option and to create the export file.Note: Some options on this screen vary based on Modules and other settings defined within your Spectrum application.

## Selections

- From/Through check date – define the check date range that will be used to create the export file.

- This is typically created on a quarterly basis.

- If the From/Thru check date range is not a calendar quarter, a warning error message displays but allows you to continue.

- CA tax table code: define your company's California State Tax Code. A lookup window is provided for selection.

- Wage plan code

- Define the Employee Wage Plan Code (the type of coverage an employee has).

- This is a one-character field defined by the state of California.

- The following characters are allowed S, U, J, L, R, A, or P.

- The field is required.

- For further details on wage plan codes, please refer to the state reporting guidelines.

- Include only confidential company employees?

- This option only displays when using the Confidential Payroll module with the Payroll Installation option defining this company as a Confidential Payroll Company.

- If selected, then the programming displays only employees created in the Confidential Payroll Company's Payroll module.

- If not selected, then the programming displays all employees defined in the Confidential Payroll > Report Companies.

- Check Cost Center

- This option only displays when using the cost center entity logic within the Enterprise Management module.

- Define the Cost group used to submit data for the state.

- Each Entity should have a Cost Group defined to be used for reporting.

-  Export File

- This is the filename for the export defaults as the following:

- [Company code or Cost Group code]-CADE9C-[thru check date] - [system date-time].csv

- Example = 100-CADE9C-09302014-11012014-14:18:10.csv

- The file extension MUST BE .csv to be imported into the EDD website.

## Exporting the File

When the Export button is selected, the export file is downloaded to your local computer or network drive. The path of the exported file depends on the browser used to access Spectrum. The user controls the download path and storage of the exported file by selecting Save file on the download screen.
Export File Layout

- Employee Social Security Number

- Employee First Name

- Employee Middle Initial

- Employee Last Name

- Employee Total Subject Wages

- Employee Personal Income Tax Wages

- Employee Personal Income Tax Withheld

- Wage Plan Code

After the export file is downloaded, the California DE9C Electronic Export start screen for the report displays.

- The Preview button displays the report which is provided for your records and to define the Number of Employees required when submitting the Wage Report for the State of California.

- The Export and My Reports buttons have the same functionality as standard Spectrum report listing screens.

Report Layout

- Employee Code – displays the Employee's Code from Spectrum

- Name – displays the Full name being defined in the file

- Subject Wages – displays the Employee's Gross Wages

- PIT Wages – displays the Net Subject-to Wages

- PIT Withheld – displays the Income Tax Withheld

- Number of Employees per Month

- Displays the number of employees that worked per the state's guidelines.

- Used to enter data on the state's upload screen.

Validation for Report Columns

1. Subject Wages - validates to the QTD Gross column on the Standard Spectrum Unemployment Tax Report by Excess Report type.

1. PIT Wages - validates to the Net Subject to Wages column on the Standard Spectrum Subject-to-Tax Report.

1. PIT Withheld - validates to the Income Tax W/H column on the Standard Spectrum Subject-to-Tax Report.

## Other Information

- The file name is automatically defaulted on the start screen per the predefined definition stated above for your reference.

- [Company code or Cost Group code]-CADE9C-[thru check date] - [system date-time].csv

- Example

- Company Specific = ABC-CADE9C-09302014-11012014-14:18:10.csv

- Cost Group Specific (Entity) = GROUP-CADE9C-09302014-11012014- 14:18:10.csv

- The File MUST have a .csv file extension for the state's upload.

- The export file is stored on your local computer or network drive based on how your download logic is defined.

- The Edit Listing is for your records and to define the Number of Employees per month, which is required when submitting the Wage Report for the State of California.

- If for some reason you need to recreate the file, this process can be repeated.

- The California DE9C Electronic Report creates the .csv file format defined
 by the State of California's Employment Development Department (EDD) for the
 Direct Entry option for the Wage Report as of January 2013. For more
 information, contact the State of California or go to their website and
 review the Payroll Taxes FAQ's for tutorials on filing your returns or visit
 the website [https://www.edd.ca.gov/Payroll_Taxes/FAQs.htm](http://www.edd.ca.gov/Payroll_Taxes/FAQs.htm)

Related information

- [CA DE9C Edit Listing](/en/spectrum/spectrum/accounting/payroll/data-entry/ca-de9c-electronic-export/ca-de9c-edit-listing)
