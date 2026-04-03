---
title: "Export from WinEstimator | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/project-setup/estimating-systems/trimble-winest/export-from-winestimator"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/project-management/project-setup/estimating-systems/trimble-winest/export-from-winestimator"
---

# Export from WinEstimator

This Project Setup module can be used to link a
 non-Spectrum estimating program to the Spectrum Construction Management software.

##  Tools > Job Cost Export

From the Tools menu, select Job Cost Export. The following window opens.
This export window allows you to:

- Name the job cost transaction file with the proper extension.

- Locate the directory where the file will be created.

- Assign the specific job number or change order number to this
 file.

- Assign a date to these transactions.

- Determine the type of transactions in the file.

- Determine how the markups will be calculated in reference to the
 transactions.

- Format the job cost transaction file types.

Export File - This is the name and extension for the transaction file.
Examples: jobc1201.jct trans104.txt
The main file name can have up to eight characters to describe it. The importance of the name is that it can be identified by the person loading the transaction. The file extension is three characters long, you should name the extension with the appropriate three character extension that your accounting software will recognize as a set of job cost transactions.
Note: The transaction file name can be preceded by the path on the hard drive where the file will created. You can locate the destination on the hard drive with the browse button, using the standard file save as window to find the destination.
Job Number - This field is used in the layout tool to identify which job number that the transactions belong to. This number should be coordinated with the accounting program so that the transactions are not duplicated or sent to a different budget.
Change Order Number - This field works similar to the job number except that it is a unique identifier for a change order in association with a change order budget addition.
Date - This is the date field used in the layout tool. It will automatically pre-fill to the current date on your computer.
Transaction Type - The transaction type identifies whether the resulting job cost transactions are: preliminary budget transactions, beginning budget transactions or change order transactions. Your selection will format the data in the layout specified for the transaction type as built in the formatting tool. You must assign which filter to use with the selected transaction type by using the 'Assign Filter' button.
Markup Calculation Type - This identifies how the markups will be treated in relationship to the transactions. Only one selection can be made per file. Here are the different types:

- Do Not Include
 Markups - This will assume that the markup costs are not to be
 included in the job cost budget.

- Allocate
 Markups - This will apply the markup and bonding costs onto the cost
 items in the estimate, according to the categories they were calculated from and
 range if applicable. This is similar to selecting the "Show Gross Costs" feature.

- Assigned Markup
 Phases - This will reference the job cost phase assignments on the
 totals page and calculate the transactions in association with the layout for the
 other category.

Create File - This button implements the file creation process to the selected destination with the selected options.
Close - This button closes the window without performing the export.
Browse - This button activates the File Save As window that allows you to select the destination for the transaction file.
Edit Filters - This button activates the file layout tool. Help for this is covered in the topic, To Universal Format under the section Editing an Export Filter.
Assign  - These buttons allows you to select which filter you want to use to create your export file.
Since each cost accounting software program loads budget transactions in its own specific format, WinEst has a file layout tool that allows you to adapt WinEst to your accounting software's specific layout.

## Editing Export Filters

Since each cost accounting software program loads budget transactions in its own specific format, WinEst has a file layout tool that allows you to adapt WinEst to your accounting software's specific layout.
Helper filter - Mark this filter as just being part of a filter export chain.
Export Method - This determines what data will be export from this filter.
The layout tool defines three standard transactions types: Preliminary Job Cost Budget, Beginning Job Cost Budget and Change Order. Your cost accounting software should have the transaction file format for one or more of these possible budget types.

## The Data Options Tab

Export Header Rows - This enables you to export a Header record prior to each exported record.
Export Footer Rows - This enable you to export Footer record following each exported record.
Use Fixed Field Widths - Export data as fixed widths.
Allow a chained Filter sequence - Allow this filter to automatically call another 'Helper Filter'.
Summarized by Job Cost Phase - Summarizes all estimate item by their Job Cost Phase assignment prior to export.

## The Header Text Tab

This tab enables you to setup text that will print prior the first Exported record. Multiple lines of exported text are supported here. This is different than the 'Header' found on the Data Options Tab in that this text is print only once per filter incidence of the filter.

## The Footer Text Tab

This tab enables you to setup text that will print prior the first Exported record. Multiple lines of exported text are supported here.
