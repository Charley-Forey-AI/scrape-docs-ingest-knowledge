---
title: "About the PM Change Order Requests Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/change-orders/about-the-pm-change-order-requests-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/change-orders/about-the-pm-change-order-requests-form"
---

# About the PM Change Order Requests Form

Use this form to create and maintain change order requests (CORs).
A change order request is a formal request to an owner/customer for a change in scope, and it is an agreement acknowledging that the customer/owner will pay for the changes. Once the change order request is signed by the owner/customer, work can proceed and billings can occur.Processing a change order request in the application involves the
 following steps.
Tasks
Add PCOs to the change order
 request - PCOs tab
Use this tab
 to add pending change orders to the change order request(COR). All of the items on
 the selected PCOs will be added.
The PCOs added to this tab will display in a table on the standard Change Order
 Request document generated using the [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature.
Pending change orders added to this tab
 will automatically be related to the COR using the Related Items feature. Click
 [here](/en/vista/vista/project-management/about-related-items) for general information about the Related Items feature.
Add multiple PCOs to a COR
Select Tasks > Add PCOs to select multiple unapproved PCOs and then add them to a change order request. The PCOs added to the COR will automatically be related using the [Related Items](/en/vista/vista/project-management/about-related-items) feature.
The PCOs are selected using the [PM Add Records](/en/vista/vista/project-management/change-orders/about-the-pm-add-records-form) form, which is a generic form used for selecting multiple records and its function varies depending on how it is launched.
Create a list of
 contacts that should receive the COR - Distribution tab
Use this tab to define who should
 receive the Change Order Request document when using the [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature.
Overview
When a new communication is created
 using the Create and Send feature (), the contacts on this tab are automatically added to
 the communication. For example if a project contact should be included in any
 communication about an RFI record (emails, RFI documents, change order reports,
 etc.), you should add that project contact to the Distribution tab of the RFI so
 that they are automatically added to any communication.
Contacts are automatically added to
 this tab in two ways

- When a project contact is included in a Create and Send communication - When a project contact is included in a Create and Send communication, the system automatically adds that contact to the Distribution tab. For example if you launch the Create and Send feature using an RFQ record, the project contacts added to the email using the To, Cc, and Bcc fields will also be added to the Distribution tab of the PM Request For Quote form. When a new email is created for that RFQ using the Create and Send feature, the project contacts set up on the Distribution tab will automatically populate in the To, Cc , and Bcc fields on the email.

- When a project contact is set up as a distribution default - The [Assign Distribution Defaults](/en/vista/vista/project-management/create-and-send/pm-assign-distribution-defaults-form) feature automatically adds contacts to the Distribution tab if they are setup as a default contact for the document type associated with the form. For example, if a project contact is set up to receive all documents and correspondence dealing with RFQs, that contact will by default be included on the Distribution tab of any RFQ document. [More](/en/vista/vista/project-management/create-and-send/pm-assign-distribution-defaults-form)Manually add contacts to the Distribution tab
You can also manually add contacts to the Distribution tab.

1. Add contacts to the Distribution tab to create a list of contacts that should receive documents generated using the Create and Send feature. There are two ways to add contacts to the tab:

- Drag and Drop - By default the Project Firm Contacts form displays when you open the Distribution tab. The Project Firm Contacts form displays a list of contacts associated with the project using the Firms tab in [PM Projects](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form). Drag and drop a contact from the Project Firm Contacts form to the Distribution tab to add the contact. Note: The Project Firm Contacts list can also be accessed by selecting View > Project Firms List.

- Manually enter the information - Enter contact information into the grid to manually to add a contact to the Distribution tab. If the contact is not already associated with the project, a message will display when you save the record. Select Yes to add the contact to the distribution list and to PM Project Firms. Select No to add the contact to the distribution list only. The Project Firm Contacts
 form doesn't display

The Project Firm Contacts form displays when the Distribution tab is opened and the Always Show Form box on the Project Firm Contacts form is checked. The selection in the Always Show
 Form box only affects the currently selected form (for example PM Request For Information, PM Issues, etc.) and it only applies to your user account. To view the Project
 Firm Contacts form when the Always Show Form box is
 not checked, open the Distribution tab and select View > Project Firms List from the toolbar at the top of the form.

1. Verify that the preferred method of correspondence is correct.

1. Use the Send Type field to select how the contacts should be included in the communication. The [Create and Send ](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature will generate a unique document for each contact with a send type of To.

1. Check the Send box for each contact in the grid that should receive the communication. If this box is not checked, the contact will be excluded when generating documents using the [Create and Send ](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)feature.

Approve the PCOs on the COR
Once the COR is approved by the customer, you can approve all of the pending change orders on a COR by clicking the Tasks icon and selecting Approve PCOs. This will open [PM Approve PCOs](/en/vista/vista/project-management/change-orders/about-the-pm-approve-pcos-form) with all of the pending change orders on the COR populated in the form.
Click [here](/en/vista/vista/project-management/change-orders/about-the-pm-approve-pcos-form) for more information about the approving the PCOs using PM Approve PCOs.
Create and Send feature - Generate a COR document and email it to a project contact
 The [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature allows you to generate documents and send them to project contacts. For example, you can use this feature to create RFIs, submittals, and change order documents and then email those documents to the contacts on a project.
Click [here](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) for more information on the Create and Send feature.
Three options display when you click on the Create and Send () icon:

- Send Message - Select this option to send an email to a list of project contacts. Using this option you can also generate a document, include an attachment, and/or generate a report. [More](/en/vista/vista/project-management/create-and-send/about-sending-messages)

- Send Document - Select this option to generate a project document or report, and email it to a list of project contacts. Using this option you can also include an attachment. [More](/en/vista/vista/project-management/create-and-send/about-sending-documents)

- Send with Transmittal - Select this option to generate a project document and transmittal, and email those documents to a list of project contacts. Using this option you can also include an attachment and/or generate a report. [More](/en/vista/vista/project-management/create-and-send/about-sending-with-transmittal)Generate a report
Some of the PM module forms do not have a related
 document template, for example the [PM Approved Change Orders ](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form), [PM Purchase Orders](/en/vista/vista/project-management/materials/pm-purchase-orders-form), and [PM Punch List ](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-punch-list)forms. Generally you will use
 the Create and Send feature on these forms to generate reports and then
 email those to a list of project contacts. For example you can use the
 Create and Send feature to generate a daily log report and then send it to a
 list of project contacts.
Why doesn't the Create and Send () icon display on the form?
Note: The Create and Send () icon will not display on the form if it has been disabled using [PM Create & Send Settings](/en/vista/vista/project-management/create-and-send/pm-create--send-settings-form) form (Info tab> Deactivate Document Create and Send Featurebox).Additional Information

COR Status
A system status field displays next to the Contract field at the top of the form. This field displays the approval status of the PCOs on the COR. This field is not related to the user-defined Status field that displays on the Info tab next to the Date field.

- No PCOS - No PCOs have been added to the change order request.

- Not Approved - All of the PCOs on the COR have a pending status, meaning that none of them have been approved and added to an ACO.

- Partially Approved - Some of the PCOS on the COR have been approved and added to an ACO

- Approved - All of the PCOs on the COR have been added to ACOs.

Note: Pending change orders are approved using [PM Approve PCOs](/en/vista/vista/project-management/change-orders/about-the-pm-approve-pcos-form).
Totals - Info tab
There are four total fields on the Info tab that provide a snapshot of the COR when it is created. These fields will populate with calculated values as PCOs are added to the COR, but these totals do not automatically update when you change the information on the PCOs.
For example if you add an item to a PCO that has already been included on the COR, the COR totals will not automatically update to reflect the amounts on the new PCO item.
If you would like to update the totals so that they reflect the changes made to the PCOs after they have been added to the COR, select Tasks > Refresh Totals.
Note: When you add new PCOs to a COR, only the amounts on the new PCOs will be added to the totals, but changes to PCOs that have already been added to the COR will not update.Original
 Contract Amount

This field displays the original contract amount, including all contract items.
Previously Authorized Contract Changes
This field includes all change orders that have already been approved on the contract - for example potential change orders that have been approved and added to ACOs using [PM Approve PCOs](/en/vista/vista/project-management/change-orders/about-the-pm-approve-pcos-form), or change orders created as ACOs using [PM Approved Change Orders ](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form).
Current Change Order Request
This field displays the change to the contract amount associated with all of the items on the pending change orders selected on the PCOs tab.
Note: If there are items on the selected PCOs that have been approved using [PM
 Approve PCOs](/en/vista/vista/project-management/change-orders/about-the-pm-approve-pcos-form), those items will be included in this total.Current Contract Amount

This field displays the original contract amount plus previously approved change orders and the pending change orders on the PCOs tab.
Related Items ()
The Related Items feature allows you to link associated items - for example link a project issue with the RFIs, meetings, PCOs, and other documents and records that relate to the issue.
Items are linked in several ways:

- Automatically - The system automatically relates two records when one record is used to generate another. For example if you select Create > RFI on PM Issues, the system will automatically relate the created RFI and the project issue used to create it. The Create drop down in the PM Work Center also automatically links related records.

- Manually in a form - You can manually create and remove item relations using the [PM Related Items](/en/vista/vista/project-management/about-related-items/pm-relate-items-form) form. This form is launched from most forms in the PM module by clicking the drop down next to the Related Items icon and selecting Add Record Items. PM Relate Items has search functions that allow you to quickly locate records and then manually add or remove the relations.

- Manually in the PM Work Center - You can also manually relate items using the drag and drop feature on the Related Items panel on the PM Work Center. For example if you receive an MS Outlook email about an RFI, you can open that RFI in the PM Work Center and then drag and drop the email from MS Outlook to the Related Items panel. This will add the email as an attachment and as a related item on the RFI. Once the items are linked, use the Related Items panel on the PM Work Center and most PM module forms to view and open the related items.

- Click [here](/en/vista/vista/project-management/about-related-items) for general information about the Related Items feature.

- Click [here](/en/vista/vista/project-management/about-related-items/pm-relate-items-form) for information on manually adding or removing related items.

Distribution Icon ()
Use the Distribution icon to either set up a distribution default on a project or create a distribution group.

- Distribution Default - Use distribution defaults to define what documents a contact should by default receive when using the [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature. For example, if a contact at an architecture firm should receive a copy of all drawing logs of document type 'ARCH', use this feature to set up that contact as a default for 'ARCH' documents. When drawing logs of that type are created in PM Drawing Logs, the contact will automatically be added to the Distribution tab. When communications and documents are created using the Create and Send feature, the contact will by default be included. [More](/en/vista/vista/project-management/create-and-send/pm-assign-distribution-defaults-form)Note: Assigning a new
 distribution default will not change the distribution of the current
 document. The new distribution default will only be applied when you create
 a new document (RFI, change order, etc.).

- Distribution Group - A distribution group is a collection of contacts that you regularly group together and send correspondence to - for example a group of contacts that receive submittals. These groups can then be added to communications created using the Create and Send feature. [More](/en/vista/vista/project-management/create-and-send/pm-distribution-groups-form)

Distribution Audit ()
Use the Distribution Audit () feature to view:

- All of the documents generated using the [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature - for example change orders, RFIs, drawing logs, project issues, etc.

- Any communications sent using the Create and Send feature- for example if you resend a document to a project contact. Click [here](/en/vista/vista/project-management/document-tracking/pm-document-distribution-audit-form) for more information.

Create a related item ()
Use the Create Related option () to create a new record using the information on the currently selected record. The new record will be associated with the current record using the [Related Item](/en/vista/vista/project-management/about-related-items) feature, and to reduce data entry some of the fields on the new record will default based on the currently selected record.
For example if you are viewing a meeting in the PM Meeting Minutes form and want to create a new pending change order, click on the Create Related option () and select Pending Change Orders from the menu that displays. This will open the PM Pending Change Orders form, and populate the Project field so that you can create a new pending change order.
This feature is also available on the PM Work Center.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Orders - Overview
