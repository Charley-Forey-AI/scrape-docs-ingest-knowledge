---
title: "About the PM Approved Change Orders Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form"
---

# About the PM Approved Change Orders Form

Use this form to create and maintain approved change orders
 (ACOs).
An approved change order can represent a pending change order that has been approved, or it can be change order that was approved outside of the application.
Click [here](/en/vista/vista/project-management/change-orders/change-management---overview) for an overview on change orders.
Tasks
Unapprove a change order item
Select a PCO item in the lower portion of the form and click the Unapprove Item button to unapprove the PCO item on the ACO. This will remove the change order item from the ACO, and enable it on the [PM Pending Change Orders ](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form) form . The status of the PCO item will also change to:

- The default beginning status defined using the Default
 Beginning Status field on the Info tab of the PM Company
 Parameters form.

- If you haven't defined a default beginning status, the system will use the
 first status found in the PM Status ID form that is set up with a beginning
 status, and is associated with the pending change order document category. The
 system will determine which status is first using the Status
 Code field on the PM Status IDs form - alphabetical sort with
 numbers coming before letters.

Note: Change order items with interfaced subcontract and/or
 material detail cannot be unapproved. If a change order item has been interfaced to
 Job Cost, it must first be deleted from the ACO in Job Cost before it can be
 ‘unapproved’ here.
Open/view subcontract detail
Select Tasks > Open
 Subcontract Detail  to open [PM Subcontract Detail](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form) and view the subcontract
 detail associated with the approved change order.
Click [here](/en/vista/vista/project-management/materials/pm-material-detail-form) for more information about the PM Subcontract Detail form.
Generate Detail
The Generate Detail option on the Tasks menu is used to add phase/cost type detail to a change order using the phase/cost types set up on a contract item. This can reduce data entry and save you some time when creating change orders.
Select Tasks > Generate
 Detail and all phases/cost types linked to the contract item on the CO item
 will be added to the change order. You can change or delete the phase/cost types
 that do not apply.
The values calculated for each phase/cost type will depend on the following:

- If the phase/cost type unit of measure (UM) is equal to the contract item
 UM, the same number of units specified for the change order item will be added
 for the phase/cost type.

- If the phase/cost type UM differs from the contract item UM, but is not LS,
 the units for the phase/cost type will be calculated as follows: (CO Item Units / Curr Contract
 Item Units) x Curr Phase/CT Units = CO Item Phase/CT Units

- If the phase/cost type UM differs from the contract item UM and is LS and it
 is a PCO item, all amounts will be zero since there is no amount entered for a
 change order item on which to base the calculations.

- If the phase/cost type UM differs from the contract item UM and is LS and it
 is an ACO item, the amount of the phase/cost type will be calculated as follows:
 (CO Item Amt / Curr Contract
 Item Amt) x Curr Phase/CT Amt = ACO Phase/CT Amt
If you are generating detail
 for a PCO item, the process will include add-on phases; however, they will
 be generated with zero amounts. Since add-ons are calculated for the pending
 change order item based on the phase/cost type detail, the amounts for these
 phases should be left at zero. Another option would be to delete the add-on
 phases after they have been generated.

Open/view material detail
Select Tasks > Open
 Material Detail  to open [PM Material Detail](/en/vista/vista/project-management/materials/pm-material-detail-form) and view the material detail on
 the approved change order.
Click [here](/en/vista/vista/project-management/materials/pm-material-detail-form) for more information about the PM Material Detail form.
Initializing Phases to Job Roles
If you are using the job roles functionality and
 have assigned roles to projects/jobs using [PM
 Projects](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form) or [JC Jobs ](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form), you can use the Job Phase Roles
 Initialize option in the File menu to initialize phases to roles assigned to a
 project/job. This will open [JC Job Phase Roles Initialize](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phase-roles-initialize-form).
Although this functionality does not directly impact pending or approved change orders, it does allow you to assign any phases added to a change order to job roles. Click [here](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form) for more information about job roles and initializing phases to job roles.
Send an email - Create and Send
 The [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature allows you to generate
 documents and send them to project contacts. For example, you can use this feature
 to create RFIs, submittals, and change order documents and then email those
 documents to the contacts on a project.
Click [here](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) for more information on the Create and Send feature.
Three options display when you click on the Create and Send () icon:

- Send Message - Select this option to send an email to a list of project
 contacts. Using this option you can also generate a document, include an
 attachment, and/or generate a report. [More](/en/vista/vista/project-management/create-and-send/about-sending-messages)

- Send Document - Select this option to generate a project document or report,
 and email it to a list of project contacts. Using this option you can also
 include an attachment. [More](/en/vista/vista/project-management/create-and-send/about-sending-documents)

- Send with Transmittal - Select this option to generate a project document
 and transmittal, and email those documents to a list of project contacts. Using
 this option you can also include an attachment and/or generate a report. [More](/en/vista/vista/project-management/create-and-send/about-sending-with-transmittal)Generate a report
Some of the PM module forms do not have a related
 document template, for example the [PM Approved Change Orders
 ](#ID-00022638--en__ID-00022638), [PM Purchase Orders](/en/vista/vista/project-management/materials/pm-purchase-orders-form), and [PM Punch List ](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-punch-list)forms. Generally you will use
 the Create and Send feature on these forms to generate reports and then
 email those to a list of project contacts. For example you can use the
 Create and Send feature to generate a daily log report and then send it to a
 list of project contacts.
Why doesn't the Create and Send () icon display on the form?
Note: The Create and Send () icon will not display
 on the form if it has been disabled using [PM Create & Send Settings](/en/vista/vista/project-management/create-and-send/pm-create--send-settings-form) form (Info
 tab> Deactivate Document Create and Send
 Feature box).

Create a list of contacts that should receive change order document - Distribution tab
Overview
When a new communication is created using the Create and Send feature (), the contacts on this tab are automatically added to the communication. For example if a project contact should be included in any communication about an RFI record (emails, RFI documents, change order reports, etc.), you should add that project contact to the Distribution tab of the RFI so that they are automatically added to any communication.
Contacts are automatically added to this tab in two ways

- When a project contact is included in a Create and Send communication - When
 a project contact is included in a Create and Send communication, the system
 automatically adds that contact to the Distribution tab. For example if you
 launch the Create and Send feature using an RFQ record, the project contacts
 added to the email using the To, Cc,
 and Bcc fields will also be added to the Distribution tab of the PM
 Request For Quote form. When a new email is created for that RFQ using the
 Create and Send feature, the project contacts set up on the Distribution tab
 will automatically populate in the To, Cc,
 and Bcc fields on the email.

- When a project contact is set up as a distribution default - The [Assign Distribution Defaults](/en/vista/vista/project-management/create-and-send/pm-assign-distribution-defaults-form) feature
 automatically adds contacts to the Distribution tab if they are setup as a
 default contact for the document type associated with the form. For example, if
 a project contact is set up to receive all documents and correspondence dealing
 with RFQs, that contact will by default be included on the Distribution tab of
 any RFQ document. [More](/en/vista/vista/project-management/create-and-send/pm-assign-distribution-defaults-form)Manually add
 contacts to the Distribution tab
You can also manually add contacts to the Distribution
 tab.

1. Add contacts to the
 Distribution tab to create a list of contacts that should receive documents
 generated using the Create and Send feature.There are two ways to add
 contacts to the tab:

- Drag and Drop - By default the Project
 Firm Contacts form displays when you open the Distribution tab. The Project
 Firm Contacts form displays a list of contacts associated with the project
 using the Firms tab in [PM
 Projects](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form). Drag and drop a contact from the Project Firm Contacts
 form to the Distribution tab to add the contact. Note: The Project Firm Contacts list can also be
 accessed by selecting View > Project Firms
 List.

- Manually enter the information - Enter
 contact information into the grid to manually to add a contact to the
 Distribution tab. If the contact is not already associated with the project,
 a message will display when you save the record. Select Yes to add the contact to the distribution list and to PM
 Project Firms. Select No to add the contact to
 the distribution list only. The Project Firm Contacts form doesn't display

The Project Firm Contacts form
 displays when the Distribution tab is opened and the Always Show
 Form box on the Project Firm Contacts form is checked. The
 selection in the Always Show Form box only
 affects the currently selected form (for example PM Request For Information,
 PM Issues, etc.) and it only applies to your user account.
To view the Project Firm
 Contacts form when the Always Show Form box is
 not checked, open the Distribution tab and select View > Project Firms List from the toolbar at the top of the form.

1. Verify that the
 preferred method of correspondence is correct.

1. Use the Send
 Type field to select how the contacts should be included in the
 communication. The [Create and Send ](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature will generate a unique
 document for each contact with a send type of To.

1. Check the Send box for each contact in the grid that should receive the
 communication. If this box is not checked, the contact will be excluded when
 generating documents using the [Create and Send ](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)feature.

Additional Information
ACO Status field
The status of the ACO displays in the upper portion
 of the form next to the ACO field and totals.
An ACO can have one of the following statuses:

- No
 Detail Records - There are no change order items on the ACO.
 Items are added to an ACO using the lower portion of the form.

- Approved - There are items on the ACO, and the ACO has not been
 added to a contract change order(CCO). ACOs can be added to a CCO using [PM Contract Change Orders](/en/vista/vista/project-management/change-orders/pm-contract-change-orders-form).

- Pending Contract Change Order - The ACO has been added to a
 contract change order (CCO), and that CCO has not been approved. By default you
 will not be able to interface the ACO until the CCO has been approved. CCOs are
 approved using the Approve button on [PM Contract Change Orders](/en/vista/vista/project-management/change-orders/pm-contract-change-orders-form).

Note: An ACO can only be interfaced when the Ready For
 Accounting box on the Info tab in the upper portion of the form is
 checked. When an ACO is added to a CCO, this box will be unchecked so that the ACO
 cannot be interfaced. If you need to interface the ACO before approving the CCO, you
 can check the Ready for Accounting field on ACO
 and then interface it using [PM
 Interface](/en/vista/vista/project-management/setupmaintenance/pm-interface-form). The status of the ACO will stay as Pending Contract
 Change Order until the CCO is approved. Click [here](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form/field-definitions-pm-approved-change-orders-form#ID-00022801--en) for more information on the Ready For Accounting field.

- Approved Contract Change
 Order - The ACO has been added to a contract change order,
 and that CCO has been approved.

- Approved and Interfaced -
 The ACO has been interfaced with the accounting modules using [PM Interface](/en/vista/vista/project-management/setupmaintenance/pm-interface-form).

Click [here](/en/vista/vista/project-management/change-orders/pm-contract-change-orders-form) for general information on contract change orders (CCOs).
History tab
The History tabs (in both the Header and Items sections) provide a record of all additions, changes, and deletions made to the approved change order and approved change order items (respectively). Each history record shows the action date/time, action type (add, change, delete), the field affected, the old and new values (where applicable), the user name of the person performing the action, and a description of the action. You can also view the history for approved change orders/items in [PM Document History ](/en/vista/vista/project-management/document-tracking/pm-document-history-form).
ACO Items - General information
Approved change order items are entered in the lower section of the form. You can set up a single change order item to represent a group of phases of work to be done, or set up each phase of work to be done as a separate item on the change order.
You can enter change order items manually or
 initialize them using PM CO Items Initialize (Tasks > Load ACO
 Items Costs). Initialization will generate change order items from selected
 contract items.
For each change order item, you can specify the PCO Type, PCO, and PCO Item to which the approved change order item is related. If you approved a pending change order using the [PM Approve PCOs](/en/vista/vista/project-management/change-orders/about-the-pm-approve-pcos-form) form, this information will default from the approved pending change order and cannot be changed. Additional information entered for the change order item includes the change order item description, the contract item to which the change order item is associated, status, units, UM, unit price, amount, and number of days by which the change order item changes the original contract completion date.
Estimate Detail tab
Use this tab to enter the estimate detail for each
 approved change order item.
Approved PCO
If this is a potential/pending change order that has been approved using [PM Approve PCOs](/en/vista/vista/project-management/change-orders/about-the-pm-approve-pcos-form), this tab will display the estimates entered using the Estimate/ Purchase Details tab on PM Pending Change Orders - Estimate UM, Estimate Hrs/Unit, Estimate Hours, Estimate Cost/Hour, Estimate Unit Cost, and the Estimate Amount fields.
Note: If the detail item is ready to be sent to accounting, make
 sure that the Send box checked. Only items with
 this box checked can be interfaced with the accounting modules using [PM Interface](/en/vista/vista/project-management/setupmaintenance/pm-interface-form). Once the estimates are interfaced,
 they will display on the Phase Detail tab of [JC Change Orders ](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form).Manually Creating an ACO

If you are manually entering an ACO rather than
 approving a PCO, you can automatically add phase/cost type detail by selecting
 Tasks > Generate
 Detail. This will add all phases/cost types linked to the contract item
 specified for the change order item using the Contract Item on the Info
 tab.
Note: In order to use the Generate Detail feature, the contract
 item must already exist for the contract and phases/cost types must already be
 linked to the contract item in [PM Project Phases ](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form).
For applicable phases/cost types, you can:

- manually enter units, hours, and cost or load the actual values (units,
 hours, and costs) from JCCD (see Related Topics below for more
 information);

- set the Item Unit or Phase Unit flags to indicate whether the phase’s cost
 type will be used to accumulate units complete for the related contract item or
 units complete for the phase (respectively);

- indicate whether the phase/cost type should immediately update Job Cost
 (Active flag checked), or whether they will be updated only when the interface
 is run (Active flag unchecked).

If you are tracking the costs associated with a
 change order, it is important to use a different phase than the original. You may
 choose to use the last part of the multi-part code to designate the change order.
 For example, if phase 04210- - is for Brick Masonry, you could use 04210- - 3
 for approved change order #3 on Brick Masonry.
As phases are entered, the fields above the grid display the pending revenue, cost, and profit of the change order item, along with current estimated units, unit cost, hours, and costs. If a phase’s contract item does not match the contract item assigned to the change order item, a message displays below the totals indicating the contract items do not match; however, entry is allowed. If you have checked the Force Phase box for the change order item, during the interface to accounting, these phases will be changed so they point to the same contract item as specified for the change order item.
Note: Phases added for a change order that are assigned a
 subcontract cost type or material cost type will be treated as follows:

- If the subcontract cost type matches either of the cost
 types designated for subcontracts in PM Company Parameters (SL Params tab),
 the system will create a subcontract detail line in PM Subcontract
 Detail.

- If the material cost type matches either of the cost
 types designated for materials in PM Company Parameters (Material Parameters
 tab), the system will create a material detail line in PM Material Detail
 with a Material Type of Purchase Order.

 You can add, modify, or delete the subcontract
 and/or material detail as necessary in PM Subcontract Detail or PM Material Detail
 (respectively). For more information about subcontract or material detail, see
 Related Topics below.
Additional Info Tab - Interfaced Date
Interface dates are tracked for both change order items and phase/cost type detail. The Interfaced Date for items can be seen on the Grid tab and the Add’l Info tab, along with the user (login) who interfaced the approved change order.
The Interfaced Date for phases/cost types displays on the Phases grid; however, it will only display if you have checked the ‘Show on Grid’ option for the Interfaced Date column in F3 Properties.
The interface dates are updated during the interface to Job Cost. Since phases/cost types can be interfaced at different times, the interface date may differ for each phase/cost type record. For change order items, the interface date will depend on whether or not phase detail exists for the item. The update will occur as follows:

- If phase cost type detail exists for the approved change order item, the
 item's interface date will be updated with the last Interfaced Date from the
 phase/cost type detail.

- If no phase cost type detail exists for the approved change order item, the
 item's interface date will be the actual interface date for the item.

Note: Change order items with an interface date will be included
 in certain reports, regardless of whether phase detail exists for the item.
Distribution Icon
Use the Distribution icon to either set up a distribution default on a project or create a distribution group.

- Distribution Default - Use distribution defaults to define what documents a
 contact should by default receive when using the [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature. For example, if a
 contact at an architecture firm should receive a copy of all drawing logs of
 document type 'ARCH', use this feature to set up that contact as a default for
 'ARCH' documents. When drawing logs of that type are created in PM Drawing Logs,
 the contact will automatically be added to the Distribution tab. When
 communications and documents are created using the Create and Send feature, the
 contact will by default be included. [More](/en/vista/vista/project-management/create-and-send/pm-assign-distribution-defaults-form)Note: Assigning a new
 distribution default will not change the distribution of the current
 document. The new distribution default will only be applied when you create
 a new document (RFI, change order, etc.).

- Distribution Group - A distribution group is a collection of contacts that
 you regularly group together and send correspondence to - for example a group of
 contacts that receive submittals. These groups can then be added to
 communications created using the Create and Send feature. [More](/en/vista/vista/project-management/create-and-send/pm-distribution-groups-form)

Related Items
The Related Items feature allows you to link
 associated items - for example link a project issue with the RFIs, meetings, PCOs,
 and other documents and records that relate to the issue.
Items are linked in several ways:

- Automatically - The system automatically relates two records
 when one record is used to generate another. For example if you select
 Create > RFI on PM Issues, the system will automatically relate the created
 RFI and the project issue used to create it. The Create drop down in the PM Work Center also automatically links
 related records.

- Manually in a form - You can manually create and remove item
 relations using the [PM Related Items](/en/vista/vista/project-management/about-related-items/pm-relate-items-form) form. This form is launched
 from most forms in the PM module by clicking the drop down next to the Related
 Items icon and selecting Add Record Items. PM Relate Items has search functions
 that allow you to quickly locate records and then manually add or remove the
 relations.

- Manually in the PM Work Center - You can also manually relate
 items using the drag and drop feature on the Related Items panel on the PM Work
 Center. For example if you receive an MS Outlook email about an RFI, you can
 open that RFI in the PM Work Center and then drag and drop the email from MS
 Outlook to the Related Items panel. This will add the email as an attachment and
 as a related item on the RFI. Once the items are linked, use the Related Items panel on the PM Work
 Center and most PM module forms to view and open the related items.


- Click [here](/en/vista/vista/project-management/about-related-items) for general information about the Related Items feature.

- Click [here](/en/vista/vista/project-management/about-related-items/pm-relate-items-form) for information on manually adding or
 removing related items.

Distribution Audit
Use the Distribution Audit () feature to view:

- All of the documents generated using the [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature - for example change
 orders, RFIs, drawing logs, project issues, etc.

- Any communications sent using the Create and Send feature- for example if
 you resend a document to a project contact. Click [here](/en/vista/vista/project-management/document-tracking/pm-document-distribution-audit-form) for more information.

Create a related item
Use the Create Related option () to create a new record using the information on the currently selected record. The new record will be associated with the current record using the [Related Item](/en/vista/vista/project-management/about-related-items) feature, and to reduce data entry some of the fields on the new record will default based on the currently selected record.
For example if you are viewing a meeting in the PM
 Meeting Minutes form and want to create a new pending change order, click on the
 Create Related option () and select Pending Change Orders from the
 menu that displays. This will open the PM Pending Change Orders form, and populate
 the Project field so that you can create a new pending change
 order.
This feature is also available on the PM Work Center.
Why can't I add an ACO item to an interfaced ACO?
Are you trying to add an ACO item to an interfaced ACO? You can't do this using the PM Approved Change Orders form if the [Lock down ACO Items after Interface box](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-0005b2fd--en) is checked (PM Company Parameters> Info).

[](/en/vista/vista/project-management/change-orders/change-management---overview)Overview of Change Orders
[](/en/vista/vista/project-management/change-orders/about-the-pm-load-co-item-costs-form)Load Costs
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-budgets-form)Project Budgets
[](/en/vista/vista/project-management/change-orders/updating-phases-to-job-cost)Updating Phases to JC
