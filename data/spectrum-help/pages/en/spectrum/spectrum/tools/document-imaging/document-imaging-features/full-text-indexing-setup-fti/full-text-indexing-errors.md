---
title: "Full Text Indexing Errors | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/document-imaging/document-imaging-features/full-text-indexing-setup-fti/full-text-indexing-errors"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/tools/document-imaging/document-imaging-features/full-text-indexing-setup-fti/full-text-indexing-errors"
---

# Full Text Indexing Errors

The table below shows a list of the errors Spectrum could potentially return when importing files.
Error
Meaning

Unable to find the specified file.
The file was not found in the path specified or it was inaccessible from the server.

The following types of files will be read using OCR technology:

- PDF

- TIFF

- DOC, DOCX

- XLS, XLSX

- TXT (plain text)

- RTF (formatted rich text)

Process timed out or interrupted by server shutdown.
This message will occur when the service has timed out when reading a file.
 This could occur when the service is reading an extremely large file.
 Highlight the record and click Retry to start the
 process once again. If this continues, contact Systems Support to increase
 the time out settings.

[File Type] OCR error: {description of the error}
This indicates that the file cannot be read by the OCR service for some
 reason. For example, a PDF may have the error PDF OCR error: java error. A
 TIF file would have the error TIF OCR error: header error.

Unspecified OCR failure.
This message indicates that it attempted to scan a secured PDF document or a PDF document containing form fields. These types of files cannot be scanned for OCR.
