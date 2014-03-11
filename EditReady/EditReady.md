# Welcome to EditReady #

## Welcome ##

EditReady provides easy, powerful, and fast transcoding for video professionals.  

This manual will introduce you to the basic of EditReady, and provide suggestions for ways to use it within your post-production workflow.


For news, updates, and support regarding EditReady, or to learn about other products from Divergent Media, visit [http://www.divergentmedia.com](http://www.divergentmedia.com).

## Overview ##

Modern production pipelines often involve generating QuickTime files with a variety of codecs.  A single production may use a mix of "A-Camera" files in ProRes422, "B-Camera" footage in H.264, as well as archive footage in formats like Apple Intermediate Codec.  


EditReady lets you take this mix of files and convert them into a single mezzanine format, offering your post-production pipeline simplicity, reliability, and performance.


EditReady can also generate high quality proxy media, so that you can take all of your media with you on the road.

# Getting Started #

## Installing ##

EditReady is available as a direct download from [http://www.divergentmedia.com](www.divergentmedia.com) and as a purchase from the Mac App Store.  If you've downloaded it from our website, just drag and drop the application into your Applications folder.  If you've purchased from the Mac App Store, EditReady should already be in your Applications folder - no installation necessary.


In order to convert footage to or from the Avid DNxHD Codec, you'll need to have the free DNxHD plugin installed.  It can be downloaded from [http://www.avid.com/dnxhd/](http://www.avid.com/dnxhd/).  

## Uninstalling ##

To remove EditReady, simply drag it to your trash.

## Registering ##
When you first launch EditReady, it will run in trial mode, which will only transcode the first minute of each clip. To lift this restriction, you must purchase an unlock key from <http://store.divergentmedia.com>, or purchase a copy from the Mac App Store.

If you've already purchased EditReady, click the "Enter Key" button and enter your name and key exactly as it is shown in your registration information. You may display this menu at any time by selecting "Registration" from the EditReady menu.  Make sure you don't have any extra spaces or other stray characters in the "key" field, as this can cause the key to be rejected.

## Updating ##
EditReady automatically checks for updates during startup. If you'd like to force it to check for an update, select "Check for Updates" from the EditReady menu.

## Reinstalling ##

If you've purchased from our website, you can download a "fresh" copy at any time from <http://www.divergentmedia.com/filedownload/editready>.  After downloading, you can unlock it with your key.  If you've lost your key, you can look it up at <http://www.divergentmedia.com>.


# Application Overview #

EditReady accepts files in the QuickTime MOV, MP4 and M4V formats. In general, if a file plays in QuickTime Player, it'll play in EditReady.

While you can customize many parts of the conversion process, EditReady includes a variety of presets so you can get started right away.

## Basic Usage ##

Clips can be added to EditReady by selecting "Open" under the "File" menu, or by dragging clips into the EditReady window.  Your clips will appear with thumbnails in the EditReady window.  You may toggle between "list view" and "thumbnail" view using the selector in the toolbar.

If you'd like to convert all of your clips, simply click the "convert all" button at the top of the window.  If you'd only like to convert some clips <<FLAG CLIPS>>.

Clicking the convert button will reveal the batch settings pane.  EditReady includes a variety of presets for popular editing formats like ProRes and DNxHD.  You can customize these further by creating [custom presets](#custom-presets).

Regardless of the preset you select, you have the option of adjusting the destination folder and destination file name.  See ["Naming your Files"](#naming-your-files) for details.

When you're ready to go, click Convert.

## Monitoring Progress ##

Each clip will show a progress indicator below the thumbnail.  In addition, you can see batch progress within the toolbar.  You may pause or resume conversion using the play/pause indicator in the timeline.


# Metadata #

One of the most powerful features in EditReady is the ability to view and edit the metadata contained in your files.  Clicking the blue <<carrot??>> will reveal the most common metadata from your file.  Clicking the "Show all" button will open a separate window with all of the metadata.


## Browsing Metadata ##

Metadata may include camera settings like F-Stop, Iris, and Shutter, as well as items like Location (if your camera has GPS), media serial numbers, or even diagnostic data.  

In some cases, there may be multiple entries for a single category of metadata.  For example, your camera may store a "Creation date" in a variety of places throughout the file.  In this case, EditReady will display "Multiple Values" and provide a disclosure triangle to reveal the individual entries.

If your camera includes GPS data in the metadata, those fields will have a "map" button, allowing you to view the clip location on a map.  Dates within your metadata will be normalized to the current timezone of your computer.  

Some metadata is intended only for use by the camera manufacturer during troubleshooting, so may appear as simply a string of numbers or letters within EditReady.


## Editing Metadata ##

One of the most powerful futures in EditReady is the ability to edit your metadata.  To edit an entry, simply double click and begin typing.  Depending on the field, EditReady may enforce requirements on the type of information you can entry (for example, date fields may only contain a valid date).

## Adding Metadata ##

To add a new entry <<STUFF HERE>>

## Removing Metadata ##

To remove a metadata entry, click the minus sign to the right of the entry.


# Naming Your Files #

EditReady includes powerful file naming features, so that you can keep track of all the files in your post production pipeline.

The popup menu to the right of the <<"Dest File Name">> label is pre-populated with a handful of options.  You may, for example, choose to have your output file names match the input file names, or have them be named with an automatically incrementing number.  

## Customizing File Names ##
In addition to the presets, you can add additional values from your file's metadata to the file naming scheme.  When viewing your file's metadata (see the [previous chapter](#browsing-metadata)), you will notice a small "tag" icon next to each metadata entry.

Drag that tag to the "dest file name" field to include that metadata element in the destination filename.

For example, you may wish to add the "Reel" key and the "Creation date" keys to the existing "auto-increment" entry.  You can drag and drop to rearrange values within the "dest file name" field, and you can type to add characters like dashes or underscores.  So, you could easily have all of your output files named "<Reel>-<CreationDate>-<Auto-increment>.mov".  



# Custom Presets

EditReady is an integral part of a post production workflow. To make the usage even more seamless, you can create custom presets that match your workflow needs.  Begin by selecting the "custom" preset in the preset dropdown.  

## Video Format ##
EditReady allows you convert to Apple ProRes, Avid DNxHD and H.264.  You may also choose to pass the input video directly to the output file (using the "passthrough" option).  This is helpful if you only need to adjust the audio track of your file.

### Apple ProRes ###

Apple ProRes is a popular editing format, whether you're working with Apple Final Cut Pro X, Avid Media Composer 7, Adobe Premiere Pro CC, or apps like Blackmagic Design Resolve.  

EditReady allows you choose from five different ProRes options - ProRes 422, 422 HQ, 422 LT, 422 Proxy, and 4444.  The "right" choice will be different for each workflow, but in general if your source is already compressed (an h264 file from a GoPro camera for example), the standard ProRes 422 file will be fine.  

### Avid DNxHD ###

DNxHD is a popular editing format for workflows involving the Avid ecosystem.  EditReady provides three DNxHD choices, Low, Medium, and High.

These choices may be confusing if you're used to seeing DNxHD listed with a variety of bitrates.  EditReady selects the correct bitrate automatically, based on your input file's resolution and framerate.  

For example, if your source is 1920x1080i60, the Low, Medium, and High settings correspond to DNxHD 100, 145 and 220, respectively.  For a 1920x1080p24 file, the bitrates are 36, 80 and 176.  

If you'd like to see a full chart of the bitrates used by DNxHD, take a look at the [DNxHD whitepaper](http://www.avid.com/static/resources/US/documents/dnxhd.pdf) from Avid.

### H.264 ###

If you'd like to use EditReady for generating files for distribution, or for creating very small proxy files, the H.264 setting is a good option.  This setting will automatically select a bitrate high enough to preserve the quality of your source footage without introducing substantial artifacts.

## Audio Formats ##
EditReady includes three options for audio formats - Uncompressed, AAC, and Passthrough.  Passthrough will preserve your source audio and is useful if you only wish to make changes to the video component of your file.

### Uncompressed (PCM) ###
Uncompressed PCM audio is the most common and interoperable method for working with audio on a computer.  This is the recommended option for any editing platform.

### AAC ###
AAC compressed audio is an ideal choice if you'll be creating H.264 compressed files for distribution. 

## Framerate ##
EditReady allows you to adjust the output framerate of your file during conversion.  **This setting adjusts the playback rate of your media**, it does not add or remove frames from your footage.  This setting is especially useful when creating "slow motion" footage with a source that shoots at 60 or 120 frames per second (or higher).  


# LUTs #

EditReady allows you to load LUTs ("Look up Table") which can apply color grading looks to your footage during conversion.  This can be very powerful if, for example, your camera records in the log space, but you wish to edit with a linear mapping.  EditReady supports LUTs in the 3DL and Cube formats.  If you attempt to load a LUT in an unsupported format, EditReady will prompt you to submit the file to Divergent Media, so we can evaluate adding support for that format in the future. 

If you save a new preset with a LUT, that LUT will be included in the preset.

Please note, LUTs require additional processing, and will slow the conversion process.  

# Troubleshooting

There are a few basic steps you can take when troubleshooting problems with EditReady.

## Errors during Conversion##

Does your file play within QuickTime player?  If QuickTime player reports that the file is unplayable, EditReady is unlikely to be able to convert it.  If QuickTime reports that you need additional components to play the file, you should download and install those to resolve the issue.

Some issues may be caused by invalid output destinations.  To test whether this is the case, try setting the "dest folder" option to your desktop.

## Submitting File Diagnostics ##

If you'd like additional help with a problematic file, you may submit some file diagnostics to Divergent Media.  Highlight a file (or multiple files) within the EditReady interface, and then select "submit selected clip" from the Help menu.  You'll be prompted to supply a brief explanation of the issue, as well as your email address.  This process submits the file header and additional diagnostic data, but does not send us the actual video content of your file.

We'll contact you via email after we investigate. 



# Other Resources #

If you need additional support using EditReady, please try the resources listed below.

## Support on the Web ##

<http://www.divergentmedia.com/support>

## Email support ##
<support@divergentmedia.com>

