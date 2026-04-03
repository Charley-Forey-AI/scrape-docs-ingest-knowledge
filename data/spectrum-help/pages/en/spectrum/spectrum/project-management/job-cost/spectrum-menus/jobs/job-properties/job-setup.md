---
title: "Job Setup | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/job-setup"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/job-setup"
---

# Job Setup

Use this screen to set up additional properties for the job.
FieldsDescriptions
Job codeEnter or search for the job code you want to view. The description displays.
Defaults
Tax classification/Sales tax codeUse this optional field to track the sales tax or reporting location. The sales tax code is for Accounts Receivable reporting purposes while the tax classification code is a combination of Accounts Receivable sales tax and Accounts Payable sales or use tax.
Select the Utilize tax classification checkbox in [Job Cost Installation - Properties](/en/spectrum/spectrum/project-management/job-cost/installation-overview/job-cost-installation---properties) to display the Tax class code field. Leave the checkbox clear to display the Sales tax field.
Tax classification and sales tax codes should have been previously set up in [Tax Classification File Maintenance](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/tax-classification-file-maintenance). For details, see the Use Tax Management [In-Depth Overview](/en/spectrum/spectrum/project-management/job-cost/in-depth-overview) topic.
Tax Classification: Add or edit the tax class code for this job. You can enter up to 15 alpha-numeric characters.
If you filled out the Quick Job setup section, and set the code to copy the tax classification code, the tax code defaults from the Group code field.
Sales tax: Based on the job's location, enter the default Sales Tax Code. A code should be entered even if this is not a taxable job. Click the drop-down arrow or double-click on this field to view valid sales tax codes.
If you selected the Group code and a Customer above, then the sales tax code associated with that customer is the default.

TaxableSelect a taxable status:

- Yes: Select if the contract invoice is taxable. If you selected a Group code that is set to copy the taxable setting, then this field displays Yes.

- No: Select if it is not taxable. If the Sales tax code is at 0.00%, then No displays.

- No Default: This setting is the default for the billing detail. Select if the invoice is conditionally taxable and the decision needs to be made on a case-by-case basis.

Job overhead batchSelect the overhead allocation Batch code.You can specify the allocation of overhead on job batches in [Overhead Allocation Maintenance](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/overhead-allocation-maintenance).
A/P invoice approval
This section is available only if the Use invoice approval
 processing checkbox is selected in the Accounts Payable Installation > Invoice Approval tab.
Default routing code(Optional) Enter a routing code to use as the default.
Invoice dollar limit
Routing code over limit
The dollar limit which should trigger the use of the over-limit routing code, and the routing code to use when an invoice amount exceeds the dollar limit. If there is no established invoice dollar limit, leave this field blank.Note: You can opt to leave both fields blank and instead manage the approval routing by entering Approval Limits on the Routing Code. For additional information, see [Approval Limits](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/about-invoice-approval/approval-limits).

Phase setup
If the job specified in the heading is a sub job, the fields in this section will be hidden. An exception to this rule is if a particular field in the sub-job is different from the master job, that field will be available to edit and make the same as the master job.
Phase categoryEnter the phase category or select the drop-down arrow to select from a list of available phase categories.
Phase maskEnter the phase code display mask for this job (for example, X-XX-XXX).
This field stores the display pattern of your phase code for this job and is used throughout the application.
Though not required, some users define phases according to the Construction Specifications Institute (C.S.I.) standard.
You can specify up to 20 characters, including dashes or or capital X, and up to two levels of summarization.
You can also define a single phase, particularly if the operation is a subcontract or specialty contractor with a limited variety of tasks.
The phase code mask should not be altered after initial installation. This
 standard phase mask will default as new jobs are added from the
 Job Cost Installation screen.
Example 1: You may plan to set up a six-digit phase code with two tiers of summarization and dashes for readability (0-22-000, 0-26-000, 1-16-000, and so forth). The mask for this phase code would be X-XX-XXX.
Example 2: You may opt for a six-digit pattern for your phase code with the first two digits indicating the group subtotal point (02-2000, 16-0000, and so forth). The mask for this phase cost configuration would be XX-XXXX.
Example 3: The phase could simply be a single phase 1. The mask in this case is X.

Major group start positionEnter the standard position, left to right, in which the major group starts. This is either 1 or blank (zero), depending on whether this job will utilize major group subtotals.
 Major group subtotals are necessary only when two tiers of group subtotals
 are desired. If only one tier of subtotals is desired, the minor group
 should be used; the major group positions are to be set to blank (zero). The
 standard position will default as new jobs are added from Job Cost
 Installation.

Major group end positionEnter the standard position, left to right, in which the
 major group ends. This is either a digit or blank
 (zero), depending upon whether this job will utilize major group subtotals.
 Major group subtotals are necessary only when two tiers of group subtotals
 are desired. If only one tier of subtotals is desired, the minor group
 should be used; the major group positions are to be set to blank (zero). The
 standard position will default as new jobs are added from Job Cost
 Installation.
An example of a phase structure with major and minor group subtotals is X-XX-XXX. The ending position of the major group in this example is also 1 (1-XX-XXX).

Minor group start positionEnter the standard position, left to right, in which the
 minor group starts. This is either a digit or
 blank (zero). The standard position will default as new jobs are added from
 Job Cost Installation.
An example of a phase structure with major and minor group subtotals is X-XX-XXX. The starting position of the minor group in this example is 2 (X-2X-XXX).
An example of a phase structure with only minor group subtotals is XXX-XXXX. The starting position of the minor group in this example is 1 (1XX-XXXX).

Minor group end positionEnter the standard position, left to right, in which the
 minor group ends. This is either a digit or blank
 (zero), depending upon whether this job will utilize minor group subtotals.
 If no group subtotals are desired, all four group positions should be set to
 blank (zero). The standard position will default as new jobs are added from
 Job Cost Installation.
An example of a phase structure with major and minor group subtotals is X-XX-XXX. The ending position of the minor group in this example is 3 (X-X3-XXX).
An example of a phase structure with only minor group subtotals is XXX-XXXX. The ending position of the minor group in this example is 3 (XX3-XXXX).

Default purchase order ship-to address
Override job address on P.O.?Select to designate a default ship-to address on purchase orders for this job, instead of using the general job address as specified in [Job Main Properties](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/job-main-properties) If this checkbox is clear, the other fields in this section will be disabled.
Ship-to nameEnter a name for the new ship-to location.
Ship-to addressComplete the New Address window by entering the full
 ship-to address for the purchase order.
Earned revenue calculation
The percent method is usually selected for fixed price and unit price jobs.
This method is used in the contract status report and over report and inquiries for the calculation of the earned amount.
If the percent method is chosen, then the system will calculate the "earned amount = % complete times the revised contract amount".
The percent complete is the actual cost/projected cost or actual cost/estimated cost (if using the non-projected method). Also, in the job file, you may enter an entered percent complete for the entire job, which will be used instead of the calculated percent complete (if using the projected method only).
This function may also be used to track earned revenue on jobs with both fixed contract and T+M phases. However,you may also set up a new job to keep the T+M revenue/costs separate from the fixed.

The Billed method is normally used when calculating earned revenue for a T+M job,
This method prompts the user to enter an unbilled amount, if desired. The calculation is now "earned amount = billed amount + unbilled amount". The system will then enter TM under the percent complete field. This option allows the user to calculate the earned amounts properly for time and material jobs, and for cost plus jobs.
The Unbilled amount field displays below when you select this option.

Percent

Master job methodBilled

Sub job methodCost

Pay-When-Paid window
Use the Pay-When-Paid button when defining the
 pay-when-paid policy for the current job. (This window is conditionally
 available from the [Job Payables](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-costs/job-payables)
 screen.)
The parameters in this window are offered by job, in order to specify the job-specific pay-when-paid policy for when vendor invoices are reviewed for release following receipt of customer payment. The policy also offers settings to 'auto-release' vendor invoices after a specified percentage of payment for the customer billing has been received (excluding retention).

Pay A/P invoices on this job based on customer
 payment?When this checkbox is selected, you will be prompted for auto release and flag for review parameters, based on customer payment.
This checkbox serves as a trigger for new invoices in Vendor Invoice Entry, in
 conjunction with the pay-when-paid default settings found on the
 Vendor Defaults screen and the Subcontract
 Defaults screen.

Auto-release A/P invoicesThe release parameter impacts how the Accounts Receivable > Cash Receipts Update works.
When____% of non-retention portion of customer billing is
 paidEnter a value between .01 and 100 percent.
Flag A/P invoices for reviewThe review parameter impacts how the Accounts
 Receivable > [Cash Receipts Journal](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/cash-receipts-journal) works.
When____% of non-retention portion of customer billing is
 paidEnter a value between .01 and 100 percent if this field is enabled.
Unbilled Amount or Cost markup %
Unbilled amountDisplays when you select the Billed option above. Enter the unbilled amount to be added to amounts already billed in order to determine earned revenue-to-date on the job.
Cost markup%Displays when you select the Cost option above. Enter the percentage to mark actual cost-to-date to determine earned revenue-to-date on the job.

Related information

- [Overhead Allocation Maintenance](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/overhead-allocation-maintenance)
