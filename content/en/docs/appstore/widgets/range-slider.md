---
title: "Range Slider"
url: /appstore/widgets/range-slider/
category: "Widgets"
description: "Describes the configuration and usage of the Range Slider widget, which is available in the Mendix Marketplace."
tags: ["marketplace", "marketplace component", "widget", "range slider", "platform support"]
#If moving or renaming this doc file, implement a temporary redirect and let the respective team know they should update the URL in the product. See Mapping to Products for more details.
---

## 1 Introduction

The [Range Slider](https://marketplace.mendix.com/link/component/52704/) widget can be used to change the range of values using a slider.

### 1.1 Features

* Adjust lower bound and upper bound values on the slider
* Execute a microflow when a slider value is changed or clicked
* Show or hide a tooltip upon hover
* Render range slider with different Bootstrap colors

## 2 Configuration

On the **Data source** tab, configure these properties:

* **Range minimum attribute** – the attribute that contains the minimum slider value; if not provided, the **Default minimum value** is used
* **Range maximum attribute** – the attribute that contains the maximum slider value; if not provided, the **Default maximum value** is used
* **Selected minimum attribute** – the attribute that contains the minimum bound slider value
* **Selected maximum attribute** – the attribute that contains the maximum bound slider value

## 3 Usage

### 3.1 Two Values vs. One Value

The Range Slider widget allows you to set two values between two bounds (the minimum value and maximum value). However, if only one value needs to be set between two bounds, you should use the [Slider](https://marketplace.mendix.com/link/component/48786/) widget instead.

### 3.2 Sample Slider

In Studio Pro, place the widget in the context of an object that has attributes for the maximum value, minimum value, lower bound value, and upper bound value. The maximum and minimum values determine the range within which the range slider values can be adjusted.

![](/attachments/appstore/widgets/range-slider/sample-range.png)

The step value determines the next point to shift to when sliding (meaning, the interval between points or numbers):

![](/attachments/appstore/widgets/range-slider/step-value.png)

For the step value, the difference between the maximum value and the minimum value should be divisible by 2 (as in, `(maximumValue - minimumValue) % 2 = 0`).
