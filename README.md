dublinbikes
===========

Quick'n'dirty Class to query the Dublin Bikes API.

##What's happening here?
This class uses the same API that the dublinbikes website uses. It doesn't collect ALL the information, only information you ask it for.
This keeps the number of queries to the dublinbikes website to a minimum. We don't want them claiming we're abusing the site now, do we?

##Why bother?
Yes, I know there are other packages out there that do this, and more. I did this to prove to myself that I could.
My python skills are still rather basic (I'm sure you can tell from the code), so this was more an exercise in learning to python than anything else.

If you want something a little more extensive, take a look at PyBikes https://github.com/eskerda/PyBikes
Or you're free to contribute here...

##Basic usage
1. Update all Station details (stuff that doesn't change often, like location and name)
2. If thats all you want, then get the details for the station you're interested in.
3. If you want more (like total slots, available bikes, etc), then update the Status of the station you're interested in.
4. Now query those fields, they'll have information in them

##Example:
    >>> import DublinBikes
    >>> stations=DublinBikes.StationInfo()
    >>> stations.updateStations()
    >>> stations.getStationDetails(8)
    <DublinBikes.Station object at 0x7f8fd5aad310>
    >>> stations.getStationDetails(8).name
    'CUSTOM HOUSE QUAY'
    >>> stations.getStationDetails(8).open
    True
    >>> stations.getStationDetails(8).free
    >>> stations.updateStationStatus(8)
    >>> stations.getStationDetails(8).free
    10

