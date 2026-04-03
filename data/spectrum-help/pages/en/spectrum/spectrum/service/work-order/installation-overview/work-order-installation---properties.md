---
title: "Work Order Installation - Properties | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/installation-overview/work-order-installation---properties"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/installation-overview/work-order-installation---properties"
---

# Work Order Installation - Properties

The Work Order Installation screen is used by the software administrator to specify how the Work Order
 module should function. The needs of every company are different; use this screen to customize
 the Work Order module to fit your unique needs.
When Work Order Installation is selected from the Site Map > System Administration > Installation > Work Order menu for the first time, the software will beep and a dialog box containing
 the following message displays: CONTROL
 RECORD HAS NOT BEEN CREATED OK TO PROCEED. Once this installation screen has
 been completed and the information saved, the message will not appear again.
Information that appears on the dispatch operator's screen can be set
 through the Description Setup button. The pricing defaults that
 occur during entry of new work orders can be set through the Default
 Selections button.
Installing this module includes specifying how work order labor and materials will post. Some companies job cost at least some work orders, others will need to decide whether to post cost-of-goods sold to the general ledger. This work can be done automatically by the software if specified on this installation screen.
There is also a section on this installation screen for specifying how work order data transfers to the Accounts Receivable module. When work orders transfer to A/R, an invoice is automatically created. The invoice can either be assigned the next number that any A/R invoice would receive, or work order invoices can be given the work order number as the invoice number. Invoices can contain either detailed information from work order, or summarized information.
Field
Description

Use auto-sequenced site numbers?
If this checkbox is selected, then the
 software will automatically provide the next sequential site number; the next
 work order number is maintained in Site File
 Maintenance. If this checkbox is not selected, then the operator
 will be prompted for a unique site number when adding new work orders to
 Spectrum.
Use auto sequenced work order numbers?
If this checkbox is selected, then the
 software will automatically provide the next sequential work order number; the
 next work order number is maintained in the Work Order
 Installation. If this checkbox is not selected, then the
 operator will be prompted for a unique work order number when adding new work
 orders to Spectrum. If the auto-numbering feature is
 used, the first work order number and proposal number will be specified on
 this screen. After installation, the "next" number can easily be checked, as
 the software will maintain that information and display it on this
 installation screen.
Note: Work Orders
 generated from the Service Tech app will always be auto-sequenced,
 regardless of the checkbox setting in this screen.

Require lead source on work order?
Select this checkbox to require lead
 codes for tracking the source of new work order business.
Require equipment code for work order transactions?
Use this checkbox to specify whether
 to allow the Equipment field to be left blank in data
 entry screens when recording work order cost transactions. When this checkbox
 is selected, the Equipment field will be a required
 field in data entry screens like Accounts Payable > Invoice/Credit Memo Entry.
Require component code for work order transactions?
Use this checkbox to specify whether
 to allow the Component field to be left blank in data
 entry screens when recording work order cost transactions. When this checkbox
 is selected, the Component field will be a required
 field in data entry screens like Accounts Payable > Invoice/Credit Memo Entry.
Validate make and model entries?
Use this checkbox to specify whether
 equipment and component Setup fields will require entry of pre-defined make and
 models. When this checkbox is selected, equipment and component setup fields
 will provide a search window and will require entry of make and/or model
 previously set up in Make/Model File Maintenance.
Allow job work orders?
Select this checkbox to allow job work
 orders and show any job labels in various work order screens. When this check
 box is clear, the fields in the Job Cost work order section of the screen will
 be hidden and the following screens will be removed from the menus:

- Work Order Standard Phase Maintenance

- Work Order Standard Phase Listing

- Update Material Costs

- Update Other Charges

- Copy Standard Phase File from JC

- Copy Standard Phase File to JC

Validate work order type
Work order type can be restricted for a
 technician by the following validation options:

- No
 warning Allows any technician to be assigned to any work
 order.

- Warn,
 but allow assignment Allows any technician to be assigned
 to any work order, but if the technician has not been approved for the WO
 type a warning message will appear.

- Disallow assignment of technician This choice will
 prevent assigning a technician to a work order if he or she is not
 approved for the WO type associated with the work order.

WO types for each technician are approved in the Work Order Maintenance > Technician master file.

Validate case type
Work order case types can be restricted
 for a technician by the following validation options:

- No
 warning Allows any technician to be assigned to any work
 order.

- Warn,
 but allow assignment Allows any technician to be assigned
 to any work order, but if the technician has not been approved for the
 case type a warning message will appear.

- Disallow assignment of technician This choice will
 prevent assigning a technician to a work order if he or she is not
 approved for the case type associated with the work order.

Case types for each technician are approved in the Work Order Maintenance > Technician master file.

Next site number
The system is prompting for the next
 site number the software should assign for new sites. Enter the next number the
 software should use during Proposal Entry. This field
 will be hidden if the Use
 auto-sequenced site numbers? checkbox is not
 selected.

Next work order number
The system is prompting for the next
 work order number the software should assign for new work orders. Enter the
 next number the software should use during Work Order Entry. Spectrum features auto-count work order numbers if the Auto
 sequenced work order number field is selected. It is recommended that this
 number be initialized at some point significantly higher or lower than work
 order numbers presently in use so that auto-sequenced work order numbers will
 not interfere with work orders already issued. For example, if work orders are
 currently numbered 1500 to 1600, you may choose to set the next W/O number to
 5001. Alternatively, if work orders are presently numbered in the 80000 range,
 you may elect to commence the Spectrum work orders at 10001.  Entry in this field is irrelevant if your company does
 not use auto-sequenced work orders. This feature may be utilized at any time
 if the above Auto sequenced work order number field is selected.


Work order price type default
Click to specify the type of pricing
 most frequently used for work orders:

- Time +
 materials

- Flat rate

When new work orders are entered, the pricing type
 selected here will be the default, but either option may be selected at that
 time. Having the most frequently used option default makes entry quicker for
 the operator entering new work orders.

Accounts receivable invoice #
The system is prompting you to decide
 whether the A/R invoice number will be the same as the Work order number or
 will be automatically assigned the next sequential invoice number when a
 completed work order is transferred to Accounts Receivable Invoice Entry. If you select
 Work order, the
 work order and its subsequent A/R invoice will have a matching number. If you
 select Auto invoice
 number, the software will assign the next available invoice
 number (stored in the Accounts Receivable Installation).
Job cost work order

Default job to work order number?
The system is prompting you to decide
 whether to default the job number to the work order number when adding new work
 orders. If all of your work orders are job costed, this feature allows you to
 assign the job number to match the work order, select this checkbox if the job
 number should default from the assigned work order number. If several work
 orders may relate to a single job, you may want to leave this checkbox blank
 and utilize sequential work order numbers. If none of
 your work orders are job-related, entry in this field is irrelevant.


Update material and other costs to job cost transaction entry?
The system is prompting you to decide
 whether work order entries will interface with Job Cost Transaction
 Entry. If this checkbox is selected, when a job cost work order
 is completed the associated job costs will automatically be recorded in
 Job Cost Transaction Entry. It will then be necessary
 for the Operator to update these job cost transactions using Cost
 Transaction Selection. If this checkbox is not selected, job
 cost files will be unaffected by work order activities. Select this checkbox if you are using job requisitions and you need to
 transfer non-stock material costs to Job Cost. In this case, the non-stock
 costs will be transferred via Update Material Cost
 and stock items will transfer to Job Cost via the job requisitions.
Entry in this field is irrelevant if your office does not
 enter job work orders.

Post material transactions as inventory type (IC)
When this checkbox is selected, the
 job cost transaction will be posted as an IC transaction type.Note: This option is only available when the 'Update
 material and other costs to Job cost Transaction entry' option is
 selected.

Default work order entry type
If this checkbox is selected, then the
 operator will be provided the option during Work Order
 Entry to reference job cost. If a job is specified, then the
 software will default certain information from Job File
 Maintenance (such as name and address), phases and cost types
 will be validated, and actual costs associated with the work order will be
 recorded in job cost files when the work order is completed. It will be
 possible to enter non-job work orders even if this checkbox is selected. When
 this checkbox is selected, billing amounts will transfer automatically to job
 cost files through Work Order Entry. Corresponding work
 order costs will transfer to Job Cost through Payroll Time Card Entry
 processing and Accounts Payable processing of materials in
 Invoice/Credit Memo Entry or (optionally)
 Update Material Costs.  If Job
 Cost module is not installed or if work orders will never interface with job
 cost in this company, then this field should be left blank. If this field is
 not selected, then the cursor will skip over the job-related prompts during
 work order entry.

Labor cost type
Enter the default cost type to be
 offered during Labor Hours Entry. This cost type is set
 up in Job Cost > Cost Type File Maintenance. This default cost type may be over-written during labor hours
 entry if desired.  Entry in this field will be used by
 the software only when companies are engaging in Job Cost work orders.


Material cost type
Enter the default cost type to be
 offered during Work Order Material Entry. This cost type
 is set up in Job Cost > Cost Type File Maintenance. This default cost type may be over-written during material
 entry if desired.
