---
title: "Affordable Care Act Processing | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/year-end/year-end-for-u.s.-payrolls/processing/affordable-care-act-processing"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/year-end/year-end-for-u.s.-payrolls/processing/affordable-care-act-processing"
---

# Affordable Care Act Processing

Form 1095-C is used by employers that are required to report their offers of health coverage to the IRS and employees. It is issued to an individual by an employer subject to 'employer shared responsibility' for providing minimum essential health coverage to any of its employees.
Viewpoint has partnered with Nelco to provide initial e-filing at no cost. Nelco can also handle any follow-up 1095-C corrections for a fee, and printing and mailing of physical forms are also available for an additional fee.
Note: These forms are exported from each of the companies where the employees are set up, and each file can be separately uploaded to Nelco for processing.

## 1095-C Processing

Open the Payroll > Period End > 1095-C Processing screen to add and edit employee-specific reporting information. Individual employee records can be edited and deleted, and new records can be manually entered here.
After the year is entered, the grid populates with the codes and names of employees who have been paid in this company in the year. Entries from previous years will be saved, and will re-appear when that year is entered.
If employees and dependents have been setup in Human Resources module (see the [Affordable Care Act Setup](/en/spectrum/spectrum/year-end/year-end-for-u.s.-payrolls/year-end-preparatory-actions/affordable-care-act-setup) section for more information), employee dependent information automatically populates into Part III of the 1095-C form.

- To edit an employee record, select the record in the grid, and select the Edit button.

- To delete an employee record, select the record in the grid, and then select Delete.

## Export Worksheet

To make the process of filling in lines 14-16 of the 1095-C easier, select the Export Worksheet button to export a 1095-C Excel template.Note: The worksheet does not include any previously entered 1095-C entries.

To save the worksheet, follow these steps:

1. On the pop-up screen, enter the reporting year.

1. If your company provides health insurance for your employees, select the Employer provided self-insured coverage? checkbox.

1. Enter the name of the file. The file created is a comma-delimited file, and is not given an extension by Spectrum.

1. Select OK and download the file to your workstation.

1. Open Excel with a blank workbook.

1. Select into the Data tab.

1. Select From Text.

1. Search for the file entered in Step 2 at the download location (if you didn't give the file an extension, choose to look for all files).

1. Choose the file, and select Import. Note: If you don't choose the Import option for opening the file, all leading zeros will be dropped from the file, negatively impacting birth dates and employee codes.

1. Use the following settings to import the data:

- Select Delimiters = Comma

- Data Type Detection = Based on entire dataset

- Select Transform Data

- Select all columns in the data preview:

- Select the left-most column with your mouse

- At the bottom, scroll all the way to the right

- Holding down the shift key, select the right-most column with your mouse

- Add filter to use first row as header

1. Select Close & Load.

The worksheet is populated with a list of employees who were paid in the year entered, and columns for entering, per month, lines 14 – 16 for each employee. For self-insured employers, the list may also include employee and dependent records for filling out Part III, and does include blank columns for filling out Part III.
For import, save the worksheet as a .csv / comma-delimited file.

## Import Worksheet

On the Form 1095-C Maintenance screen, select the Import Worksheet button to import information from the Employee Worksheet (saved as a .csv file). The imported records will change existing records where the employee code / employee name matches (including writing blanks over previously entered data). If an employee code is not on the import file, existing records will not be impacted.
To add employee information, select an employee, select the edit button to open the Edit Form 1095-C window and make changes to an individual employee. The 'Offer' fields and the 'Safe Harbor' fields each provide drop-down lists for IRS-designated codes.

## File ACA forms using Nelco

Before exporting ACA data to Nelco, there are a few additional steps:

- Contact Nelco at 1-800-266-4669 to obtain your prepaid 1095-C filing code. You will need to provide the total number of customer records you are processing, and your Spectrum customer ID. If you do not know your customer ID, contact Support using the [Viewpoint Customer Portal](https://support.viewpoint.com/s/).

- Select the Print Forms button on the Form 1095-C Maintenance screen, and review all 1095-C reports for accuracy and completeness.

- Once all entry in Spectrum is complete, select the Export button to export the data for electronic processing. The Export to Nelco information window displays.

- Enter a contact and phone number for your company, and select Continue to proceed with the export.

- Save the file to your workstation. Note: Do not open the export file in Microsoft Excel, as this will remove leading zeros from, for instance, codes and birth dates. If you need to make any changes to the export file, use a text editor like Notepad, or make changes in Nelco's portal instead.

Import your 1095-C data into Nelco for processing:

- Open the [Nelco partner site](https://spectrum.nelcoportal.com/import/gwximport).

- Select the Import Data link, select the 'Affordable Care Act Reporting' Form Type, and then select File to Import.

- Navigate to and select your .CSV file.

- Select the Import button.

- On the Forms In Progress screen, choose the filing services you wish to use. Remember that Federal E-filing is provided at no cost with the prepaid filing code from Nelco, and printing and mailing services are available for an additional fee. If you only want to file the 1095-C Forms, select the Federal E-filing option from the A LA CARTE SERVICES section.

- Make sure all the employees for your companies are selected on this screen and select the Next button to proceed.

- If you selected the Recipient Mail & Online Retrieval service, enter recipient email addresses.

- On the 1094-C Data Entry screen, enter Applicable Large Employer (ALE) Member transmittal information for your company. Refer to the IRS instructions for details on entering this information.

- Review the recipients in your cart and select the Next button.

- On the Payment Details screen, enter the Prepaid Filing Code you received from Nelco earlier and select the Apply Code button. If you are having Nelco print and mail the forms for you as well, you will need to enter credit card information on this screen for those services.

- Select the Pay & Submit button to complete processing.
