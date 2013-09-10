#Dealing with Codec Conflicts#

Many Mac users have accumulated a variety of QuickTime components or "plugins" to deal with different types of video.  As Mac OS X has been updated over the years, some of these codecs have not kept pace with the changes and can now cause application instability or performance issues in other applications.

ClipWrap will automatically detect codecs that are known to cause crashes or video glitches and will alert you with a popup.

![Codec Conflict Alert](misc/images/codecConflict.png)

If you receive this alert, you should check your system for conflicting codecs.  Via Finder, select the "Go" menu and then "Go To Folder."  Enter `/Library/QuickTime` and press return.  Look for any of the codecs listed below.  If you find them, we recommend dragging them to your desktop or to the trash.  In most cases, they're no longer necessary on Mac OS X.  If you do need these codecs, make sure you're using the newest version from the codec's vendor.

Codecs which are known to cause instability:

* Flip4Mac
* 3vix
* Xvid
* DiVX
* Xiph
* FFusion

If you're uncomfortable doing these sorts of system changes yourself, you can use [SandboxCleaner](https://itunes.apple.com/us/app/sandboxcleaner/id597424370?mt=12) from Boinx Software.  Apple also has a [support page](http://support.apple.com/kb/HT5448?viewlocale=en_US&locale=en_US) with information on removing conflicting codecs.


