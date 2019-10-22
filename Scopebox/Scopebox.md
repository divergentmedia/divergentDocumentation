# Welcome to ScopeBox 4 #

## Welcome ##

ScopeBox transforms your Mac into a suite of high-end video analysis tools, replacing a cart full of heavy and expensive components with one simple application.

This manual will walk you through the basics of using ScopeBox, and will also introduce you to some of the theory behind video quality analysis.

For the latest updates, news and support, be sure to visit <http://www.divergentmedia.com/>.

## What's new in ScopeBox 4 ##

ScopeBox 4 is an all-new application, building upon a decade of ScopeBox innovation.  A brand new processing engine allows for higher performance, utilization of the latest Mac hardware, and support for a huge variety of capture hardware.

### CIE Plot Palette ###
With HDR, Rec 2020, p3 and more, the world of colorspaces has gotten incredible complex.  The CIE Plot allows you to visualize gamut across multiple sets of primaries. 

### Luma and RGB TimeTrace Plot ###
Traditional scopes only show you what's happening right now.  The Luma and RGB TimeTrace palettes continuously refresh, showing you your luma (or RGB) history over the last 300 frames.  

### False Color ###
One of the most highly-requested features, false color in the preview provides a visual way to identify issues, using a variety of presets.  And you can leverage the ability of ScopeBox to host multiple copies of the same palette, running both a normal color and false color preview side-by-side.

### ScopeLink support in Resolve ###
Until now, using ScopeBox with Resolve meant running ScopeBox on a separate Mac.  Thanks to the addition of Resolve support in ScopeLink, you can run it all on the same Mac, without any additional hardware. 

### Feature Insights ###

Feature Insights allow you to focus your scopes on a specific section of your signal.  Maybe you want to focus on one face, or a window in the background.  By setting a feature insight within your preview palette, all of your scopes will highlight just that portion of the signal. Or, you can highlight a portion of your signal in a scope and find out exactly which part of your signal is responsible for that value. 

### HDR ###

Throughout the app, we've revamped scales and features to support modern HDR workflows and measurements.

### User Targets ###

User targets let you set custom values that appear as targets on your scopes.  This makes it easier to match specific values between shots.


# Getting Started #

## Installing ##
ScopeBox is a self-contained application. Just drag and drop the application to your Applications folder or any other location on your hard disk, and you're ready to start using it.

As a rule of thumb, if your device works as a source in Quicktime X, it should work within ScopeBox.

## Uninstalling ##
If you want to uninstall ScopeBox, simply drag the application to the trash.

ScopeBox stores its preferences in a file named "com.divergentmedia.scopebox.plist" in your (username)/Library/Preferences/ folder. Layouts and saved source settings are stored in (username)/Library/ Application Support/.

## Registering ##
When you first launch ScopeBox, it will run as "unregistered". To enable the full feature set of ScopeBox, you must enter a serial number in the Registration dialog. You may also visit (http://www.divergentmedia.com/scopebox/trial)[http://www.divergentmedia.com/scopebox/trial] to obtain a time-limited trial key, which will allow you to try all of the features of ScopeBox before buying.

If you've already purchased ScopeBox, click the "Enter Key" button and enter your name and key exactly as it is shown in your registration information.  

![Registration Window](ScopeBox/images/registration.png)

## Updating ##
ScopeBox automatically checks for updates during startup. If you'd like to force it to check for an update, select "Check for Updates" from the ScopeBox menu.  You must have an active subscription or a perpetual license to get updates.  If your subscription has lapsed, you many continue to run the latest version that was covered by your subscription.

You can disable automatic updates via the "General" tab of the preferences dialog.

ScopeBox can only check for updates if you are currently connected to the internet. If your ScopeBox system is not connected, you can always download an updated copy from <http://www.divergentmedia.com/scopebox>.

# Application Overview #
The main ScopeBox window can be broken into 2 distinct regions. On launch, the majority of the screen hosts the palette region.  The sidebar, on the right side of the window, contains all of the controls and adjustments for sources, and palettes.  The sidebar can be hidden at any time using the button in the upper right corner of the window, or using the Command-\ keyboard shortcut. 

![A sample view of ScopeBox's main window.](ScopeBox/images/MainWindow.png)

## The Sidebar ##
Changing the settings of one of your sources or palettes is done in the sidebar.  The sidebar will open to the "source selection" pane, where you can add a live source, a ScopeLink source, or a movie file.  The icons at the top of the sidebar allow you to toggle between palette settings, source settings, still images, and predefined targets.  Clicking the gear icon in the upper right corner of any palette allows you to adjust settings for that palette. 

## The Palette Region ##
Once you've added a source, you're free to start inspecting the signal in a variety of ways. You do this by adding palettes to the source. Each new palette you add will give you an additional tool to quantitatively or qualitatively examine the video, audio, or timecode signal of that source.

When a new palette is added, it appears in the Palette Region. This area serves as your general workspace for analyzing sources. You can add or remove palettes, change the source they monitor, or alter their size and position at any time.  Click the gear icon in the upper right corner of any palette to access its settings. 


# Dealing with Sources #

## Adding a Source ##
The Source menu allows you to add new sources. In addition, new sources can be added via the sources tab in the sidebar.  Click the "Add new source" button. 

![Opening a new source from the Source menu.](ScopeBox/images/AddingSource.png)

By default, you will be presented with the options "Add Live Source," "Add Movie Source," "Add ScopeLink Source," and "Add Test Patterns." 

The "Movie Source" menu allows you to open video files within ScopeBox.  ScopeBox currently supports MOV, MP4, MTS, M2T, MXF, and BRAW sources.  ScopeLink is covered in a [separate chapter](#scopelink).

### Unavailable Sources ###
If a source is unavailable, it will be grayed-out in the menu. A source may be unavailable for many reasons:

* It is already open in ScopeBox or another application.
* Your system is missing the necessary codecs or drivers.

If you are having problems with a device please refer to the troubleshooting section near the end of this manual.

## Removing a Source ##
To remove a source, click the "x" next to the source within the sidebar. 

![Removing a source](ScopeBox/images/removingASource.png)

## Source Settings ##
Once you've added a source, a small preview and the source settings will appear.   This provides a quick way to confirm you are receiving the proper video and audio signals. When opening a movie, you'll also get playback controls on this screen.  

The settings available will depend on the type of source you're working with.

### Video ###
You may change the name of the source using the Device field - just click and begin typing. This can be useful when using more than one of the same device.

The "Input" dropdown allows you to select which input you would like assigned to this source. This dropdown will only show up for devices or capture cards with multiple inputs. However, many such devices choose to present themselves as discrete devices rather than a single source with different inputs. In those cases, the dropdown will be disabled, and you'll select the input as part of the device selection process.

![The source setting sidebar](ScopeBox/images/SourceSidebar.png)

### Audio ###
The audio section allows you to select an audio source for recording and adjust the level at which the audio is played through your computer speakers.

The preview audio adjustment is for monitoring only - any changes you need to make to adjust the levels you see within your VU meters should be done in your camera's audio controls.

### Timecode ###

If your device supports timecode, via embedded (RP188) or serial, you may enable the timecode section to configure those settings.  

Because serial deck control does not provide information about the timecode format of the device, you'll also need to choose the appropriate timecode format to tag incoming timecode.

### Preview Adjustments ###
It's often helpful to preview a signal with adjustments applied, to get a sense of how an image will look after color correction is applied or other changes are made. For example, when shooting in the log space, you may wish to preview the image in the linear space. The Preview Adjustments section of the source settings allow you to apply these adjustments via LUTs (look up tables)

ScopeBox supports two LUT formats, cube (1d and 3d) and 3dl. To apply a LUT, check the Preview Adjustments box and then click Set Path. This will allow you to load a LUT in one of the supported formats. You may easily toggle the LUT on and off by checking the Preview Adjustments box.

LUTs impact all of the palettes, including the preview and any scopes. LUTs **do not** impact recorded files. LUTs are automatically reloaded if they contents of the LUT file changes on disk.

We support a variety of LUT formats in ScopeBox, but many production pipelines use custom LUTs.  If you've got a LUT that isn't working with ScopeBox, send us a copy at <support@divergentmedia.com>, along with a brief description of what the LUT is intended to do.

The preview adjustments section also allows you to adjust the matrix, transfer and primaries used for displaying and processing your source.  You can also use this section to rotate and flip your image. 

## Saving and Recalling Sources ##
Once you've adjusted all of your source settings, you can save a preset. Highlight the source in the source settings tab, and then select "Save" from the Source menu. This will save all of the settings for the source.

To recall a source, select it from the "Recall Saved Source" menu.

Sources will be saved with the device name set in the sidebar (see above).

You can set a default source, which will automatically be loaded (if available) when ScopeBox is launched, in the preferences.

# Loading Stills #

ScopeBox provides a "still-store" which can load images to be overlaid on other palettes.  You can load images via the media gallery tab in the sidebar.  This provides a convenient way to compare your signals against reference images. 

![Loading Stills](ScopeBox/images/StillStore.png)

# Target Values #

Target Values in ScopeBox allow you to define preset values that will be marked on your scopes.  From the target values tab, you can set targets using a standard color picker.  The label you add will be shown within your scopes.

![Setting Targets](ScopeBox/images/Targets.png)

# Palette Overview #
## Working with Palettes ##
ScopeBox displays all content in flexible palettes within the palette region of the ScopeBox window. The settings for each palette are displayed in the sidebar on the right side of the ScopeBox window whenever a palette is selected.

You may add multiple copies of each palette, each with its own settings. For example, you may choose to open a preview palette for each of your sources, and you may choose to also multiple preview palettes for a single source, each with distinct settings.

![A standard palette in ScopeBox](ScopeBox/images/waveform.png)

### Adding Palettes ###
To add new palettes, select the desired palette type from the Palettes menu or right click on the background of the ScopeBox window or on the source palette.

### Closing Palettes ###
To close a palette, click the "x" in the upper left corner or hit the delete key while the palette is selected. You may also right click palette and select "close."

### Moving Palettes ###
Click and drag to move a palette to the desired position. You can also use the arrows keys for very precise positioning of a selected palette.

![A waveform palette unselected (left) and selected (right)](ScopeBox/images/DualWave.png)

If you wish to organize your palettes with more precision, you can "Enable Snapping" in the "View" menu. This will constrain your palette's movement and re-sizing to an internal grid, allowing you to easily line up multiple palettes.

### Resizing Palettes ###
Click and drag on the lower right corner to resize a palette.

### Soloing Palettes ###
Soloing a palette allows you to temporarily hide all other palettes and focus your attention on the selected palette re-sized full screen. You can activate a palette's soloing by choosing Solo Palette from the View menu, by right clicking on the palettes.

### Switching Sources ###
When you have multiple source open, you may adjust which source a palette is previewing by clicking the "gear" icon in the upper right, and then selecting a source by clicking on it.  

## Common Settings ##

Some settings are shared among many palettes. They are detailed in this section.

### Intensity ###
When in weighted mode, the intensity slider adjusts the brightness of the scope. By changing this value, you adjust the visibility of areas of low pixel concentration.

### Colors ###
The color of the graticules and traces can be set in the application preferences, available under the "ScopeBox" menu.


## Feature Insights ##

Feature Insights let you select just a portion of your image or signal to focus on.  Once you enable a feature insight, your scopes and preview will all highlight the relevant portion of your signal.  To set a feature insight, hold the option key and then click and drag on a palette to select a portion of the image or signal. You can reset your feature insights using the view menu. 

![Feature Insight Highlighting a Portion of the Signal](ScopeBox/images/featureInsight.png)


# Preview Palette #
The Preview palette displays video source output and can replace a traditional field monitor for checking focus, framing, and color calibration.

![The Preview Palette with 4x3 mask, center marks, and title safe overlays enabled.](ScopeBox/images/PreviewWithOverlays.png)


## Controls ##
When you select the preview palette, the following controls will appear in the sidebar.

> **Changes made to the image in monitor calibration only affect what you see in the preview palette. They are not reflected in any other scopes. Monitor Calibration should only be used to ensure your preview accurately reflects the video signal. You can do this by calibrating to color bars sent from your source device.**

### Aspect ###
Controls the aspect ratio at which the video source will be displayed.

Standard Definition video uses rectangular pixels whereas computer monitors use square pixels. This can result in video images that are stretched when displayed on a computer. If you're shooting HD, the 16:9 option should be selected by default. For SD sources, you can either view the native "rectangular" pixels, or the corrected "square" display. When you choose a new source, ScopeBox will automatically set your preview's aspect to match that of the incoming image.

### Zoom ###
Zoom sets the size of your image. 100% and 200% set the video image to the corresponding magnification no matter the size of the preview palette. This gives you a pixel-for-pixel view of your image with no interpolation from the graphics card or video re-size, which is especially useful when trying to set focus. However, if your palette is too small you may not see the whole image. "Fit to Size" fits the video to fill the palette, but does so by re-sizing the image which may introduce minor sub-sampling interpolation - leading to a slightly blurrier image.  When zoomed in, you can click and drag to pan within the image. 

### Mask ###
The mask overlay draws blue bars as a framing guide when shooting at an aspect ratio other than the destination ratio. Using this will allow you to frame shots not only for the acquisition format, but for any other formats you may have to deliver to as well. For instance, if you know the video you are shooting in HD (16x9) will be used in an SD production, setting your mask to 4x3 will allow to see where by default the image will be cropped in the format change.

### Monitor Calibration ###
The Saturation, Brightness, and Contrast sliders provide simple correction of the Preview image. These corrections are used to compensate for differences in computer monitors. Calibrating the Preview palette ensures that the image accurately represents what the camera is shooting. Any changes made do not affect the video captured to disk or the video monitored in any other scope.

### Blue Gun ###
When checked, the Preview palette displays the blue channel as black and white, ignoring red and green. This simulates the "blue only" button on many CRT monitors, which is useful when calibrating a monitor with SMPTE color bars.

### Title Safe ###
Title Safe adds two overlay boxes to the video. The outer box shows the graphics safe region and the inner box shows the title safe region. Make sure important action happens inside the title safe box, as older televisions may crop beyond it.

### Rule of Thirds ###
Provides a 3x3 grid to assist with composition.

### Center ###
Provides center cross-hairs to assist with composition.

### Overlays ###

#### False Color ####
False color colorizes the preview monitor with a color mapping based on the signal's luminance value. ScopeBox ships with the Red, Arri and ST2048 profiles. 


#### Image Overlay ####
Overlays allow you to layer an image, movie, or live source on top of your source. This can be used for custom guides for framing around your productions lower thirds, a background that will later be chroma keyed into the shot, or video footage you need to match framing or exposure in.

After enabling the "image overlay" option, you'll be shown a list of sources. To learn about loading image sources, see the [loading stills](#Loading-Stills) section. 

Below the image well is a slider to adjust the opacity of the overlay.

# Audio Meters #
The Audio Meter displays the level of the audio signal in dBFS. It provides both an instant meter and an averaging peak meter. Every spike is displayed, even if very brief.

![The Audio Meter Palette](ScopeBox/images/AudioLevels.png)

## Controls ##

### Channel Count ###
By default the Audio Meter will show all channels currently reported by a source. However, many devices report a fixed number of output channels, which can waste valuable screen space displaying empty channels. If your capture device always sends eight channels to ScopeBox, but you are only using two, you can set channel count to 2 to only present the first two channels.

### Scale ###
Different source formats require different peak audio levels. This level is often referred to as Unity. When working with bars and tone, or when trying to set your mic volumes at the proper levels, you want to know exactly where unity lies in the Audio Meter. ScopeBox provides a set of Scale markers for each of the three major unity levels found on professional video devices -12, -14 and -20 dB.

### Peak Hold ###
This shows you the highest level achieved since the peak hold was reset.  Click the "reset peaks" button at any time to reset this value. 

# Surround Meters #

The Surround Meters give you a way to visualize your audio signal in a surround sound context. This allows you to quickly analyze the surround components of your audio mix, even in environments that don't lend themselves to proper audio monitoring.

![The Surround Meter Palette](ScopeBox/images/SurroundLevels.png)

Because audio inputs do not inherently pass information about how to lay out each channel in a surround environment, ScopeBox provides a variety of popular channel layouts. Select the layout which matches the input layout you are feeding ScopeBox.

The palette settings also allow you to set the scale, and enable a "peak hold" option, similar to the Audio Meters (see [section 7](#Audio-Meters)).

# Waveform #

The Waveform scope provides a view of the luminance in the video signal. The vertical axis corresponds to luminance while the horizontal axis matches the horizontal axis of the video source.

![The Waveform Palette](ScopeBox/images/waveform-wide.png)

## Controls ##
### Mode ###
The Mode dropdown allows you to choose the method ScopeBox uses to render your scope. Each mode offers you different information:

*Weighted* mode looks more like a traditional raster scope and expresses the number of pixels at a given value by varying the brightness.

*Mono* displays every data point at full intensity, which can be useful in ensuring complete legality. With weighted views it is possible to miss a small pixel region that is out of range.

*Colorize* replaces the traditional monochrome tone in a scope with the actual color that it represents. For example, if someone is wearing a bright red shirt, there will be a bright red streak where the scope renders those pixels.

### Zoom Blacks ###
Often colorists want to get a detailed look at the darkest parts of a signal.  The "Zoom Blacks" slider magnifies just the lower values of the signal. 

### Filter ###
The Filter dropdown allows you to select between the two commonly found filter types found on hardware waveform monitors - *Luma* and *Chroma*. Luma is the default, causing the waveform to display only the luminance (Y) channel of your video. Chroma will display only the chrominance (C) channel of your video.

### Instantaneous Envelopes ###
Instantaneous Envelopes help ensure that you don't miss any data within your waveform monitor, even when it's just a single pixel. Checking the box will cause two bounding lines to be added to your trace, one showing the maximum values for your waveform, and one showing the minimum values for each vertical line.

### Peak Envelopes ###
Peak envelopes show the maximum and minimum values for your waveform over time. This allows you to look away from your scopes, and still know whether you exceeded a target threshold. The reset button will clear the peak values.

### Scale ###
There are five different Scale options available for measuring your waveform. These are IRE (the traditional scale for a waveform monitor), 8 bit, 10 bit and mV (millivolt). The 8 bit and 10 bit options allow you to measure your waveform according to the actual sample values in the signal. Millivolt allows you to compare against the signal shown by a traditional hardware waveform monitor or oscilloscope.  ST2084 is the Dolby PQ Standard scale. 

# Vectorscope #

The Vectorscope displays chrominance (color) information. Saturation is indicated by distance from the center while the position around the circle indicates hue.

![The Vectorscope Palette](ScopeBox/images/vectorscope.png)

The markers on the Vectorscope (R, Y, B, etc) indicate colors. The boxes show where the signal should land when displaying the standard SMPTE color bars signal, providing a guide for evaluating saturation. The targets are plus and minus 5 degrees and 5% saturation.

The rings represent saturation percentage, in 20% increments (the innermost circle represents 20% saturation, the next 40%, etc).

## Controls ##

### Colorspace ###
The colorspace option provides three different colorspaces with which to view the vectorscope. These are Rec. 601, Rec. 709 and Rec2020/2100. By default, ScopeBox will automatically set the colorspace based on your source. These colorspaces will adjust the color targets and scaling of the vectorscope.

### Mode ###
The Mode dropdown allows you to choose the method ScopeBox uses to render your scope. Each mode offers you different information:

*Weighted* mode looks like a traditional scope and expresses the number of pixels at a given value by varying the brightness.

*Mono* mode displays every data point at full intensity, which can be useful in ensuring complete legality. With weighted views it is possible to miss a small pixel region that is out of range.

*Colorize* mode replaces the traditional green in a scope and with the actual color that it represents. For example, if someone is wearing a bright red shirt, there will be a bright red streak where the scope renders those pixels.

### Instantaneous Envelopes ###
Instantaneous Envelopes help ensure that you don't miss any data within your vectorscope, even when it's just a single pixel. Checking the box will cause draw a boundary around the maximum values of your vectorscope.


### Peak Envelopes ###
Peak envelopes show the maximum values for your vectorscope over time. This allows you to look away from your scopes, and still know whether you exceeded a target threshold. The reset button will clear the peak values.


### Flesh Line ###
The Flesh Line is an industry standard reference line along which skin tones will generally fall. It's most useful as a static reference between scenes or cameras.

### Grat Style ###
The default graticule style for the vectorscope a standard set of concentric circles, representing saturation.

ScopeBox also offers a "hue vectors" graticule style, which provides a more modern, color correct and camera matching specific overlay. This view gives more contextual information for hue adjustments across the entire range of saturations, while removing unneeded clutter more appropriate for signal-analysis and legality monitoring. The perpendicular hash marks on each line represent a 75% target.

### Show Targets ###

See the [Target Values](#Target-Values) section to learn more about how to set targets.  You can enable or disable them within a given palette. 

Hue vectors graticule by [Alexis Van Hurkman](http://vanhurkman.com/wordpress/?p=2563) is licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/deed.en_US)

# HML Balance #

The HML Balance palette can be thought of as three distinct vectorscopes, displaying information about the "high," "mid," and "low" components of your signal. This can be helpful for identifying color casts in specific luminance regions of your image, like shadows or highlights.

Because the crosspoints between the three vectorscopes are configurable, this palette can be filtered in a variety of ways to allow you to focus on just one component of your signal.

Many of the controls are similar to those found on the vectorscope, but there are some HML-specific controls as well.

![The HML Balance Palette](ScopeBox/images/HMLBalance.png)

## Controls ##
### Zoom ###
The Zoom control is a variable zoom, allowing you scale up the scopes to see even the most minute detail. Keep in mind that with an 8-bit signal, the amount of resolution available in the display is inherently very limited.

### Luma Threshold ###
The "low" and "high" values act as low- and high-pass filters, respectively. Everything below the value entered in the "low" field will be displayed on the low scope, everything above the value entered in the "high" field will be displayed in the high scope, and everything in between will be drawn in the mid scope.


# RGB Parade #
The RGB Parade displays individual waveforms for each channel (Red, Green and Blue) of your video signal.

![The RGB Parade Palette](ScopeBox/images/RGBParade.png)

You can use the RGB Parade to gauge separation between the color channels. For example, when setting white balance, all three channels should be equal horizontally, indicating that you have equal amounts of red, green and blue, thus creating white.

The RGB Parade is also useful when trying to determine the cause of a color cast in shadow or highlight areas. Such casts can be caused by clipping (overexposure or underexposure) in one particular color channel. It is often difficult to diagnose this issue without a specialized tool like the RGB Parade.

## Controls ##
### Layout ###
The layout control allows you to display your RGB parade as either "R,G,B," "B,G,R," or "Overlay." Overlay mode will stack each channel, and composite their values.

### Zoom Blacks ###
Often colorists want to get a detailed look at the darkest parts of a signal.  The "Zoom Blacks" slider magnifies just the lower values of the signal. 

### Mode ###
The Mode dropdown allows you to choose the method ScopeBox uses to render your scope. Each mode offers you different information:

*Weighted* mode looks like a traditional scope and expresses the number of pixels at a given value by varying the brightness.

*Mono* mode displays every data point at full intensity, which can be useful in ensuring complete legality. With weighted views it is possible to miss a small pixel region that is out of range.

### Instantaneous Envelopes ###
Instantaneous Envelopes help ensure that you don't miss any data within your monitor, even when it's just a single pixel. Checking the box will cause two bounding lines to be added to your trace, one showing the maximum values for your trace, and one showing the minimum values for each vertical line.

### Peak Envelopes ###
Peak envelopes show the maximum and minimum values for each channel over time. This allows you to look away from your scopes, and still know whether you exceeded a target threshold. The reset button will clear the peak values.

# YCbCr Parade #

The YCbCr Parade displays individual waveform monitors for the Y, Cb and Cr components of the signal.

![The YCbCr Parade Palette](ScopeBox/images/YUVParade.png)

The YCbCr Parade is useful for signal chain diagnosis since most video devices process in the YUV colorspace.

## Controls ##

### Mode ###
The Mode dropdown allows you to choose the method ScopeBox uses to render your scope. Each mode offers you different information.

*Weighted* mode looks like a traditional scope and expresses the number of pixels at a given value by varying the brightness.

*Mono* mode displays every data point at full intensity, which can be useful in ensuring complete legality. With weighted views it is possible to miss a small pixel region that is out of range.

### Instantaneous Envelopes ###
Instantaneous Envelopes help ensure that you don't miss any data within your monitor, even when it's just a single pixel. Checking the box will cause two bounding lines to be added to your waveform, one showing the maximum values for your waveform, and one showing the minimum values for each vertical line.

### Peak Envelopes ###
Peak envelopes show the maximum and minimum values for each component over time. This allows you to look away from your scopes, and still know whether you exceeded a target threshold. The reset button will clear the peak values.

# Luma Histogram #
The Luma Histogram displays the range of luminance levels in the video signal, with black on the left and white on the right. The height of each line corresponds to the percentage of the image that occurs at that luminance level.

![The Luma Histogram Palette](ScopeBox/images/LumaHistogram.png)

## Controls ##
### Scaling ###
The Luma Histogram can be toggled between "log" and "linear" scaling. In log mode, each horizontal graticule represents an order of magnitude - 10, 100, 1000 and so on. This means that even luminance levels with relatively low frequency within your signal will be easily visible within the palette.

Linear scaling causes the vertical axis to be scaled to the height of the most populated luminance level.

### HDR Overlays ###
HDR overlays show a lower fidelity histogram of common ST2084-specific luma ranges, along with a total coverage percentage.

# RGB Histogram #
The RGB Histogram displays the intensity of the Red, Green and Blue signals. Similar to the Luma Histogram, the leftmost column is the lowest intensity and the rightmost is the highest intensity.

![The RGB Histogram Palette](ScopeBox/images/RGBHistogram.png)

The RGB histogram is particularly useful when working with chroma key shots. The key color should be as even as possible for clean keying. Doing so produces a very tight clump of long bars rather than a wider clump of short bars.

## Controls ##

### Layout ###
The layout control allows you to adjust whether you're viewing the individual R, G, and B components separately, or overlayed as a single composite. 

### Scaling ###
The RGB Histogram can be toggled between "log" and "linear" scaling. In log mode, each horizontal graticule represents an order of magnitude - 10, 100, 1000 and so on. This means that even levels with relatively low frequency within your signal will be easily visible within the palette.

Linear scaling causes the vertical axis to be scaled to the height of the most populated intensity for a given channel.

# Timecode #
The Timecode palette displays the timecode as sent from the video source, generally when playing a tape or recording. Some devices operate in "free run" mode, which generates timecode without a tape present. Timecode is formatted in SMPTE standard format - Drop Frame timecodes have a semicolon (;) between the seconds and frames place whereas Non Drop Frame timecodes have a colon (:).

![The Timecode Palette](ScopeBox/images/Timecode.png)

# Channel Plot #

The channel plot allows you to map two channels of a video signal on an X/Y axis. The box drawn within the scope helps you determine when your signal will be clipped by a colorspace conversion (gamut errors).

![The Channel Plot Palette](ScopeBox/images/ChannelPlot.png)

## Controls ##
### Axis Controls ###

There are six different channels which may be plotted on either the X or Y axis. These are Y, Cb, Cr; R,G,B; X Y Z; and x y. The channel plot is primarily useful when plotting values within a single color format. For example, you'd generally want to plot R against G or B, rather than against Y,Cb,Cr. By plotting R versus G, and in a second palette, G versus B, you'll be able to quickly judge whether any data will be clipped during the YCbCr to RGB conversion.

# CIE Plot #
The CIE plot provides a standard display allowing you to see how your signal fits within a given colorspace. The CIE Plot by itself shows the gamut of all visible chromaticities.  Within the CIE Plot palette, you can enable additional colorspaces to determine whether your signal is within gamut for these.  ScopeBox comes preset with Rec 709, P3, and Rec 2020 primaries. You can also enable custom primaries and set your own values. 

![CIE Plot displaying Rec709 color bars with Rec 709 and P3 primaries](ScopeBox/images/cieplot.png)

# Luma and RGB TimeTrace #
Traditional scopes only show you what's happening right now.  The Luma and RGB TimeTrace palettes continuously refresh, showing you your luma (or RGB) history over the last 300 frames.  You can use the TimeTrace to catch an excursion or to get a quick glance view of how your signal changes over time.   

The signal draws in an endless loop along the X axis.  The Y axis shows a histogram of your signal, each line being one frame of video, with black on the bottom and white at the top.  

![TimeTrace showing Luma](ScopeBox/images/timetrace.png)


# ScopeLink #
ScopeLink allows you to monitor the signal from other applications on your computer, without any special hardware. Once installed, ScopeLink appears as an output option within supported applications, just like a traditional hardware output device.

Within ScopeBox, you can add the ScopeLink device from the source menu, just like any other source.  Select the application you'll be using with ScopeLink.

![Adding a ScopeLink Source](ScopeBox/images/scopelinkSource.png)



## Installing ScopeLink ##

Installing ScopeLink requires administrator privileges on your computer. The first time you attempt to add a ScopeLink source, you'll be prompted to install ScopeLink. You can manually initiate the installation by selecting "Install Additional Software" from the ScopeBox menu.

The installation will prompt for your administrator password and install the ScopeLink software on your system.

## Configuring ScopeLink ##

After installing, ScopeLink must be activated within the individual applications you wish to use with ScopeBox. This should only need to be done once per application.

### Adobe Premiere and Prelude ###
To configure ScopeLink with Adobe Premiere Pro, or Adobe Prelude, begin by launching the application you wish to configure. Start a new project (the format doesn't matter). From the menu bar, select "Adobe Premiere" (or "Adobe Prelude" and then "Preferences." Within the preferences dialog, select the "Playback" option.

![Configuring Adobe Premiere](ScopeBox/images/PremierePreferences.png)

Check the box next to the ScopeLink device. You may also activate other devices if you wish. Click "OK," and then restart the application.

When used with Adobe Premiere Pro or Adobe Prelude, ScopeLink will transmit 8bit Rec. 709 signals, and ScopeBox will default to viewing within the Rec. 709 colorspace.

### Adobe After Effects 2014 and later ###
To use ScopeLink with Adobe After Effects 2014 and later, begin by launching After Effects. Select "Preferences" from the "After Effects" menu, and then "View Preview." Enable Mercury Transmit, then set ScopeLink as the Video Device. We recommend unchecking "disable video output when in background".

![Configuring Adobe After Effects 2014](ScopeBox/images/AfterEffects2014.png)

Click "OK" and then relaunch After Effects.


### Final Cut Pro X ###
Launch Final Cut Pro X and open the Preferences.  Select ScopeLink in the "A/V Output" dropdown.

![Select ScopeLink in the A/V Output dropdown](ScopeBox/images/FCPXPreferences.png)

Close the preferences and select the "Window" menu from the top of the screen.  Click "A/V Output" to enable live output of your sequence.

![Select A/V Output from the Window menu](ScopeBox/images/AVOutput.png)

Restart Final Cut Pro X to begin using ScopeLink.

### DaVinci Resolve ###

To use ScopeLink with Resolve, first add the ScopeLink OFX plugin from the Library.  

![Add ScopeLink Plugin](ScopeBox/images/selectResolveNode.png)

After you've added the plugin to your project, add it in your node graph so that it has both an input and an output.  ScopeLink will monitor whichever signal you feed into the ScopeLink node.  Users may wish to add the OFX as a timeline node to view scopes across clips. Note that ScopeLink will monitor the image before an output postprocessing is applied.

![Add ScopeLink Plugin](ScopeBox/images/resolveNode.png)

### Other Applications ###
Other applications which support either CoreMedia-based output, OFX, or Adobe Transmit-based output may work with ScopeLink. Contact support if you'd like information on using a specific application with ScopeLink.

## ScopeLink Settings ##
Depending on the application hosting ScopeLink, there are a variety of settings you may adjust.  After adding a ScopeLink source, click the source settings in the sidebar.  In some applications, you'll be able to set frame size, colorspace and frame format.  

These changes alter the type of frame being sent by the host application.  After changing these settings, you'll need to restart the host application.

Depending on your host application, selecting a non-native format (for example, requesting RGB frames from a YCbCr sequence) may increase system overhead.

# View Menu #
The View menu allows you to customize the look and feel of the main ScopeBox window. Each of the major sections of the window can be shown or hidden from the View menu. In addition, you can save and recall preset palette layouts and configurations.  You can also choose to make the application fullscreen.

## Saving a new layout ##
To save a custom layout, arrange the palettes as desired and select "Save Custom Layout...". You will be prompted to name your layout.

After clicking OK, you will find your newly saved layout in the Layouts menu.

## Restoring a layout ##

Choose any of the layouts found in the custom layout section to restore the main window to this configuration.
You can set a default layout, which will be loaded every time ScopeBox is launched, via the preferences. If you ever wish to override this default, simply hold the shift key while launching ScopeBox.


# Performance #

ScopeBox is a high end application and requires a lot of system resources to run properly. The application uses a number of techniques to actively monitor video processing and allocate CPU resources to ensure video is captured without frame drops.

If the sources often show the drop frame warning icon, there are a number of options for increasing available resources and decreasing resource demand.

* Quit other applications
* Lower the preview level of open sources
* Lower the palette count
* Close RGB Histogram and RGB Parade palettes, as well as CIE
* Turn on subsampling, within the source settings

If none of these actions work then you may need more RAM, a faster video card or a faster machine.

# System Requirements #

ScopeBox is a flexible application that can be used with many hardware configurations. System requirements will vary drastically based on your specific usage and hardware. The following are guidelines for the minimum system required to run ScopeBox in its default layout.

* Intel-base Macintosh
* Graphics card with support for Metal.
* 8 GB of RAM.
* 120 MB of disk space.
* Mac OS X 10.12.5 or later.

> **These minimum requirements are not a guarantee ScopeBox will work with your exact configuration. Please thoroughly test your hardware with the trial version before making any decisions. You can download the trial at <http://www.divergentmedia.com/scopebox/trial>**

# Troubleshooting #

## My video input is not showing up / is grayed out/ does not work ##
Make sure your video input isn't in use by another application, check input cabling, and restart ScopeBox. Verify that your camera is outputting video.

Also, verify that you have the proper codecs or drivers installed. While this is not a absolute assurance the device should work in ScopeBox, you can confirm your system is set up properly by checking to see if the device works in as a "new video recording" source in QuickTime Player X.


# Other Resources #

If you need additional support using ScopeBox, please try the resources listed below.

Support on the Web
<http://www.divergentmedia.com/scopebox>

Email support
<support@divergentmedia.com>

Phone support
toll free - 888.632.0904
