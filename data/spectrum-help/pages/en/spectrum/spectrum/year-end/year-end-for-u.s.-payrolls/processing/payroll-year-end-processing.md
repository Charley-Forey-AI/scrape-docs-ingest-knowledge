---
title: "Payroll Year-end Processing | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/year-end/year-end-for-u.s.-payrolls/processing/payroll-year-end-processing"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/year-end/year-end-for-u.s.-payrolls/processing/payroll-year-end-processing"
---

# Payroll Year-end Processing

This topic walks through the different Spectrum functions you will use for year-end processing of U.S. payrolls.
These functions are available through System Administration > Year End > Year End Processing > Payroll, or through the Payroll module.

## Cost Center Security Information

If cost centers are being used in the current company, only employees that the operator has security authorization to access are available.
If entity tracking is enabled in the current company, employee W-2 records display based on whether the operator has authorization for the assigned entity. If at least one authorized cost center is assigned to the specified entity code, all W-2s for that entity display.

## Payroll Reports

We recommend running and saving/archiving the following reports. They are available through Payroll > Reports or System Administration > Year End > Year End Processing > Payroll.

- Quarterly Federal Tax

- Unemployment Tax

- State, County & Local Tax – also called Subject-to-Tax

- State Disability Insurance

- Worker's Comp Rate/$100

- Worker's Comp Rate/Hour

- State History – also called Wage and Tax History

- Earnings History – also called Employee Earnings History

- Liabilities Reconciliation – available only at Payroll > Reports.

## W-2 Form Maintenance

The W-2 Form Maintenance screen is used to add or edit information produced by the Build W-2 Forms function. It is also the landing page for all W-2 and W-3 processing functions: Build, Print, Listing, and Export.

- Enter numeric fields in dollars and cents (up to $99 million); cannot be negative.

- Do not enter dollar signs ($) or commas. Use a decimal point even if the amount is an even dollar amount.

- If needed, refer to the [field descriptions in the Spectrum online Help](/en/spectrum/spectrum/accounting/payroll/period-end-procedures/w-2-form-maintenance/w-2-form-maintenance---field-descriptions).

## Build W-2 Forms

Use this screen to update W-2 information. Up to 360 forms per employee are supported. The Build W-2 Forms screen clears the W-2 file and calculates W-2 information based on the payroll earnings history file.

Unless the Write 1 state & locality per W-2? checkbox is selected, each form contains up to two localities. Even if it is selected, Federal information appears only on Form 1 for each employee. If you are processing W-2 forms through Nelco, and you have multi-state filings to make, please leave this checkbox clear.

## Separate W-2s by Entity

If entity tracking is enabled for the current company in the Enterprise Installation screen, the W-2 build will break employee earnings onto separate W-2 Forms based on 'Entity code' stored in the Payroll Check History Table. The software will first look to find the particular state or locality's tax code for the entity code and if found, will then look for whether it has an assigned Payer tax ID number. If the state or locality does not have a tax code present, the taxpayer ID will be assigned from the tax table.
For step-by-step instructions on this screen, refer to the field descriptions at [Build W-2 Forms](/en/spectrum/spectrum/year-end/year-end-for-u.s.-payrolls/processing/year-end-processing-screen-u.s./build-w-2-forms).

## Print W-2 Forms

Use this screen to Print W-2s. It's available in two locations:

- Payroll > Period End > W-2 ProcessingPrint W-2

- System Administration > Year End > Year End Processing > Payroll > W-2 Processing > Print W-2

If W-2s need to be grouped by state when printing, use the Tax table code field to specify a state.

Each year, before W-2 forms are loaded into the printer, we recommend the following:

- Print one W-2 on plain paper to confirm the correct printer destination.

- After printing a W-2 on plain paper, use it to check the alignment of the values with the form. If the W-2 values do not align with the form, please try the following:

- Use the Actual size print option (no scaling).

- Select Export in the print selection screen (instead of preview) and print to Acrobat (PDF) or Crystal Report Viewer (RPT).

- Try another browser to print from (if using Chrome, try Firefox and vice versa).

- Try scaling the print one or more percentage points in either direction.

- Use a different printer.

- Export the final W-2 print to .PDF format and save it in a read-only, year-specific folder on your server or workstation. This will allow you to reprint the W-2 in the future, if necessary.

For step-by-step instructions on this screen, refer to the field descriptions at [Print W-2 Forms](/en/spectrum/spectrum/year-end/year-end-for-u.s.-payrolls/processing/year-end-processing-screen-u.s./print-w-2-forms).

## Print W-3 Forms

Use this screen to print the W-3 Transmittal of Wage and Tax Statements form, which is a required form when filing W-2s. Please refer to the IRS instructions on filing forms W-2 and W-3 for detail on SSA requirements.

Per Social Security Administration (SSA) regulations, the W-3 form is a Federal form not intended for use as a "state" totals page. Please go to W-2 Form Maintenance screen, select the Listing button, select Totals only?, enter the state code in the Tax table code field, and use that print-out for state purposes.

- Box 12a of the W-3 form sums Box 12 figures of the W-2 forms for code letters D, E, F, G, H, S, Y, AA, and BB.

- Box 12 code DD is for the Cost of employer-sponsored health coverage, and code EE is for Designated Roth contributions under a governmental section 457(b) plan.

- See [Print W-3 Forms - Field Descriptions](/en/spectrum/spectrum/accounting/payroll/period-end-procedures/w-2-form-maintenance/print-w-3-forms/print-w-3-forms---field-descriptions) for more detailed information.

## Export W-2 File

Use this screen to prepare W-2 electronic files. There are two electronic file types that can be created from this screen:

- One conforms to the federal electronic EFW2 format.

- One is a comma-delimited file, in a format used by Nelco, a 3rd party processor of W-2s.

Backup W-2 Records to History
Use the Backup option on the W-2 Processing screen to save W-2 information into a new history database table. This process is available before or after the electronic files and printing of forms takes place. While it can be run multiple times, only the latest version is saved.
EFW2 Format File for Federal Filing
To create the EFW2 format file for Federal W-2 filing:

1. Complete and review the screen selections. For step-by-step instructions, see [Export W-2 File and Nelco State Tax Filing - Field Descriptions](/en/spectrum/spectrum/accounting/payroll/period-end-procedures/w-2-form-maintenance/export-w-2-file-and-nelco-state-tax-filing/export-w-2-file-and-nelco-state-tax-filing---field-descriptions).

1. For Federal submittal, leave Tax table field set to ALL.

1. Select Continue. A pop-up appears in which you can enter an alternate file name for the export (the file name default is W2REPORT).

1. Select the Continue button on the pop-up. The download settings for your browser and / or workstation will determine where the EFW2 format file is saved or how it is opened. If you have questions about this, contact your company IT department.

1. After the EFW2 format file has been created, use Notepad or Notepad++ to confirm the W-2 information has been created.Tip:Spectrum includes data validations on the Nelco export that are not part of the EFW2 file creation, such as addresses, SSNs, and names on the W-2 Employee records. To do this, select the Nelco CSV button before selecting the Continue button on the Export W-2 file screen. After you've corrected any errors, and the Nelco CSV validation is clean, then select the Continue button, and create an EFW2 record with cleaner data.

1. To further validate the contents of the electronic file, the Social Security Administration offers [AccuWage Online](https://www.ssa.gov/employer/accuwage/index.html).Note: All Address fields must be completed, even if the same address is used more than once, or you will receive an error message when you run your AccuWage test.

1. Enter information as needed in each field. Refer to the message line at the bottom of the screen and IRS or SSA documentation for assistance.

Supplemental Instructions for State filing with the EFW2
Spectrum's W-2 export includes the standard, required EFW2 fields. Many states require additional fields, which are not supported by Spectrum's W-2 export. Please see the [Appendix](/en/spectrum/spectrum/year-end/year-end-for-u.s.-payrolls/state-w-2-electronic-file-requirements) for a list of states which have additional requirements for electronic filing.
There are several options to create an electronic file that meets these states' non-standard requirements:

- Using Notepad or Notepad++, manually modify the EFW2 file you created using Spectrum. Note: Support cannot assist with modifying EFW2 files.

- Contract with Viewpoint's Professional Services or Technical Services to create a state-specific EFW2 file.

- Contract with Nelco to generate the W-2's.

- To create a state-specific electronic file, enter the tax table code for the state in the Tax table field, and fill in the Tax ID and FIPS code on the screen, before selecting the Continue button. Important: The file name always defaults to "W2REPORT." Create separate locations to save the Federal and each individual state file, or be very careful to rename each file upon saving. Unless you save to a different location or use a different file name, each new electronic file will overwrite a previous one.

## Viewpoint Partners with Nelco to Support W-2 Filing

Your Spectrum application can create a comma delimited (.csv) file for uploading to the Nelco site to process W-2s.
If you want to file using Nelco, and if you haven't already, you'll need to [Create an account at our partner site](https://spectrum.nelcoportal.com/Account/CreateUser) where you'll be prompted to enter general info (name, address, email) about your company. Note: Nelco has special Viewpoint customer pricing for processing W-2s. Please contact Nelco at 1-800-266-4669 for more information.

After carefully filling out the Export W-2 file screen, select the Nelco CSV button. After validating and and making any necessary corrections, the system prompts you to save the file (or open it, based on the download and save settings on your workstation). Tip: If you choose to open the file, use Notepad or Notepad++, as Excel removes leading zeros unless you take steps to prevent it.

Important: If you are using Nelco to file W-2s, you must enter the State ID in an exact format. Please see the Appendix for a document with State ID format requirements, or contact the taxing agency of each state in question. The State ID should be verified prior to building W-2s. To correct the State Tax ID, enter it at Payroll > Maintenance > Tax Tables and then return to the W-2 Maintenance page and perform the Update State ID utility.
Complete and review the screen selections, paying special attention to the tax year selection.
To upload your file to Nelco:

1. Select the Nelco CSV button. The Export to Nelco CSV Format information window displays.

1. Select Continue.

1. A second information window displays letting you know if the export was successful and listing any exceptions (records containing errors) if they exist.

1. Open the [Nelco partner site](https://spectrum.nelcoportal.com/import/gwximport).

1. Select the Import Data link and select the 'Federal Information Reporting' Form Type and .

1. Select the file to upload from your Downloads folder.

1. Select the Import button.

1. On the Forms In Progress screen, choose the filing services you wish to use, related to electronic filing and delivery of forms to employees.

1. Make sure all the employees for your companies are selected on this screen and select Next.

1. If you selected the 'Recipient Mail & Online Retrieval' service, enter recipient email addresses.

1. Review the recipients in your cart and select the Next button.

1. On the Payment Details screen, enter credit card information.

1. Select the Pay & Submit button to complete processing.
