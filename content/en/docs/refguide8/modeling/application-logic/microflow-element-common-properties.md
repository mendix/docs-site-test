---
title: "Common Properties"
url: /refguide8/microflow-element-common-properties/
parent: "application-logic"
weight: 110
tags: ["studio pro", "common properties", "microflow", "nanoflow"]
---

{{% alert color="info" %}}
<img src="/attachments/china.png" style="display: inline-block; margin: 0" /> For the Simplified Chinese translation, click [中文译文](https://cdn.mendix.tencent-cloud.com/documentation/refguide8/microflow-element-common-properties.pdf).
{{% /alert %}}

## 1 Introduction

This document describes common properties that are shared by many elements in the microflow editor.

{{% alert color="warning" %}}
Not every element in a microflow or a nanoflow has all of these properties.
{{% /alert %}}

These are the common properties for microflows and nanoflows:

{{/* % image_container width="30%" % */}}
![Common properties in properties pane](/attachments/refguide8/modeling/application-logic/microflow-element-common-properties/microflow-element-common-properties.png)
{{/* % /image_container % */}}


* [Caption](#caption)
* [Auto-generate caption](#auto-generate-caption)
* [Background color](#color)
* [Error handling type](#error-handling)

## 2 Caption {#caption}

The **Caption** describes what happens in this element. It is displayed in the microflow element to make the microflow easier to read and understand without needing to add annotations. If a value is entered here, [Auto-generate caption](#auto-generate-caption) is automatically set to **No**.

## 3 Auto-Generate Caption {#auto-generate-caption}

The **Auto-generate caption** property specifies whether the caption is automatically generated based on the type of activity.

| Option | Description |
| --- | --- |
| Yes  *(default)* | The caption of the activity is generated by Studio Pro. |
| No | The value in the **Caption** property, which you can edit yourself, is used. |

## 3 Background Color {#color}

The **Background color** property allows you to choose a background color for each activity individually. Colors do not influence execution; they are only used to quickly spot an element in a flow. For example, you can make activities with [error handlers](/refguide8/error-event/#errorhandlers) red so you can easily identify them.

You can also select a default color for all the activities of a certain type in **Project Settings** > [Miscellaneous](/refguide8/project-settings/#miscellaneous). The default color for all activities of a certain type can also be changed by right-clicking a microflow activity and selecting **Set as default color** from the context menu. This will make the current activity's color the default color for all activities of the same type. If you change the default color for an activity type and there are other activities of that type present in the app that have a different individual background color specified, you will be asked whether you want to overwrite these individual colors with the new default color.

## 4 Error Handling Type {#error-handling}

In **Error handling type**, you can choose the type of error handling for the activity. For details on available options and their effects, see the [Error Handlers](/refguide8/error-event/#errorhandlers) section in *Microflows*.

## 5 Read More

* [Microflows](/refguide8/microflows/)
* [Nanoflows](/refguide8/nanoflows/)