---
title: "Pay When Paid | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/cash-receipts-journal/pay-when-paid"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/cash-receipts-journal/pay-when-paid"
---

# Pay When Paid

## How to track Accounts Receivable Payments Received to Trigger Paying the Subcontractors

Spectrum currently has a feature to bill monthly draw requests based on monthly costs which also give you a way to track payments to trigger paying the subcontractors.
To make this procedure work, create a one-to-one relationship between revenue
 and cost. The relationship is established using the Accounts Receivable Billing
 Items feature. When the Accounts Receivable contract is created in Accounts Receivable > Contracts, the schedule of values is broken down using billing items. Those
 same billing items are then attached to the individual phases in Job Cost > Maintenance > Phases.

## Accounts Receivable > Contracts

1. Click New. Enter a customer and job code.

1. Complete the Contract Main Properties,
 Defaults, and the Schedule of
 Values screens; all can be accessed from the
 Contract Info Bar. (See example: hover on image
 to enlarge.)

1. After the Accounts Receivable contract is set up and the contract details are
 complete, proceed to Job Cost > Maintenance > Phases.

## Job Cost > Maintenance > Phases

1. Add the phases to the job and attach the corresponding billing items to each
 phase in the Phase Default screen. Phases used to
 track subcontracts will also have a billing item attached in Job Cost > Maintenance > Phase. The billing item will default in when setting up the
 subcontract.

## Accounts Payable > Subcontracts

1. Set up the individual subcontracts in Accounts Payable > Subcontracts. When in the subcontract detail screen, assign the phase to
 the subcontract and the billing item defaults.

1. At this point you will proceed to Accounts Receivable
 and create a draw request billing (date the draw request for the time range
 of the billing).
Note: If the contract has been previously billed, it is not necessary to reverse everything out and start over. As long as the one-to- one relationship exists, this process can be started at any time. Be sure the Accounts Receivable billing items are assigned to the phases and an open draw request exists.
Cost is booked to the individual phases. Accounts Payable invoices are added and updated. Payroll time cards are processed and updated. Subcontract billings are added and updated.

## Accounts Receivable > Data Entry > Draw Request Cost Selection

1. This screen is used to flag costs for the specific draw request application. This will flag records in the Job Cost History file with the application number and will write to the draw request record. Use of this screen will allow you to select and deselect job history records based on cost type, phase, and so forth. Total costs will display on the screen.

1. With a draw request already created, enter a selection for the specific job
 number, customer code, and draw request application number. Selections can
 be based on cost type, phase, transaction types, vendor codes, employee
 codes and/or items for a date range. Make your selections and
 Save.

1. Once the selection is made, click the Totals button.
 The total cost posted to the job within the dates specified will display.
 Further drill down is available by clicking the
 History button. (See example, hover over image to
 enlarge.)

## Draw Request by Percent Markup-Optional

Once the selection is made, the costs will automatically transfer to the draw
 request to be billed this period. Using the Percent Markup
 feature is optional. Use this screen to add a percent markup for calculating the
 amounts to be billed for an item based on the costs associated with the current
 application. Alternatively, you can enter the amount to be billed, and the percent
 markup will automatically be calculated. This billing method is intended for use
 with fixed price contracts only.
In order to perform draw requests using percent markup, first enter all valid
 information in the Draw Request Cost Selection screen. This
 associates the job cost history records with the particular draw request that is
 being processed. Only billing items on the Draw Request Billing
 Entry screen will appear on the [Draw Request by Percent Markup](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/draw-request-cost-selection/draw-request-by-percent-markup) screen. Also note that if the billing item is blank in
 the phase file or if there are no costs associated with a billing item for this
 current application, it will not appear on this screen.
Billing items can be added to the phase file at any time. Cost information for the current application calculate based on the billing item in the phase file at the time Draw Request Cost Selection is performed. It might be necessary to deselect costs, add the billing item to the phase files, and perform the cost selection again.
In the [Billing Entry by Percent Markup - Billing Detail window](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/billing-entry-by-percent-markup---billing-detail-window) screen the cost per phase defaults based on the date range specified during the Select process. At this time a percent markup can be added phase by phase and Spectrum will automatically calculate the Proposed JTD billed this period or you can manually enter a Billed amount this period.

- If no markup is entered, the cost per phase will automatically become the 'this period' on the current application.

- Click OK in the Percent Markup
 screen. The proposed billed this period automatically populates the This
 Period on the draw request.

- Any additional modification to the draw can be performed in Accounts Receivable > Data Entry > Draw Request prior to the update. Once the Draw Request Update is
 performed and the Sales Journal is updated the billing of this application
 is complete.

How do I determine what vendors and subcontracts are to be paid once a payment is received?
The Job Cost History Report and the Job Cost Analysis Report offer selections based on customer and draw application number. Proceed to Job Cost  >  Reports  >  Job Cost History or Job Cost Analysis Report. Enter the job number. The report can be run for all phases and cost types or individual subcontracts to be paid based on the phase code and subcontract cost type. Enter the date range of the billing period. To track what costs were associated with the draw application, enter the Customer Code and the Application #.
Preview the report. The report will show only those job cost history transactions that have been flagged for a specified billing period (customer and draw request #). Use these reports to determine which subcontracts and/or vendors are to be paid.

- When a check has been received from the customer for this billing, a
 Pay-when-paid subcontract worksheet can be printed for either fixed price or
 unit price contracts, based on an option found on the Accounts
 Receivable Installation screen.

- The Subcontract Payment Worksheet will print automatically upon clicking
 Preview. The payment worksheet provides a
 convenient method for determining when a payment for an AIA draw application
 is associated with a subcontractor payable for the same job and application,
 and includes the payment amount and invoice balance information.
Note: No reports will print if no applicable contract payments are included on the Cash Receipts Journal.
