---
title: "Set up Oregon Transit Tax | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-oregon-transit-tax"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-oregon-transit-tax"
---

# Set up Oregon Transit Tax

This topic discusses how to set up Oregon Transit Tax (OTT)
.
 If you are an Oregon employer, you must withhold
 Oregon Transit Tax from your employees' wages as follows:

- If the employee resides in Oregon, the withholding applies to
 all wages, regardless of where the employee works.

- If the employee does not reside in Oregon, the withholding only
 applies to wages earned for services performed in Oregon.

If you are a non-Oregon employer, and you have employees that
 reside in Oregon, you have the option to withhold Oregon Transit Tax from their
 earnings, as long as their compensation falls within the definition of wages as stated
 in ORS 316.162. If you choose to not withhold the Oregon Transit Tax from their
 earnings, the employee is responsible for filing and paying the tax.
Note: Oregon Transit Tax amounts withheld during the year
 are reported in Box 14 of employee W-2s. If you are using Aatrix to generate W-2's,
 Oregon Transit Tax is reported as a local tax and will be included in Boxes 18, 19, and
 20 of the W-2. Since Box 14 does not show subject amounts, if you want W-2s to reflect
 the subject amount, use Aatrix to generate W-2s.
The
 following information details how to set up the Oregon Transit Tax.

1.  From the main menu, select Payroll  > Programs > PR
 Deductions/Liabilities.

1. Set up a new deduction code for Oregon Transit Tax using the following settings:

- Type = Deduction

- Calculation Category = S-State

- Method = G-Rate of Gross

- Rate / Amount #1 = Enter the current rate (see the [Oregon Department of
 Revenue](https://www.oregon.gov/DOR/programs/businesses/Pages/statewide-transit-tax.aspx) for information.

- Rate / Amount #2 = Enter the same rate you entered in the
 Rate / Amount #1
 field.

- Accumulate Subject Amounts = Select this checkbox.

- Aatrix Tax Type (Addl Info tab, W2 section) = 5666 (Statewide Transit Tax)

Important: The Aatrix Tax Type is required even
 if you are not using Aatrix. The system will use this information in the
 generation of W2s, as well as for the regulatory reports for Oregon Transit Tax
 available in PR Aatrix Report Selection (OR OR-STT- -1/2 Form and OR OR-STT-V
 Form).

1. Save the record.

1. From the main menu, select Payroll > Programs > PR State Information.

1. In the State field, enter OR or press F4 to select Oregon from the list of states.

1. Click on the Add'l State Based Dedn/Liabs tab.

1. In the grid, add the deduction code that you just
 created in PR Deductions/Liabilities.

1. Select the Always calc for resident checkbox.

1. Save the record.

You are now set up to include Oregon Transit Tax when processing applicable employees.
When you are ready to process W-2s, you must add the Oregon Transit Tax deduction to the state-specific Box 14 information so that it is included when processing W-2s. For more information, see [Setting State-Specific/Misc Box 14 Information for W-2 Processing](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/w-2s/set-state-specific-box-14-information-for-w-2-processing).

Related information

- [About Job Cost and Service Management Options](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-job-cost-and-service-management-options)

- [PR Groups Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-groups-form)
