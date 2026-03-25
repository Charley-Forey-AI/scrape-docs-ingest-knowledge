---
title: "About the PC Potential Projects Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/pre-construction/pc-potential-projects/potential-project-setup/about-the-pc-potential-projects-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/pre-construction/pc-potential-projects/potential-project-setup/about-the-pc-potential-projects-form"
---

# About the PC Potential Projects Form

You can use the PC Potential Projects form to create and
 maintain potential projects.
Potential projects represent bid or estimate work that may or may not be awarded and become contracts/jobs in the Project Management and Job Cost module.

## Info Tab

Use this tab to enter information about the potential project, including the project
 name and description, site location, project details (size, status, type, value, etc.),
 and bid results.

## Bid Info Tab

This tab contains bid information for the project. You can track the bid status and bid
 dates (started, completed, and submitted), project plan administration and availability,
 and cost breakdowns (e.g. labor costs/hours, material costs, equipment costs/hours,
 etc.). In addition, options are provided to indicate whether a bid bond is required and
 whether pre-qualification is required for bidding.

## M/WBE Goals Tab

Use this tab to track SWMBE goals for the potential project.
If you use [PC Create PM Project](/en/vista/vista/costs-and-contracts/pre-construction/pc-potential-projects/potential-project-setup/about-the-pc-create-pm-project-form) to create a PM project from this
 potential project, the SWMBE goals will copy over to the PM module project and they will
 display on the M/WBE Goals tab of PM Projects. Changes made on this tab after a PM
 project has been created will update the PM project, and changes made on the PM project
 will update the potential project.

## Project Team Tab

Use this tab to define the team members on
 the project. Team members are contacts involved in the project, for example owners,
 contractors, subcontractors, estimators, and engineers.
When setting up contacts, you will need to
 assign a contact type and a contact source.

- The contact type identifies the
 contact's capacity in the current project. You can have several contacts of the
 same type on a project; likewise, a contact can be assigned different contact
 types depending on the projects to which they are assigned.

- The contact source determines the
 list of contacts available for selection. For example, if the contact source is AP
 Vendors, the contact must exist in the AP Vendors. Make sure contacts are set up
 in the appropriate form (e.g. AP Vendors, AR Customers) before you add them as a
 team member here.

When using [PC Create PM Project](/en/vista/vista/costs-and-contracts/pre-construction/pc-potential-projects/potential-project-setup/about-the-pc-create-pm-project-form) to create a PM project from a PC
 potential project, the team members that are PM contacts can be copied to the new PM
 project. Click [here](/en/vista/vista/costs-and-contracts/pre-construction/pc-potential-projects/potential-project-setup/about-the-pc-create-pm-project-form) for more information on PC Create PM Project.

## Bid Packages Tab

Use this tab to set up bid packages for the
 potential project. Bid packages are used to define areas of work (scopes or phases) that
 you will send out for bid.
You can set up the preliminary information
 for a bid package on this tab or via [PC Bid
 Package](/en/vista/vista/costs-and-contracts/pre-construction/pc-potential-projects/bids/about-the-pc-bid-package-form) (accessed by double-clicking in the grid). Other information for the
 bid package (scopes/phases and the bid list) can be set up via PC Bid Package.
For information on setting up a bid package
 for a potential project, [click here.](/en/vista/vista/costs-and-contracts/pre-construction/pc-potential-projects/bids/setting-up-a-bid-package)

## Bid Coverage Tab

The Bid Coverage tab is used to maintain the vendor bids on a potential project. [Click here for more information on this tab. ](/en/vista/vista/costs-and-contracts/pre-construction/pc-potential-projects/bids/about-the-pc-bid-coverage-form)

## Correspondence Tab

The Correspondence tab displays
 emails/faxes sent using [PC Create and Send](/en/vista/vista/costs-and-contracts/pre-construction/pc-create-and-send/about-the-pc-create-and-send-form) that relate to the potential project.
 This includes emails/faxes sent from both PC Potential Projects and PC Bid Package. For
 example, if you emailed an invitation to bid to a vendor on the bid list, that
 correspondence will display on this tab.
Click [here](/en/vista/vista/costs-and-contracts/pre-construction/pc-create-and-send/about-pc-module-email-integration)
 for an overview on email integration in the PC module.
Click [here](/en/vista/vista/costs-and-contracts/pre-construction/pc-create-and-send/about-the-pc-create-and-send-form) for more information about using PC Create and Send
 to generate and send documents to vendors.

## Forecast Info Tab

Use this tab to set up forecasting
 information for the project. The Allow Forecasting box, when checked,
 indicates that forecasting information for this potential project will be included in
 reports and Business Intelligence (BI).
The Scheduling section is used to identify
 the estimated start and completion dates for the project. These dates will be used to
 generate the forecast schedule (Forecast tab).
Use the Forecast section to identify the
 revenue, cost, and profit estimates for the project. These estimates will be used to
 determine the forecast amounts (on the forecast schedule).
You can also enter probability percentages
 for the company taking on the project (Go Probability) and being awarded the project
 (Award Probability). The Projected Chase field represents the
 estimated value of potential work. This value is a calculation of the Revenue Estimate x
 Go Probability x Award Probability, and will generally be reviewed by design build
 contractors to determine the feasibility of the project for their company.

## Forecast Tab

Use this tab to set up the forecast for the
 potential project. The forecast defines, by month, the expected revenue, cost, and
 profit over the life of the project. If you have set up forecasting options in [JC Company Parameters ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form) (Forecast tab), the forecast will
 be generated automatically based on the start and completion dates, the estimates
 specified on the Forecast Info tab of PC Potential Project, and the forecast options
 defined in JC Company Parameters.
 For example:
In [JC Company Parameters ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form), set up the Forecast tab like
 below:
Revenue
Revenue
 Forecast MethodCurve
# of Rev.
 Forecast Intervals3
Revenue %
 Complete at end of each interval20:50
Cost
Cost
 Forecast MethodCurve
# of Cost
 Forecast Intervals3
Cost %
 Complete at end of each interval20:50

You then set up a potential project with
 the following information:
Start
 Date:01/01/10
Complete
 Date:12/31/10
Revenue
 Estimate:3,500,000
Cost
 Estimate:1,680,000
Profit
 Estimate:1,820,000

Once you save the project, the forecast
 will initialize as shown in the example below. The highlighted months are those marking
 the 1/3 and 2/3 intervals for the project based on the forecast intervals specified for
 revenue and cost in JC Company Parameters. The percentages shown for these months
 coincide with the revenue and cost complete percentages defined for these intervals
 (i.e. 20:50).
Note: When the project is awarded and a contract set up
 in JC Contracts or PM Projects (referencing the project), the forecast defined here does
 not transfer to the contract. Actual forecast values for the contract will be
 initialized once you have set up contract items and values, as well as the phase/cost
 type estimates for the associated job.

## Adding Reports to the Form

You can associate a report with a form so
 that you can launch the report from the form using the Options > Reports menu. For example, you might want to associate the PC Bid Analysis or PC
 Subcontract Risk reports with this form so that you can launch those reports directly
 from the form and view the bid and vendor information.
Click [here](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-reports-by-form-form) for information on launching reports from a form.
Note: Many tabs on PC Potential Projects actually
 represent unique forms. For example, the Bid Packages tab is actually the PC Bid
 Packages form not PC Potential Projects, so if you want to launch a report while the Bid
 Packages tab is open, you have to associate the report with PC Bid Packages. You can
 view the form associated with a tab by pressing F3 while in any field on a tab.

The following are related topics:
[](/en/vista/vista/costs-and-contracts/pre-construction/pc-potential-projects/potential-project-setup/overview-pc-potential-project-to-pm-project)Overview: PC potential project to PM project
[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters
[](/en/vista/vista/project-management/projects-and-contracts/contracts/pm-contracts-form)PM Contracts
