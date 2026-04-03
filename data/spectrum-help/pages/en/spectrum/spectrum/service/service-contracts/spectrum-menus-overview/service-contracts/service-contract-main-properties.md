---
title: "Service Contract Main Properties | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/service-contracts/spectrum-menus-overview/service-contracts/service-contract-main-properties"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/service/service-contracts/spectrum-menus-overview/service-contracts/service-contract-main-properties"
---

# Service Contract Main Properties

Use this tab to set up and manage general contract, maintenance work order, notes and exception information related to the service contract.
To open this screen: from the Service Contracts Info Bar, select Properties > Main.

- To create a new service contract, select a site code and enter a new contract code to enable the rest of the fields on this tab.

- To cancel a service contract, change the contract amount and number of visits based on the work performed, and review the earning table for the contract. Changes to the earned revenue table will take effect when the earned revenue update is run.

Fields/ButtonsDescriptions
Contract
DescriptionEnter the new contract description, or press F4 to select from a list of available descriptions.
Contract typeEnter the contract type (for example, Inspection, Labor, Full, and so forth), or press F4 or double-click on this field to select from a list of available contract types.
SalespersonEnter the salesperson code for this contract. A lookup window is available for viewing valid salespeople.
Start/End dateEnter the date range for the service contract.
This field prevents you from adding a start date later than any un-invoiced scheduled billings.
If the current number of scheduled visits does exceed the contractual total for the specified contract date range, you can edit the contract date range or select the 'Adjust visit total' checkbox that displays in order to set the total visits equal to the number currently scheduled.

Maintenance work orders
Work order typeThe work order type defaults from the Type field in the Work Order > Work Site Address File Maintenance > Properties window.
Press Enter to accept the system default, enter a different work order type, or press F4 to select from a list of available work order types (note that equipment and job cost types are not permitted).

Material levelEnter the material level number (0-5) as defined in the Work Order Material Item Code File Maintenance or the Inventory Item File Maintenance screen.
Labor levelEnter the labor level number (0-5) as defined in the Work Order Billing Rates File Maintenance screen.
Material markupEnter a material markup code in this optional field, or press F4 to search for material markup codes. This field is intended to remain blank, unless an override to the code specified in the Site File Maintenance, Customer File Maintenance or Work Order Installation screen is needed.
Include contract notes?Select this checkbox to include all contract notes for this service contract when the Contract Work Order Process update is run.
Include contract exceptions?Select this checkbox to include all contract exceptions for this service contract when the Contract Work Order Process update is run.
Contract status
Current statusThis view-only field displays the status of the service contract, based on the current date.
Customer P.O.Enter the customer purchase order number, up to 25 characters. Entry not required.
Proposed service contract?If this is a proposed contract, select this checkbox to re-calculate and re-display the 'Current status' checkbox.
Proposal issued dateEnter the proposal issue date, or use this field as a memo entry field if this is not a proposed contract.
Honor forEnter the number of days this proposal should be honored for as of the proposal issued date.
Proposal expirationThis field is calculated by adding the number of 'Honor for' days to the 'Proposal issued date' field. A blank expiration date means the proposal has NOT expired.
Profit summary
Earned revenueOpen the Service Contract Earned Revenue page in context to the current contract.
Work order revenueOpen the [Service Contract Work Order Revenue](/en/spectrum/spectrum/service/service-contracts/spectrum-menus-overview/service-contracts/service-contract-work-order-revenue) page in context to the current contract.
Total revenueThis is the Earned revenue amount plus the Work order revenue amount.
Total costThe total costs, including company equipment costs, for the service contract are displayed beneath this field.
Select the hyperlink to open the [Work Order Cost History](/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/inquiries-overview/work-order-cost-history) inquiry screen in context to the current contract.

Gross profitThis is the Total Revenue minus Total Cost.
