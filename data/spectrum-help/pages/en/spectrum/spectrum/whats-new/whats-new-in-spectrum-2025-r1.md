---
title: "What's New in Spectrum 2025 R1 | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/whats-new/whats-new-in-spectrum-2025-r1"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/whats-new/whats-new-in-spectrum-2025-r1"
---

# What's New in Spectrum 2025 R1

The key updates and enhancements included in the Spectrum 2025 R1 release.

## Trimble Assistant for Spectrum - Beta Release

Spectrum now
 includes a beta version of the Trimble Assistant chat agent. Use this assistant to ask specific
 questions about the tasks you can perform in Spectrum. To start a chat, select the Trimble Assistant icon  in the navigation bar. See [About Trimble Assistant - Beta](/en/spectrum/spectrum/whats-new/about-trimble-assistant---beta) for
 details.
Important:Trimble Assistant is trained only on
 Spectrum-related content
 on the Trimble Help website. The assistant does not have access to any of your
 company's data or any data within the Spectrum database.

Tips for chatting with Trimble Assistant:

- Trimble Assistant is still learning. To improve results, ask
 specific questions. If you do not get a helpful answer the first time, try
 rephrasing your question and asking it again.

- Trimble Assistant is looking
 for feedback. Select the Rate button in the lower right of the chat window to rank
 and comment on the answer to your question. Your feedback will be used to
 improve the assistant and documentation as needed.

- Trimble Assistant is enabled by default. To turn off the
 assistant, go to System
 Administration > Installation > System, and clear the Enable Trimble Assistant? checkbox.

## Trimble ID Sign-in is now the default

Now when you sign in to Spectrum, instead of encountering the Spectrum sign in screen to sign in using your Trimble ID, you arrive directly to the Trimble sign in screen.

As before, use your Trimble ID to sign in.

## Jump directly into Trimble Pay™

To improve workflow efficiency for frequent Trimble Pay users, there are two new ways you can easily navigate there from your Spectrum application:

- A new option in the Site Map under Accounts Payable > Data Entry.

- A new Trimble Pay Approval button in the Accounts Payable > Data Entry > Invoice Approval window.Note: Access to these shortcuts requires the user to have Accounts Payable security equal to or greater than the standard level of 4.

## Streamlined ePayments Processing

The ePayments functionality has been enhanced to streamline the payment processing workflow. You can now send your electronic payment files directly to Corpay without first needing to download or upload them.
Aside from some one-time setup steps, there's no change to your process. These new items support this feature:

- Set up the direct connection using new fields in System Administration > Installation > Accounts Payable > Printing. After entering the required values, use the new Connection Test button to verify.

- In the Generate ePayments Export File window:

- When the direct connection is set up and validated, a confirmation note displays.

- When you select Continue as part of the existing process, Spectrum sends the file directly to Corpay via their secure API.

- Once the payment file is successfully transmitted, a note displays to tell you so.

- An error message displays if the connection information is not entered correctly (over in the setup screen) at the moment you select Continue.

See also [Generate ePayments Export File](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/generate-epayments-export-file).

## Enhanced 'Update Vendor' Web Service

The Update Vendor web service now supports ePayments as a payment type.
It now supports five types:

- (P) Print Check

- (S) Send electronic pre-note

- (E) Electronic payment

- (C) Comdata

- (V) ePayments

The same requirements apply for this new payment type as for the others. See the Assumptions and Dependencies section in [Update Vendor](https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-payable-services/update-vendor#:~:text=On%20the%20Payment%20Setup%20page).

## Usability Improvements

Add Contract number to Advanced Search for Job
Some clients use the Contract # field to store customer purchase order numbers. For a more efficient way to search for jobs using the contract number, the Search Jobs window now includes the Contract # field in its search criteria. The Advanced Search options also include this functionality, providing greater flexibility in locating specific jobs.
Aatrix Search Window Improvements
The naming convention for Aatrix reports within the search window has been updated for clarity. The report names have been modified to better align with the corresponding report names found on the Aatrix website, making it easier for users to identify the correct reports.
Reverse Earned Revenue Start Screen Improvement
To reduce user confusion when using Service Contract > Data Entry > Reverse Earned Revenue, the start screen provides clearer context.
Update Detail Billing Selection Entry Screen

- Customers who process high volumes of transactions for their Time & Material jobs now have more flexibility in the Detail Billing Selection window with a new Selections option. This option becomes available immediately after you enter a job number, allowing you to filter data more effectively from the outset.

- Building upon the previous enhancement, the selection criteria within the Detail Billing Selection screen is expanded to provide more granular filtering capabilities. The new From work date and To work date fields enable filtering employee time entries based on specific date ranges. This allows for more targeted searches when locating employee work records.

Improved Payroll Processing Completion Indicator
In the Payroll Payment Processing window, the green check mark will now appear only after the check processing is fully complete.
During payroll check calculation, if there is any reason the process doesn't complete, the check mark won't appear.Important: Despite this improvement, you should still review your payroll check calculation reports for accuracy after the process is finished.

Employee Code Change Utility History
To improve auditing and ease of use, the Change Employee Code utility now has a history log.
All employee code changes processed through this utility will now be recorded in a new table. With the new Employee Code Change History report, you can review these changes.Note: Tracking of employee code changes will only begin after this update is applied. Historical changes prior to this update aren't available in the new history report.

Year-End Clear Warning Message
The Year End Update screen now has additional information and warnings to guide you through the process and help prevent potential issues that could arise from improper processing.

## Spectrum BI is upgraded to Trimble Analytics

We've upgraded all organizations to Trimble Analytics. You can read about the benefits of this change at [Spectrum BI and Team Reporting to Trimble Analytics Upgrade](/en/spectrum/spectrum/trimble-construction-one-analytics/spectrum-bi-and-team-reporting-to-trimble-analytics-upgrade).
There are a number of resources to assist you as you make the transition.

- For training, go to [Building Power BI reports in TC1 Analytics](https://academy.viewpoint.com/learn/external-ecommerce;view=none;redirectURL=?ctldoc-catalog-0=se-%22Custom%20Power%20BI%22)

- For Help content, see [Trimble Analytics](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId::trimble-construction-one-analytics:trimble-construction-one-analytics)

With this release, the Business Intelligence menu options have been removed and are no longer accessible.

## Updated Employment Utilization Report

The Federal government has reinstated the Monthly Employment Utilization Report, Form CC-257. Spectrum's Employment Utilization Report is now updated to provide the necessary data for this form.Important: This update is provided to assist users in meeting potential state and local government requirements. Please consult with your legal resources to determine your specific compliance requirements regarding this report, as it was previously rescinded under Executive Order.

In these windows, the Employee Work Class dropdown now includes the additional work class option of 'Foreperson'.

- Employee Main Properties in Payroll > Maintenance > Main Properties.

- Applicant Main Properties in Human Resources > Applicants > Main Properties.

Report Modifications

- The report start screens for both the Payroll and the Confidential Payroll versions now reflect the recommended terminology.

- The report now displays both the work hours of employment and the number of employees.

- The EEO/Work Classifications in the report now include 'Forepersons' and 'Journey Worker'.

- A new section has been added to the report that totals both the EEO Class and the Work Class.

- The Employee Master Report and the Employee Listing report are also updated to reflect the new Work Class.

## General Ledger Updates

Removal of G/L Error Recovery from Command Prompt
As part of ongoing efforts to streamline your Spectrum application and improve usability, the G/L Error Recovery menu option has been removed from the command prompt. This change follows the relocation of all other command prompt-based menu items in previous releases.
Move Rebuild Balance File from Detail File
The Rebuild Balance File from Detail File utility, which is occasionally needed to correct discrepancies between the general ledger entries and the balance file, has been relocated for easier access. Previously accessible only via the command prompt, this utility can now be found under General Ledger > Utilities > Rebuild Balance File.Access to this utility is restricted to users with the appropriate security permissions.

## Easily print all Subcontract CO forms for a given Owner CO

Identifying and printing all subcontract change orders associated with a single owner change order can be a time-consuming process.
With the new Owner change order field in Accounts Payable > Reports > Subcontract Change Order Form, you can generate a report containing all subcontract change orders linked to the specified owner change order.

## Spectrum 2025 R1 Bug Fixes

This release includes fixes to customer-reported issues. To see the list:

1. Log in to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues?tabset-d4f10=2) of the Viewpoint Customer Portal.

1. Make your selections in the product and module filter options.

1. In the Fixed in Version field, enter 2025 R1.

1. Select Apply Filters
