---
title: "About Distribution Contacts for a Subcontract | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/subcontracts/about-distribution-contacts-for-a-subcontract"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/subcontracts/about-distribution-contacts-for-a-subcontract"
---

# About Distribution Contacts for a Subcontract

The Distributions tab in PM Subcontracts allows you to set up contacts that should receive communications related to the subcontract.
You will generally include the vendor specified on the subcontract in the distributions list; however, you can set up any firm/contact for the project who should receive any communications about the subcontract.
Contacts are automatically set up on this tab in one of two ways:

- If the vendor you specify on the subcontract is set up as a firm for the project (in PM Project Firms), and contacts are set up for the firm, the system automatically adds the first contact in the list as a contact for the subcontract.

- If a contact is set up as a default contact (in Assign Distribution Defaults) for the document type associated with the subcontract, they are added to the Distribution list. For example, if you specify SL as the document type for the subcontract, and the contact is set up as a contact for Document Category "Subcontract" and Document Type "SL", that contact is auto-added to the Distributions list..

You can also manually add contacts to the distributions list directly in the Distributions tab. For more information, see [Add Contacts to a Distribution List](/en/vista/vista/project-management/create-and-send/add-contacts-to-a-distribution-list).
You can have the ‘Send To’ information for contacts print on the subcontract by adding the merge fields to the Subcontract document template in PM Document Templates (Merge Fields tab).
Document Object
Column Name
Merge Field Name

Responsible Person
FirstName
ResponsibleFirstName

LastName
ResponsbileLastName

SendToFirm
FirmName
FirmName

SendToContact
FirstName
ContactFName

LastName
ContactLName

Note: The standard templates provided with Vista™ (i.e. PM Subcontract and PM Subcontract Item - Word) already include these merge fields. You will only need to add these merge fields manually if you do not use the standard templates as a starting point when creating custom templates. (Note: For information about adding merge fields to document templates, see Related Topics below.)
