---
title: "Create / Submit Quarterly Unemployment Report Using Aatrix | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/unemployment/create--submit-quarterly-unemployment-report-using-aatrix"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/unemployment/create--submit-quarterly-unemployment-report-using-aatrix"
---

# Create / Submit Quarterly Unemployment Report Using Aatrix

You can use Aatrix to create and submit your quarterly unemployment reports. And because Aatrix gets unemployment information directly from the PRDT (PR Pay Seq Totals) table, it eliminates the need to use the PR Unemployment Process form.

- You must have Aatrix installed on your local workstation. For more information, see [Enabling Aatrix on a workstation](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aatrix-reporting/enable-aatrix-on-a-workstation) and [Regulatory Reporting using Aatrix](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aatrix-reporting/about-regulatory-reporting-using-aatrix).

- You must assign the appropriate Aatrix Tax Type to each state's SUTA liability code in PR Deductions and Liabilities. Vista uses this information to correctly pass unemployment data to Aatrix.

- You must assign the appropriate SUTA liability code to each state in PR State Information. Vista uses this information to compute SUTA and to pass unemployment data to Aatrix.

- If your state requires additional employee data unique to unemployment regulatory reports (for example, the 7-digit NAICS, Corporate Officer identification, and Coverage Types needed for Wyoming unemployment reporting), you must set up Aatrix IDs to identify that data and the associated values. For more information, see [Set up Aatrix IDs for State Regulatory Reporting](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/set-up-aatrix-ids-for-state-regulatory-reporting).

 For many states, using Aatrix for unemployment reporting is currently optional. However, Viewpoint is transitioning to the advanced e-filing capabilities offered through Aatrix. As states change their reporting requirements and e-filing specifications, the standard Vista e-file format may no longer apply and will therefore require using Aatrix for SUI reporting. For a list of states that fall into this category, see [States Requiring Aatrix for Unemployment Reporting (United States)](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/unemployment/states-requiring-aatrix-for-unemployment-reporting-united-states).The following details how to create and submit quarterly unemployment reports using Aatrix:

1. From the main menu, select Payroll > Programs > PR Aatrix Report Selection.

1. In the Tax Year field, enter the reporting tax year.

1. From the Federal/State drop-down (to the right of the tax year), select the reporting state.The Form Type selection box displays the regulatory forms relevant to the selected state.

1. Select the unemployment form for the specified state.The Date Filter section displays a Period drop-down.

1. From the Period drop-down, select the reporting quarter.

1. Select Continue to launch the Aatrix wizard.

1. Follow the prompts in the Aatrix wizard to complete the process.Note: As you proceed through the wizard, you must resolve any areas highlighted in red before you can file the report, even if those areas are not related to unemployment (for example, state withholding or local taxes).If the wizard highlights zero values in red and the zero values are correct, you must enter 0.00 in each field to validate the zero value. Otherwise, enter the correct value.

This brief video demonstrates quarterly unemployment reporting using Aatrix.Note: You must use a browser on your local computer to view this video, and not a browser in the cloud. If you are currently using a cloud-based browser, copy this page's URL and paste it into a web browser on your local computer.

Related information

- [About the PR Unemployment Process Form](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/unemployment/about-the-pr-unemployment-process-form)

- [About Regulatory Reporting Using Aatrix](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aatrix-reporting/about-regulatory-reporting-using-aatrix)
