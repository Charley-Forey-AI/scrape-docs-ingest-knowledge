---
title: "About Submittals | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/about-submittals"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/about-submittals"
---

# About Submittals

Submittals are used to get specific information or items from the subcontractor, such as shop drawings, specifications, and samples (carpet, paint, flooring, etc.).
The submittals process is very flexible. Rather than being a linear process, once the submittals are created or imported into the PM Submittal Register form, you can perform several actions on those submittals. The diagram and steps below outline the basics.

## Step 1: Create / Import the Submittals

Use the PM Submittal Register form to create submittals. This form is very similar to a worksheet. Just enter information into any of the cells in the grid.
You can also import the submittals from MS Excel or other third-party application. For more information, see [Importing Submittals from MS Excel or other third party application](#ID-00021cf3--en__section_l4l_z5h_kjb).

## Step 2: Perform actions on the submittals

Once submittals have been created or imported, you can perform any of the following tasks. These are all optional tasks, and almost all of them can be performed directly from the PM Work Center.

- Change the submittal status, or close/open a submittal - Use the Status field on the PM Submittal Register form to assign a status to submittals. These statuses are created and maintained using the PM Status IDs form. When you change a submittal to a final status, the system also automatically closes the submittal. This disables all of the fields on the submittal.

- Track due, sent, returned, and received dates on the submittal - Enter the due, sent, returned, and received dates into the fields on the PM Submittal Register form. You can also set up a default submittal schedule, which will automatically populate many of these dates based on the expected activity date on the submittal. For more information, see [Set up a Submittal Schedule](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/set-up-a-submittal-schedule).

- Generate a submittal document - You can use the Create and Send feature to generate a submittal document and email it to a list of project contacts. You can launch the Create and Send feature directly from the PM Submittal Register form, or using the PM Work Center. There are two standard submittal documents included in the application: submittal register and submittal sheet. You cannot modify a standard submittal document, but you can copy one and then modify the copy. The standard submittal documents display in the PM Create & Send Templates form, and they can be copied using the PM Copy Document Template form. Click [here](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) for an overview on the Create and Send feature.

- Create a new submittal revision - To create a new revision of an existing submittal, click the Create Revision button on the PM Submittal Register form. This will copy all of the information on the previous revision and create a new revision. [More](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/create-a-new-submittal-revision)

- Add submittals to a submittal package - Use the PM Submittal Package form to create a new submittal package, and then click the Add Submittals button to group submittals on the register onto the package. [More](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/add-submittals-to-a-submittal-package)

## Step 3 - Optional: Perform actions on the submittal package

Submittal packages are an optional feature that allows you to bundle submittals entered using the PM Submittal Register form into a submittal package. If you do group submittals onto a submittal package, you can perform these additional tasks.

- Change the submittal package status, or close/open a submittal package - Use the Statusfield on the PM Submittal Package form to assign a status to the submittal register. You can also close submittal packages just like you can close a submittal.

- Track due, sent, returned, and received dates on the submittal package - Enter the due, sent, returned, and received dates into the fields in the upper portion of the PM Submittal Package form. These fields do not relate to the due, sent, returned, and received dates on the submittals, and these fields will not populate based on the submittal schedule set up on the project.

- Generate a submittal package document - Use the Create and Send feature to create a submittal package document. There are two standard submittal documents included in the application: submittal package and submittal package return. You cannot modify the standard documents, but you can copy one and then modify the copy. The standard submittal documents display in the PM Create & Send templates form, and they can be copied using the PM Copy Document Template form. Click [here](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) for an overview on the Create and Send feature.

- Create a new submittal package revision - To create a new revision of a submittal package, click on the Create Package Revision button on the PM Submittal Package form. This will copy all of the information on the previous revision, and create a new revision. Click [here](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/create-a-new-submittal-package-revision) for more information.

## What is the relationship between the submittal register and the submittal package?

The submittal register is where you enter new submittals, and create revisions of existing submittals.
Once submittals are entered, you can bundle them together in a package in PM Submittal Package.
Here is a quick list of the basics:

- You can create submittals using either the PM Submittal Register or PM Submittal Package forms, but it is easier to create submittals using the register (PM Submittal Register).

- When you delete a submittal on a package, just are only removing the submittal from that package. The deleted submittal will still display on the register (PM Submittal Register).

- When you create a submittal revision in the PM Submittal Register form, you can add the new revision to a submittal package. [More](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/create-a-new-submittal-revision)

## Importing Submittals from MS Excel or other third party application

If you enter submittals using a third party application like MS Excel, you can import them into the PM Submittal Register form using IM Import Form.
To set this up, create a new record in the IM Template form, select PMSubmittalRegisterGrid in the Import Form field, and then use the Template Detail tab to map how the data will be imported. Once the template has been created, you can use the IM Import form to import the submittals from MS Excel into the PM Submittal Register form.
Note: The imported submittals will default with the approving firm and contact set up on the project (PM Projects> PM Info> Approving Firm and Approving Firm Contact fields).

## Closing a Submittal / Submittal Package

- Submittal Packages - There are several ways to close a submittal package. When a submittal package is closed, all of the submittals in that package are also closed.

1. PM Work Center - Go to Document Control >  Submittal Package on the standard PM Work Center, highlight a package in the list, and then click on the Tasks icon () and select Open/Close submittal package from the menu that displays.

1. PM Submittal Package form - Open a submittal package in the PM Submittal Package form, and then select Tasks >  Close Submittal Package.

1. Change the status of the package to final - The system will automatically close a submittal package when you change the status of a submittal package to a final status. You can do this using the Status field in the upper portion of the PM Submittal Package form. A status is set up as a final status if the Final  box on the PM Status IDs form is checked.

- Submittal Revisions - There are also several ways to close a submittal revision.

1. PM Work Center - Go to Document Control >  Submittal Register on the standard PM Work Center, highlight a submittal in the list, and then click on the Tasks icon () and select Open/Close submittal from the menu that displays.

1. Change the status of the submittal to final - Just like submittal packages, the system automatically closes a submittal when you change the status of the submittal to a final status. You can do this using the Status field in the PM Submittal Register form, or the Status field in the lower portion of the PM Submittal Package form.

1. PM Submittal Register - Highlight a submittal in the register and then select Tasks > Close Submittal Item. You can sort and filter the submittals that display in the PM Submittal Register form by close/open using the Display only open submittals box in the upper portion of the form, or adding a filter bar to the form and then using the Closed column.

1. Create a submittal revision - When you create a new submittal revision using the Create Revision button the PM Submittal Register form, check the Close source submittal box on the PM Submittal Create Revision form to close the source submittal revision. Click [here](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/create-a-new-submittal-revision) for more information.

Related tasks

- [Set up a Submittal Schedule](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/set-up-a-submittal-schedule)

- [Add submittals to a submittal package](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/add-submittals-to-a-submittal-package)

- [Copy submittals to a different project](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/copy-submittals-to-a-different-project)

- [Create a new submittal package revision](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/create-a-new-submittal-package-revision)

- [Create a New Submittal Revision](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/create-a-new-submittal-revision)

- [Update the submittal schedule](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/update-the-submittal-schedule)
