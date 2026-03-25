---
title: "Set up the Process Workflow Feature | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/set-up-the-process-workflow-feature"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/set-up-the-process-workflow-feature"
---

# Set up the Process Workflow Feature

The Process Workflows feature is used to force purchase orders and subcontracts that meet a defined criteria to follow a specific approval/review process.

- You must have the Workflow module in order to use this feature.

- It is important that you test this feature in a test environment or test company before implementing it. This is to verify that the workflow processes are set up correctly and functioning like expected before they are implemented.

1. Create roles in the [HQ Roles](/en/vista/vista/administration/headquarters/role-setup/hq-roles-form) form.  Every user entering or reviewing/approving purchase orders and subcontracts will need a role. These roles are not company specific, meaning that the roles you create using this form can be used in any company.

1. Assign spending limits to roles using the Spending Limits tab on the HQ Roles form. A spending limit is the maximum amount that a user can spend before a workflow will apply.

1. Assign users to the roles. You can do this using either of the following forms:

- HQ Roles > Users tab - Allows you to add multiple users to a single role.

- VA User Profile > Roles tab - Allows you to add multiple roles to a single user.

1. If applicable, assign spending limit overrides to specific users. For example if a PM should have a lower or higher spending limit than the other PMs, you can set up a user spending override for that user. Set up spending limit overrides via the HQ User Spending Overrides form, accessed by selecting User Spending Overrides on the Users tab in HQ Roles.

1. Check your work using the HQ Roles List report in the HQ module. The HQ Roles List report shows for each role, the role types and limits, as well as the users assigned to the role.

1. Define how users will receive the messages generated when purchase orders and subcontracts are processed.

- Email - If users should receive emails, make sure that everyone creating POs and Subcontracts, as well as those reviewing/approving them has an email address associated with their user account in the VA User Profile form. Emails are sent from the Vista server using SMTP, so you do not have to use MS Outlook to use this feature.

- VP Message - VP Messages are messages sent through the Viewpoint application and viewed using the VA Messages form. To use VP Messages, open the VA User Profile form, select the Notification Preferences tab, and then add a record with a Source of Workflow and a Destination of 1-VP Message. This has to be done for every user using the Process Workflow feature.

 The system sends a message to reviewers when a PO or Subcontract is ready for review/approval and to initiators when the PO or Subcontract they entered has been rejected.

1. Set up security (as needed) on the forms used in the Process Workflow feature. You might typically set up security as follows:

- HQ User Spending Overrides - Admins only

- PO Pending Purchase Orders - Initiators and Approvers/Reviewers

- PM Subcontracts - Initiators and Approvers/Reviewers

- WF Document Review Edit - Reviewers

- WF Workflow Process - Admins only

1. Create workflow processes using the [WF Workflow Process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process) form.

1. Define when to apply the processes using the Workflow tab on applicable forms. For information about applicable forms and workflow hierarchy, see [About the Workflow Hierarchy](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/about-the-workflow-hierarchy).

1. If applicable, assign users to specific roles on jobs, projects, equipment departments (POs only), and/or inventory locations (POs only). You will typically do this when you want specific users associated with a role to review/approve POs and Subcontracts, rather than all users associated with the role.

1. Purchase orders and Subcontracts are processed using inquiries launched from Work Centers. Use the [VA Inquiry Security](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-the-va-inquiry-security-form) form to set up access for these inquiries.

- My Documents to Review (WFDocumentApproval)

- My Items to Review (WFDocumentItemApproval)

- My Documents in Workflow (WFDocumentMyOutstanding)

- My Workflow Documents to Process (WFDocumentMyReadyToProcess)

- Workflow Comments (WFDocumentComments)

- All Documents in Workflow (WFDocumentAllOutstanding)

- All Workflow Documents to Process (WFDocumentAllReadyToProcess)

Note: You can see a description of these inquiries in the VA Inquiries form.

1. Add the new inquiries to the Work Centers on user accounts. There are a few ways to do this:

- Have users add a new PM Work Center - If a user adds a new PM Work Center to their application window, the basic Process Workflow inquiries will display in the a Document Review folder in the PM Work Center menu.

- Create a new Work Center Profile and have users apply it - If you use Work Center Profiles, you can create a new one that includes the Process Workflow inquiries. Users can then apply the Work Center Profile to their application windows. For more information, see [About the VA Work Center Profile Form](/en/vista/vista/administration/viewpoint-administration/work-centers/about-the-va-work-center-profile-form).

- Have users add these inquiries to their existing Work Centers - Users can add manually inquiries to the menu of a PM Work Center. For more information, see [About the Project Management Work Center](/en/vista/vista/system-tools/work-centers/about-the-project-management-work-center).

1.  Thoroughly test the processes that you have created before implementing them.

- Create POs in a test environment or test company to verify that they are being processed correctly. You can also see the workflow that will be applied to a PO item using the Workflow button on the PO Pending Purchase Orders and PM Purchase Orders form. For example you can log in as a user, create a PO, select the Workflow button to see the workflow that will apply to the PO item, and then change the PO to make sure the it will be processed correctly.

- When using a test company - The roles and workflow processes are not company specific, so you will be able to test most of your workflow processes using a test company. You will not be able to test processes that are company specific and set up using the Workflow tab on the [HQ Company Setup](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form) form.
