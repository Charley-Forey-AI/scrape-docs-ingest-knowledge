---
title: "Customer Material Contract Maintenance - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/materials-management/spectrum-menus/maintenance-overview/customer-material-contract-maintenance/customer-material-contract-maintenance---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/materials-management/spectrum-menus/maintenance-overview/customer-material-contract-maintenance/customer-material-contract-maintenance---field-descriptions"
---

# Customer Material Contract Maintenance - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Fields
Descriptions

Customer
On the New Customer Contract window, enter or search for the customer code. Entry is not allowed if the status of the customer code is Not used.
The Customer invoice parameters allow you to override the Materials Management Installation screen. If one customer will pay more promptly if you generate invoices under a specified dollar amount, this screen allows entry of that amount. If the invoice amount in the Batch exceeds this, the software will automatically create more than one invoice for that batch posting.

Customer's job
This optional field is used for different pricing schedules for different
 sales purposes. Enter or click the arrow to open the Search Material
 Contracts for Customer simple search window.

Properties

Customer's job desc
Enter the job description for this customer. This description will display in various screens throughout the software.

Price level
The price level defaults from the material level in Accounts Receivable Customer File Maintenance. This level can be overwritten, as needed.
The price level is used in conjunction with the inventory item price levels to default the unit price for an item in New/Edit Scale Ticket.
This price level is not used in Order Processing order/invoice entry to determine the sell price.

Separate freight line item on invoices?
Select this checkbox to transfer freight as a separate billing line item.
If this checkbox is clear, freight lines cannot be bundled on invoices from Materials Management if the tax flags or the G/L account codes on the lines are different.

Misc. charge type
Enter the miscellaneous charge type: Fixed, Rate, Percentage, or none.
Miscellaneous charges can also be overridden from the Materials Management Installation. The source of the Sales tax code can also be changed from the installation setup; up to 15 characters are allowed.

Misc. billing amount Misc. cost amount
Enter the miscellaneous billing and cost amounts.
Spectrum uses this amount when applying miscellaneous charges during the scale ticket update to Order Processing. If this field is blank, Spectrum applies any miscellaneous charges defined in the non-job-specific customer contract. If there is no non-job-specific contract, Spectrum applies the miscellaneous charges defined in the Materials Management Installation screen.

Msc. charge category
Enter or search for the miscellaneous charge item category code.

Nonstock misc. item Nonstock misc. desc
Enter the miscellaneous charge non-stock item code and description.

Nonstock misc. u/m
Enter the miscellaneous charge unit of measure (UM); for example, yd=yard, ea=each, pd=pound, and so forth.

Sales tax code by Tax code
Enter whether the sales tax code will be based on the Warehouse, Customer, or Customerjob.
If Customer Job is selected, the Tax code field becomes available. Enter or search for the sales tax code.

Invoice dollar limit
Enter the dollar limit for customer invoice generation (within each batch).

Billing address

Print alternate address on invoice?
Select this checkbox to apply an alternate billing address to the selected customer contract.
 If this checkbox is selected, the Bill-to code field must be completed.

Bill-to code
Enter or search for the alternate Bill-to code that you want to apply to the selected customer contract. This field must be completed if the checkbox above is selected.

Name
The addressee name for the selected billing address displays. If you selected checkbox above, then the alternate billing addressee name will display based on the code entered in the Bill-to code field. Otherwise, the billing addressee name will default from Customer File Maintenance.

Address
The first line of the address for the selected billing address displays. If you selected the Print alternate address on invoice checkbox, then the alternate billing address will display based on the code entered in the Bill-to code field. Otherwise, the billing address will default from Customer File Maintenance.

Buttons

Special Pricing
Click to view the [Customer Special Pricing window](/en/spectrum/spectrum/materials/materials-management/spectrum-menus/maintenance-overview/customer-material-contract-maintenance/customer-special-pricing-window).

Hauler Rates
Click to view the [Hauler Special Rates window](/en/spectrum/spectrum/materials/materials-management/spectrum-menus/maintenance-overview/job-material-contract-maintenance/hauler-special-rates-window).
