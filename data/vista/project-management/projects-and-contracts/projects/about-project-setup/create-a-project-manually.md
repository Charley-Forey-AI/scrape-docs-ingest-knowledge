---
title: "Create a Project Manually | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup/create-a-project-manually"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup/create-a-project-manually"
---

# Create a Project Manually

Creating a project is the first step in the Project Setup process.
Follow the steps below to manually create a project using the PM Projects form.This process only covers completing the required fields and basic setup. For more information about a field, press F1 from the selected field.

1.  Open PM Projects (Project Management > Programs > PM Projects).

1. Select the New Record icon to create a new project. Note: You can also create a project using the Grid tab if you prefer to enter data into columns.

1. Enter a project number and project description into the Project and Description fields.

1. The Contract field automatically populates with the value entered in the Project field. Accept the defaulted value or press F4 to select a different contract for the project.If you accept the defaulted value, the system automatically sets up the new contract with minimal information (in PM Contracts) once you save the record. You will enter the contract details in the next step of the project setup.

1. In the Department  field, enter the department for the specified contract or press F4 to select from a list of valid Job Cost departments.

1. In the Customer field, enter the customer for the specified contract or press F4 to select from a list of valid customers. a customer from a list. Tip: If the customer associated with the contract does not yet exist in the system, you can press F5 to access the AR Customers form, add the customer, and then enter that customer here.

1. In the Retainage Percentage field, enter the retainage percent to use as the default for all items on the contract.

1. In the Start Month field, enter the start month for the project.

1. Enter the Liability Template to use when determining how payroll burden should be charged to this project. Press F4 to select from a list of valid liability templates.

1. In the PR State field, enter the two-character state code identifying where the project is located.

1. If applicable, use the Compliance Groups section to assign the PO and SL compliance groups.

1. If applicable, use the Reviewer Group section to assign review groups for invoices and timesheets.Note: Reviewer groups allow you to assign multiple reviewers to an unapproved invoice or timesheet entered for the project. Members of those groups can either approve or deny that item.

1. Select the Add'l Info tab.

1. In the Hours Per Man Day field, accept the default (8.000) or enter the hours that make up a standard 'man-day' for this project.The system uses the hours indicated here to determine 'over/under', 'remaining' and 'final' hours for cost projections.

1. Select the PR Info tab.

1. If this project is certified, select the Certified checkbox.

1. Select the PM Info tab.

1. In the Project Our Firm field, enter the firm to use as 'our firm' for the project or press F4 to select from a list of valid PM Firms.  The system uses this firm as the sending firm/address on documents generated for the project, and overrides the 'our firm' defined in the PM Company Parameters form.

1. If applicable, use the Architect / Engineer section to enter the architect or engineer firm and contact associated with the project.

1. Use the Documents section to define how the system will automatically number the documents associated with the project. For more information about the options available for each field, press F1 in the selected field.

1. Use the Default Standard Days Due and Default Request for Information Days Due fields to set the default due date of documents generated using the Create and Send feature.

1. If you use the Approval process for purchase orders and invoices, use the Reviewers tab to assign reviewers to the project.

1. In the Sequence field, assign a sequence number that represents the order in which invoices or POs will be approved.

1. In the Reviewer field, assign a reviewer or press F4 to select from a list of valid reviewers.

1. In the Reviewer Type field, select 1-Invoice, 2-Purchase, or 3-Both, to identify what items the reviewer will be reviewing.

1. Select Save.

1. Use the Markups tab to set up the contractual Markup % for each cost type on a project.The system uses these markups as defaults when creating pending change orders; however, you can override them as needed.

1. If applicable, use the Add-ons tab to define add-ons for a project. Add-on costs set up using the PM Company Parameters form will automatically populate on the new project, but you can modify or delete these costs as needed.

1. Use the Phases tab to add phases to the project.You will complete this tab once you have set up the contract in PM Contracts.

1. If applicable, use the Locations tab to define the locations on a project. For example, you might set up locations to identify all of the buildings on a project.

1. Select the Firms tab and set up the firms associated with the project. The firms set up for a project are used when sending project-related documents, such as RFIs, RFQs, drawing logs, and so forth.

1. If applicable, use the [PM Assign Distribution Defaults](/en/vista/vista/project-management/create-and-send/pm-assign-distribution-defaults-form) form (Distribution > Distribution Default) to define which project contacts should receive documents when using the Create and Send feature.

1. If applicable, use the Roles tab to assign roles to users on the project.

1. If using the Review/Approval Workflow process feature, use the Workflow tab to define the review/approval process (set up in WF Workflow Process) to use for each document type (purchase orders and subcontracts).

Related information

- [About Project Setup](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)

- [PM Projects Form](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form)

- [PM Import Estimates Form](/en/vista/vista/project-management/import-project-estimates/pm-import-estimates-form)

- [PM Copy Project Form](/en/vista/vista/project-management/projects-and-contracts/projects/pm-copy-project-form)

- [Potential Project Conversion](/en/vista/vista/costs-and-contracts/pre-construction/pc-potential-projects/potential-project-setup/potential-project-conversion)
