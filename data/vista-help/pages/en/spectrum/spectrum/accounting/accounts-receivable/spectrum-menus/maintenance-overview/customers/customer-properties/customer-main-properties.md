---
title: "Customer Main Properties | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/customers/customer-properties/customer-main-properties"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/customers/customer-properties/customer-main-properties"
---

# Customer Main Properties

Use the Customer Main Properties screen to display general information about the customer, including address, phone number, primary contact, customer status and customer attribute settings.

##  Note about Customer Workflows:

If the Workflow module is installed and active in this company, a workflow menu displays at the top of the info bar to guide you through the process of adding a new customer. Complete the fields on this screen and click the Next button on the Workflow info bar to move to the next step.

- The Currently Assigned To You section will show any customer workflows that are currently open and require further setup. Click the tooltip icon to search current workflow assignments and switch to a different customer.

- If the workflow is overdue, the Due by date will be highlighted in red.

- The Workflow info bar will display a short description of this step and instructions for this screen.

- Click the tooltip icon to review history and add notes to this workflow.

When the last workflow step is completed, the Customer status will switch to 'Active'. Incomplete workflows will continue to display on the My Current Workflow Assignments dashboard app until completed.
Field
Description

Customer code
The selected customer code displays in this field. If desired, change the customer code.
Note: This is the only screen where the customer code can be changed.

Alpha reference
The first six characters of the customer's full name display as the customer's alphabetical reference name, which will be used for sorting purposes. Press Enter to accept the displayed alpha reference or enter another reference if a different one is desired.

Customer type
The customer type is used to group customers by function, or by any other desired classification.
Sample customer types might be SUB for subcontractor, UTIL for utilities, O for office, and GEN for general.
Press Enter if no type will be entered for the customer. Some of the available reports may be run for specific types of customers.
Note: You can also use organization attributes to assign unlimited pre-defined identifiers to the vendor.

Communication
Enter the specified customer's address, telephone and FAX numbers, contact email and website (if available).

Primary contact
The customer's primary contact name and phone number is listed in this section. Contact-specific information is entered on the [Customer Contacts](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/customers/customer-properties/customer-contacts) screen.

Resale
Enter the resale certificate number for this customer and the date the resale certificate expires.

Attributes
Any attributes assigned to the customer will display in this field. Click the Build button to assign multiple attributes to a customer.
If attributes are present but none are assigned to the customer, a window will open allowing you to select attributes.

Work order warning
Enter a message or warning for work order if the Work Order module is present and a warning message is needed in Work Order Entry.

Status
If Inactive is selected and then an attempt is made to assign a new transaction to this customer, the following message displays: Warning – customer code entered has inactive status. To continue, click OK and proceed with entering the new data.
If Not used is selected and then an attempt is made to assign a new transaction to this customer, the following message displays: Error – customer code entered is not available for use. This error message disallows further data entry.
Note: Access to this field is limited to Operators who have the minimum required
 security level. The cursor will not advance to this radio group if the
 Operator is not authorized to access it. The radio group's data is
 visible to all Operators, but they cannot access the radio group to
 make any changes without security authorization. Security for this
 radio group is set in the Function Security Maintenance > Function Links Security window. If a workflow is in progress, this field will
 be unavaible.
