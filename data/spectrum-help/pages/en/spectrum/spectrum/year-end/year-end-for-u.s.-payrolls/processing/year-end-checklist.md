---
title: "Year-End Checklist | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/year-end/year-end-for-u.s.-payrolls/processing/year-end-checklist"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/year-end/year-end-for-u.s.-payrolls/processing/year-end-checklist"
---

# Year-End Checklist

The Year-End Checklist section provides step-by-step checklists for processing your year-end information. This section also includes supplementary instructions for processing Confidential Payroll at year-end.

## Payroll Year-End Checklist

After completing the final payroll cycle for a given year, it is necessary to close payroll records and prepare for the upcoming year.
Important: If you have Confidential Payroll, please read through the [Confidential Payroll Year-End Instructions](/en/spectrum/spectrum/year-end/year-end-for-u.s.-payrolls/processing/confidential-payroll-year-end-instructions) before following this checklist. There are additional or alternate steps to take if you have a Confidential Payroll company.
This is an overview of the year-end process:

- Order Forms for the prior tax year.

- Complete the final pay cycle for the year.

- Print the period end payroll reports.

- Perform the W-2 Form Build.

- Adjust tax tables for the next year's rates.

- Change processing dates to the new year.

- Perform the Year End Update.

- Commence regular pay cycles in the new year.

- Complete W-2 processing for the prior year.

For more information about what you can do to prepare for year-end before your final payroll cycle, see [Year-end Preparatory Actions](/en/spectrum/spectrum/year-end/year-end-for-u.s.-payrolls/year-end-preparatory-actions).

## Step 1. Order Forms for the Tax Year

- W-2, W-3, and 1099-Misc Forms are available online at [https://store.viewpointforms.com/Store#Category:29833:Spectrum](https://store.viewpointforms.com/Store#Category:29833:Spectrum).

- Viewpoint Forms are all guaranteed to work with Spectrum.

- Review your check stock and order more if you are getting low.

## Step 2. Complete the Final Pay Cycle of the Year

- For all checks dated up to December 31 in the prior year. Note: If the check date is in the new year, it's in a new-year pay cycle. This is true even if the period end date is in the prior year.

- Once the Year End Update is performed and a payroll cycle in the new year has been updated, payroll checks cannot be run again for prior year, or else the new year's YTD totals will be incorrect.

## Step 3. Print the Period End Payroll Reports

1. Go to Payroll > Reports. Note: If in a Confidential Payroll company, navigate to Confidential Payroll module to run payroll reports. Refer to the Confidential Payroll Year-End Instructions for more detail.

1. Print quarterly tax reports that are relevant to you:

- Payroll Register

- Unemployment Tax Report

- Quarterly Federal Tax Report

- State Disability Insurance Report

- Subject to Tax Report

- Workers' Compensation Report (Rate per $100)

- Workers' Compensation Report (Rate per Hour)

- Workers' Compensation Job Expense Report

- Employee Earnings History Report

## Step 4. Perform the W-2 Build

1. Navigate to Payroll > Period End > W-2 Processing, then select the Build button. Note: If in a Confidential Payroll company, navigate to Confidential Payroll > W-2 Processing module to build W-2 forms, then select the Build button. Refer to the Confidential Payroll Year-End Instructions for more detail.)

1. Perform the Build W-2 Forms. See the Payroll Processing topic for more details.

## Step 5. Update Tax Tables to the New Year's Rates

There are two methods for updating the income-tax-graduated tables in Spectrum:

- Programmatically - Apply the automatic tax table import available for download from the [Viewpoint Customer Portal](https://support.viewpoint.com/s/product-more-resources?product=Spectrum&type=Downloads&links=true&title=Downloads%20for%20Spectrum).

- Manually - Enter updates in the Income Tax tab of the Tax Table Maintenance screen.

Automatic Tax Table Update – for Income-Tax-Graduated Tables onlyNote: The electronic tax table update provided by Viewpoint covers federal income tax tables and all 50 states' graduated and percentage income tax tables. It also updates standard deductions and exemptions as applicable. It does not cover other tax rates, such as FICA, Unemployment, SDI, or Worker's Comp. Adjust and confirm those tax rates and limits manually.

The electronic tax table update affects all companies equally. If you run payroll in multiple companies, before entering updates in US tax tables, complete Steps 1-4 of the Year-End Checklist in all payroll companies.

1. Log in to [Viewpoint Customer Portal](https://support.viewpoint.com/s/).

1. Select Products and select Spectrum.

1. Select Spectrum 202X Tax Tables in the Downloads section.

1. Select the Downloads 202X Tax Tables folder.

1. Select the PRTAXTABLE-202X-XX.PRO file.

1. Select the Download button, and save the .pro file to your workstation. For more detailed instructions on installing the tax table file, view the Tax Table Loading Instructions document available in the Viewpoint Customer Portal.

1. In Spectrum, go to System Administration > Year End > Tax Table Import.

1. Choose one:

- Select Preview to verify that all payroll cycles are completed in ALL companies, and to print the Tax Table Listing report.

- Select Import Only to skip the preview.

1. Upload the file saved in step 6. When the update completes, the screen returns to the Site Map.

## Manual Update: US Tax Table and FUTA/FICA rates

Note: IRS Publication 15-T contains the US Federal taxation rates. Review this publication when setting your US tax rates.

1. Go to Payroll > Maintenance > Tax Tables.

1. In the Tax Table Maintenance screen, type "US" in the search field and select Go.

1. On the Income Tax tab, select a filing status.

1. Select Edit to make changes to the graduated tables, as required for that filing status.

- On the Std Deduction and Tax Credit tabs, taxes should remain at None. The Exemption tab should be set for US Withholding values. It is the amount of withholding before calculation. The Exemption, Std Deduction, and Tax Credit tabs are set for each filing status separately.

1. In the Other Taxes tab, update FUTA and FICA rates as needed.

1. When you are done making changes, print the Tax Table Listing and compare it to the numbers on the IRS site.

## Manual Update: US State Tax Tables

Note: For Multi-Company Users: If you perform Payroll in more than one Spectrum company, take these steps in each company.

1. Go to Payroll > Maintenance > Tax Tables.

1. In the Tax Table Maintenance screen, type the state tax table code in the search field and select Go.

1. On the Income Tax tab, select a filing status.

1. Select Edit to make changes to the graduated tables and other income tax settings, as required for that filing status. Please consult with individual state revenue departments and/or your tax advisor to set up withholding for state income taxes.

1. In the Other Taxes tab, update the SUTA and SDI rates if needed.

1. When you are done making changes, print the Tax Table Listing and compare it to the numbers in state department of revenue documentation.

## Update Workers' Compensation Rates

Workers' compensation rates may have changed as well. Be sure to make changes, when new rates are available.
Go to Payroll > Maintenance > Worker's Compensation.

## Step 6. Update Aatrix Tax Table Types

If you use Aatrix to file, update tax types on a periodic basis using an Aatrix import file stored in the Viewpoint Customer Portal.

1. Go to the [Viewpoint Customer Portal](https://support.viewpoint.com/s/product-more-resources?product=Spectrum&type=Downloads&links=true&title=Downloads%20for%20Spectrum), select Aatrix Tax Types for Spectrum, and download the CSV file to your workstation.

1. In Spectrum, go to System Administration > Year End > Import Aatrix Tax Types.

1. Select Continue, and then Choose File.

1. Navigate to and select the .csv file downloaded to your workstation, and select Upload.

When the upload is complete, you are returned to the Site Map.

## Step 7. Change Payroll and General Ledger Processing Dates to the New Year

Go to System Administration > Installation > Processing Dates.
Note: If the first payroll dated in the new year has a period end date in the prior year, set the minimum date to the period end date.

## Step 8. Perform the Year End Update Procedure

Important: Before you proceed, confirm that no further payroll checks are needed dated for the prior year.
The Payroll Year End Update clears the prior year YTD earnings figures, preparing the way for the payroll cycles in the new year. Once the Year End Update is performed, and a payroll cycle in the new year is updated, it is not advisable to attempt to process a prior year's payroll check. Special procedures would have to be taken to do so (like voiding all the payroll checks in the new year) and is not recommended.

1. Go to Payroll >  Period End  >  Year End Update. The Year End Update/Employee Purge tab displays.

1. In the Set new payroll year to field, enter the new year.

1. Select Preview to review a list of employees whose data will be purged.

1. Select Continue on the Year End Update / Employee Purge screen to finish the procedure.

For non-standard calendar years that require an additional pay period, select the Extra pay period this year checkbox on the [Tax Table Maintenance](/en/spectrum/spectrum/year-end/year-end-for-u.s.-payrolls/processing/year-end-processing-screen-u.s./tax-table-maintenance) or [Year End Update](/en/spectrum/spectrum/year-end/year-end-for-u.s.-payrolls/processing/year-end-processing-screen-u.s./year-end-update) screens. The system will calculate using the appropriate weekly and biweekly payrolls that occur in a non-standard calendar.

## Step 9. Commence Regular Pay Cycles in the New Year

Note: Make sure check dates are in the new year, regardless of the work date(s) or the period end date.

## Step 10. Complete W-2 processing

Employee W-2s for the prior tax year are due by January 31 in the new year.
Note: If in a Confidential Payroll company, navigate to Confidential Payroll > W-2 Processing module to build W-2 forms, then select the Build button. Refer to the Confidential Payroll Year End Instructions for more detail.

1. Go to Payroll > Period End > W-2 Processing.

1. Print and review the W-2 Listing. If necessary, make changes and reprint the list. See [Payroll Year-end Processing](/en/spectrum/spectrum/year-end/year-end-for-u.s.-payrolls/processing/payroll-year-end-processing) for more detailed information on W-2 processing.

1. All employees who have generated a W-2 are listed in the W-2 Form Maintenance screen. To browse for the desired employee, page down to scroll through the file. (The employee search window will only provide a list of employees found in the current company.)

1. Confirm that the W-2 format is correct.

1. Print the W-2s on plain paper to confirm the W-2s print at the desired printer and that the format matches your W-2 forms.

1. Load the W-2s into the printer and print.

1. If you are filing paper W-2 forms, prepare the W-3 Form.
