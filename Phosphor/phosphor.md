
#**1** Welcome to Phosphor#

##Welcome##

Phosphor is a new way of bringing animation and video to the web.  Starting with a standard QuickTime file, Phosphor creates crossplatform, web-standards compliant assets which can be played on desktop and mobile devices without plugins or even video decoding capabilities.  As long as a browser supports Javascript and the ability to show images, it can display Phosphor content.

Using Phosphor is simple and fun.  This manual will walk you through the basics, and will explore the situations in which Phosphor is most appropriate.

#**2** Getting Started#

##Interface Basics##

Upon launch, Phosphor displays a grid of previously accessed media, as well as an assortment of sample source material.  If you’re still in the process of getting familiar with Phosphor, the sample media gives you the opportunity to begin experimenting immediately.  You can use the “open” button (or select open from the file menu) to open any other QuickTime movie on your computer.

##Supported Media##
Phosphor can open most modern QuickTime files, including H.264 and ProRes.  The composition output by Phosphor will be the same resolution as your source movie, so a 1920x1080 source movie will result in a 1920x1080 output.  See chapter three for tips on how to prepare media for Phosphor.

##Exporting##
Once you’ve loaded your movie into Phosphor, you can begin the export process.  Click “Export movie” to reveal the export dialog.  From this menu, you can choose and export format, as well as some playback options.

###PNG Export###
PNG files are a good choice for movies which include an alpha layer.  The transparency will be preserved, allowing you to integrate your Phosphor composition with an existing background design on your website.

###JPG Export###
JPEG files are the best choice for most types of content, as the files are highly compressed and easily worked with.

###TIFF Export###
TIFF files are uncompressed, and are not suitable for use directly within a webpage.  Use this option if you’ll be compressing your files separately, using an external tool.

###Interactive Mode###
Interactive Mode will allow users to scrub back and forth through your composition using their mouse or a touch interface.  This is ideal for product demonstrations and 3d visualizations.  The compositions generated in interactive mode will be larger than non-interactive mode.

##The Export Process##
Once you’ve selected an export format, you can begin the export.  Phosphor will analyze your content and figure out the most efficient way to prepare it for delivery.  With a longer movie, this can be time consuming.  

You can work with additional movies within Phosphor during an export - simply select “open” from the “file” menu to begin working on another composition.

#**3** Optimizing Media for Phosphor#

##Types of Source Material##
Phosphor works best with short movies which do not contain a lot of visual noise.  Visual noise includes things like static on a television screen, a snow storm, or ripping water.  

##Framerate##
Video typically runs at 30 frames per second.  In many cases, you can achieve fluid motion with a lower framerate, and thus benefit from greater efficiency.  Using your video editing software to convert your media to 15 frames per second will substantially reduce the size of your composition.

##Duration##
Videos longer than approximately 30 seconds will generally result in large compositions, which may not work well on mobile devices or devices with limited memory.  For these types of content, a more traditional video embed is more appropriate.

##Compressing Phosphor Compositions##
Phosphor outputs standard image files, in either JPG, PNG or TIFF format.  These files can be modified with traditional image manipulation tools.  For example, the free [ImageOptim](http://imageoptim.com) application can often substantially reduce the size of PNG and JPG files, without an additional reduction in quality.

When editing Phosphor images, it’s important that you don’t resize the images.  If the overall resolution of the file changes, the Phosphor library will no longer be able to display the composition.

#**4** Troubleshooting#
