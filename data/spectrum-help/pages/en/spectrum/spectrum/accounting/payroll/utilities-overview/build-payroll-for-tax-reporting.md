---
title: "Build Payroll for Tax Reporting | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/utilities-overview/build-payroll-for-tax-reporting"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/utilities-overview/build-payroll-for-tax-reporting"
---

# Build Payroll for Tax Reporting

This utility is provided for new Spectrum users in order to
 facilitate the entry of employee year-to-date earnings and tax information.
This process involves two primary steps:

- Import of a comma-delimited text file, and

- Running an Update to store the information in Payroll history and adjust the employee year-to-date balances.

The software performs extensive error checking. In the event that a data error is encountered during the import process, the software will provide a detailed Exceptions Report instead of continuing with the import.

## 1. Import Payroll Taxes from Text File

To begin, click the Import button. The Import file will contain a series of comma-delimited files (see rules below). The first character on the line will represent the Record ID (Header, Tax, Worker's compensation, Deduction or Add-on. The remaining fields will vary by Record ID.

- The Header Record ID must precede the rest of the records for the given "Entity + Employee code". All Header records may be grouped at the beginning of the file or may be interspersed throughout the file, as long as the Tax, Worker's compensation, Deduction or Add-on records for the given employee follow his or her Header record.

- Please note that the software will ignore all lines with an invalid or <blank> Record ID. This allows you to conveniently use 'column headings' within the Spreadsheet if desired.

- If you have time cards for unions and non-unions, you will need to import these time cards in two separate batches--one for time cards with unions, and the other for time cards without unions (when the Union option is not selected in PR Installation).

- The system will check for errors. If an error is found, you will be directed to print the Exceptions Listing for more information.

## View rules for comma-delimited files

Follow these rules when creating a spreadsheet with historical payroll data and save it as a comma-delimited (CSV) file.
RULE: The first character on the line represents the type of record being imported. The software will ignore all lines with an invalid or <BLANK> Record ID in the first column. This was done to allow you to add your own column headings as desired in the spreadsheet.
RULE: With the exception of the Header and Tax Record ID's, the import file does not require the other Record ID's exist in the import file.
RULE: The Header Record ID must precede the rest of the records for the given 'Entity + Employee code'. All other Record ID's can appear in the file in any order.
RULE: The Tax Record ID for Federal must exist for every employee in the import file, but actual tax amounts are not required.
At a minimum, the file must include a Tax Record ID of 'T' and contain valid information in the Employee Code, the federal Tax Code, and Jurisdiction Type 'F' columns.

## 2. Run the Update

Click Continue to load the information into Payroll. This update will post earnings and tax information to Payroll History and will adjust employee year-to-date totals.
The following rules are used when writing to the historical payroll tables. It is important to understand these assumptions so you can best utilize this tool.

## View rules concerning the update

RULE: As this feature is intended to be used for conversions, the update will populate the 'Check Date' and 'Period End Date' from the import file's 'End Date' column.
RULE: These will be imported as manual checks.
RULE: The update will automatically assign check numbers that start with the letter 'T'. The number will use the 'Next auto-deposit check number' counter from the Payroll Installation screen. Even though we are using the auto-deposit counter, we are not using the actual 'E' check number. This means that we are not "burning" an 'E' check number.
RULE: The update will classify gross earnings using the 'SA' Special Amounts pay type. This is similar to how we manually convert payroll.
RULE: The 'Total Hours' from the import file will be classified using the 'U' Unpaid pay type.
When recording hours for ACA purposes, remember that the 'U'npaid pay type can be included in the Average Hours Report.
RULE: The update will populate the tax code's 'Gross Wages' column with its 'Subject to Wages'.
This means that only for records processed with this feature, the user will not be able to calculate gross to subject to on the Subject To Tax Report. This is an acceptable limitation as "gross" in Spectrum has limited meaning. This decision was made because attempting to calculate gross wages has too many rules and unknown exceptions to be 100% correct.
RULE: The update will populate the workers comp 'Total Earnings' and 'Covered Earnings' columns with the workers comp 'Subject To Earnings' column amount.
RULE: The update will calculate the workers comp rate per $100 by taking the 'Burden' column divided by the 'Subject to Earnings' column multiplied by 100.00.
RULE: The system
 will calculate the employee count based on the number of unique employee codes present.
 For cost center entity users, this calculation counts each employee just once, even if
 you have tax reporting information in process for multiple entities.
Best practice: do not void 'T'
 checks. If you want to void a 'T' check, create an import that reverses
 the check you want to void.
Because the Build Payroll feature does not write to Cash Management, it is not possible to void the check through the time entry screens.
Optional step: Review the Payroll Taxes Register:
Before clicking Continue to run the update, you can click the Payroll Taxes Register button to review unposted tax information. Balance this report back to the legacy system before importing the data into Spectrum.
View sample report
The Other Taxes column includes all state, county and local withholdings. It also includes any employee paid SDI and Workers Comp.
For Canadian systems, the FICA column displays CPP. EI is contained within the Other Taxes column.
