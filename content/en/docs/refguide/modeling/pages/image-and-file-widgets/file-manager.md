---
title: "File Manager"
url: /refguide/file-manager
parent: "image-and-file-widgets"
tags: ["studio pro", "file manager", "file widget", "widget"]
#If moving or renaming this doc file, implement a temporary redirect and let the respective team know they should update the URL in the product. See Mapping to Products for more details.
---

{{% alert type="warning" %}}The file manager widget is not supported on native mobile pages.{{% /alert %}}

## 1 Introduction

A file manager is used to upload and/or download files.

![File Manager](/attachments/refguide/modeling/pages/image-and-file-widgets/file-manager/file-manager.png)

A file manager must be placed inside a data view connected to the entity that is either a **System.FileDocument** (or a specialization) or an [external entity](external-entities) with a `Contents` binary attribute.

{{% alert type="info" %}}
For an external entity to be used as a file source, it must be defined as a media element in the corresponding OData service. Such an element can be recognized by setting the `HasStream` attribute to `true` in its metadata.  
{{% /alert %}}

{{% alert type="info" %}}
When uploading a file through the file manager, the FileDocument object will be committed immediately.
{{% /alert %}}

## 2 Properties

An example of file manager properties is represented in the image below:

{{/* % image_container width="250" % */}}![File Manager Properties](/attachments/refguide/modeling/pages/image-and-file-widgets/file-manager/file-manager-properties.png)
{{/* % /image_container % */}}

File manager properties consist of the following sections:

* [Common](#common) 

* [Design Properties](#design-properties)

* [Editability](#editability)

* [General](#general)

* [Label](#label)

* [Visibility](#visibility)

### 2.1 Common Section {#common}

{{% snippet file="/static/_includes/refguide/common-section-link.md" %}}

### 2.2 Design Properties Section {#design-properties}

{{% snippet file="/static/_includes/refguide/design-section-link.md" %}} 

### 2.3 Editability Section {#editability}

{{% snippet file="/static/_includes/refguide/editability-section-link.md" %}}

### 2.4 General Section {#general}

#### 2.4.1 Type

The **Type** property indicates how the end-user will be able to use the file manager.

| Value | Description |
| --- | --- |
| Upload | The file manager can only be used to upload a file. |
| Download | The file manager can only be used to download a file. |
| Both *(default)*  | The file manager can be used to both upload and download a file. |

#### 2.4.2 Max File Size (MB)

**Max file size (MB)** determines the maximum size of files (in megabytes) that can be uploaded.

Default: *5*

{{% alert type="info" %}}
This value cannot be set arbitrarily high as the platform to which the app is deployed may also impose a limitation on the size of the files that can be uploaded or downloaded.
{{% /alert %}}

#### 2.4.3 Allowed Extensions

You can specify file extensions that users are allowed to upload. If no extension is specified, all file extensions are allowed. Separate multiple extensions by a semi-colon, for example, `txt;doc`

If a file with an extension that is not allowed is selected, a [system text](system-texts) for **File manager/dynamic image** > **Error: incorrect file extension** will be shown below the file manager.

#### 2.4.4 Show File in Browser

**Show file in browser** indicates whether a file will be shown in the browser instead of being downloaded.

Default: *False*

### 2.5 Label Section {#label}

{{% snippet file="/static/_includes/refguide/label-section-link.md" %}}

### 2.6 Visibility Section {#visibility}

{{% snippet file="/static/_includes/refguide/visibility-section-link.md" %}}

## 3 Read More

* [Page](page)
* [Images, Videos & Files](image-and-file-widgets)
* [Properties Common in the Page Editor](common-widget-properties)
* [System Texts](system-texts)
