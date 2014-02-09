import xbmc, xbmcgui, xbmcaddon, urllib2, json, xbmcplugin, sys

def makeLink(params, baseUrl=sys.argv[0]):
    """
    Build a link with the specified base URL and parameters
    
    Parameters:
    params: the params to be added to the URL
    BaseURL: the base URL, sys.argv[0] by default
    """
    return baseUrl + '?' +urllib.urlencode(dict([k.encode('utf-8'),unicode(v).encode('utf-8')] for k,v in params.items()))


def addMenuItem(caption, link, icon=None, thumbnail=None, folder=False):
    """
    Add a menu item to the xbmc GUI
    
    Parameters:
    caption: the caption for the menu item
    icon: the icon for the menu item, displayed if the thumbnail is not accessible
    thumbail: the thumbnail for the menu item
    link: the link for the menu item
    folder: True if the menu item is a folder, false if it is a terminal menu item
    
    Returns True if the item is successfully added, False otherwise
    """
    listItem = xbmcgui.ListItem(unicode(caption), iconImage=icon, thumbnailImage=thumbnail)
    listItem.setInfo(type="Video", infoLabels={ "Title": caption })
    return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=link, listitem=listItem, isFolder=folder)


def endListing():
    """
    Signals the end of the menu listing
    """
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


#url = 'https://interface.iptv.beeline.ru/PHP/manifest3a.php?json'
url = 'http://msilivonik.com/iptv.json'
response = urllib2.urlopen(url)
if response and response.getcode() == 200:
	j = json.loads(response.read())
	channels = j['Channels']
	for channel in channels:
		icon = 'https://interface.iptv.beeline.ru/PHP/images/logos_224x158_id/' + str(channel['StationId']) + '.png'
		addMenuItem(channel['name'], channel['stream'], icon, icon)
	endListing()


