---
title: "What's New in Spectrum 2024 R2 | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/whats-new/previous-spectrum-releases/whats-new-in-spectrum-2024-r2"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/whats-new/previous-spectrum-releases/whats-new-in-spectrum-2024-r2"
---

# What's New in Spectrum 2024 R2

Spectrum 2024 R2 provides many enhancements ranging from report upgrades to workflow improvements to bolstered security.

## Greater flexibility in Payroll

Spectrum now provides the option to apply weighted average overtime to timecard lines. This functionality helps you ensure that employees earning different rates over the course of a week get the appropriate overtime rates applied to their timecard lines, rather than the straight overtime rate applicable only to the given line.

- To enable this feature, select Weighted average in the Defaults tab of the Payroll Installation screen.

- To apply the average OT rate to timecard lines during your payroll process, use the existing Auto OT button in Pre-Time Card Entry and Time Card Entry.

- For calculation details, see [Payroll Installation - Defaults](/en/spectrum/spectrum/accounting/confidential-payroll/installation-overview/payroll-installation---defaults).

The Approve Pre-Time Import and the Approve Pre-Time Quantity Import screens now have a Delete All button, giving you an option to delete all imported time card lines and re-import before proceeding to Pre-Time Card. You can also opt to delete all imported lines pertaining to only a single Batch code of your choosing.
The Reverse Pre-Time Card Transfer screen is used to reverse the pre-time card process by removing checks from the pay cycle and returning entries to pre-time card entry. It now provides a new option to limit this action to layoff and/or replacement checks only, meaning you can now reverse just checks that are causing issues and continue with all remaining time cards that have no errors.
The Subject-to-Tax Report screen now includes an Employee field so that you can narrow the report to just one, or multiple, but not all employees.
The Wage and Tax History Report now includes a modified version to identify employees who have over-accrued Tier 1 tax. Access the CPP Tax Exception Report using the My Reports button in the Wage and Tax History Report screen.
The Time Card Entry and Pre-Time Card Entry screens each provide a warning message you must acknowledge before proceeding to add, delete, or edit Void Check time card lines.
The Union Report screen now includes a Status section with Active and Inactive checkboxes so you can choose which unions should should be included in the report based on their current status.

## AP report upgrades

- It's now easier to print out a Subcontract Change Order form. Just go to Accounts Payable > Reports > Subcontract Change Order Form.Until now, Subcontract Change Order forms could be accessed only by first navigating to the Subcontract Change Orders screen and then taking several steps.

- You can now filter by job when running the Document Tracking report. Whether running the exception version or the distribution version, you can now select one or more jobs to narrow the report even further than before.

- The export to ePayments now includes the amount of retention paid. We added this field to the end of the existing Retention Paid report.

## AR workflow improvements

Enhancements to the Draw Request process:

- In the Reverse Last Draw Request screen, you can now enter an Invoice date when reversing a Draw Request. The Application date appears by default just like before, but now you can override it in the same screen, instead of opening the credit memo and changing it there. Your chosen date will appear when you create the Draw Request Credit.

- In the Draw Request Entry screen, the values in the % complete fields in the header and in the grid and in the Retention % field in the grid all have greater precision - instead of just one decimal point, these percentage values now display two decimal points.

- In the Draw Request Billing Worksheets report, the same precision has been given to the Cost % complete field in the header and to the values in the % column, located next to the Completed and Stored to Date column.

The AR Aged Open Item Report now includes the work order number, making it easy to identify the work order that is associated with the invoice appearing on the aging report. When running the report, Work Order is now a filtering option, and if you also want to see the work order number on the report, select the checkbox named Include work order number?.

## Job Cost improvements

- The existing A/R balance field in the Job Analysis Inquiry screen is now linked to the Contract Open Items screen; you can select the link to open the job and customer in context.

- The Projected Cost Entry screen now displays the period end date for which the batch was built, giving project managers better visibility by making easy to tell the date range the batch covers.

- The Phase Listing report screen now includes an option to launch a new report variation. You can select the Unit of measure exceptions only checkbox to generate a report which returns only UOMs found in any phases but which are not already present in the Unit of Measure File Maintenance screen.

## HR report upgrades

The OSHA Forms report screen now displays two fields which used to appear only in the HR Installation screen. Now all users with access to the OSHA Forms report screen can see values for these fields:

- Average number of employees

- Total hours worked last year

Users with HR security level 6 and higher can also see and use the adjacent Calculate buttons to generate updated values.

## Improved Work Order management

Work orders that are [paid via credit card](/en/spectrum/spectrum/service/service-tech/set-up-service-tech-mobile-credit-card-payment-collection) in the Service Tech Mobile app should be billed and closed out. To help streamline that, the Build List of Work Orders to Bill window has two new checkboxes:

- Require Finished Work Order Form to be printed prior to update? - selected by default to match current functionality, you can clear this checkbox to include *all* work orders in the transfer, even those which haven't had their Finished Work Order Form printed already.

- Set site work orders to complete? - cleared by default, you can select this checkbox if you want to close out all work orders included in the transfer, saving you the step of having to close them separately.

In the Service Contracts Main Properties screen, you can now enter the customer's purchase order number, and Spectrum will insert your entry in both the work order and the invoice at the moment they are created.

## SDX - Quick Setup Authorization ID

A new Quick Setup feature which quickly creates an Authorization ID for the current user in the Trimble application indicated in the dropdown helps streamline your integration efforts. When using this Quick Setup feature, Spectrum automatically grants all pertinent access to the newly created Authorization ID for these products:

- Traqspera - all required web services

- Supplier Xchange - the POBatch web services

- ProjectSight - all required web services

## Simplified Credit Card Payment setup

Setting up Service Tech Mobile credit card payment collection is now easier with these minor changes in the Service Tech Installation screen:

- Your chosen dispatch status which should default for work orders paid by credit card must necessarily be set as 'excluded' in the Excluded Status Codes section. Since this excluded setting is required, the system now sets it automatically at the moment you choose the default dispatch status.

- The Public key field is renamed Account ID to match the information that Stripe® provides when you're first getting set up.

- The Secret Key field is now obsolete, so it's been removed.

## Easier Fiscal Year record maintenance

When working in Fiscal Calendar Maintenance Auto-Create Additional Years, you can now enter 0 in the Number of additional years to create field and select Continue. This results in no years being added, which is the same thing as selecting Cancel, but is more apparent.


## System Administration

- The Time Card Approval form is now added to the list of authorized areas for the PM user type. To confirm this and other similar details, run the Access by User Type Listing, accessible from System Administration > Security.

- Until now, access to the Create Employee Logons screen required EK (Employee Kiosk), with a default level of 8. Starting with this release, access to this screen requires PA (System Admin) level 8.

- If your organization is using Trimble ID to log into Spectrum, there's a new checkbox in System Administration > Installation > System named End Trimble ID session on sign out from Spectrum.Important: This checkbox is selected by default. If you want your users' Trimble ID sessions to remain active even after they sign out of Spectrum, log in and clear this checkbox.
Note: This functionality doesn't apply to:

- Users signing in with social sign-in or with an Active Directory login

- Trimble products which do not yet use Trimble ID

- The Crystal Report Inquiry screen's search options now include Function name, making it possible to query by function name. This enables you to see all the reports that are available on a given report screen.
