#!/usr/bin/env python 
import urllib2
import json
import time
from bs4 import BeautifulSoup

class Station(object):
    """Object containing all details and status of a Dublin Bikes Station"""
    def __init__(self,number,address,name,open,lattitude,longitude,bonus,available=None,free=None,total=None,ticket=None,updated=0,connected=None):
        self.number=number
        self.address=address
        self.name=name
        self.open=open
        self.lattitude=lattitude
        self.longitude=longitude
        self.bonus=bonus
        self.available=available
        self.free=free
        self.total=total
        self.ticket=ticket
        self.updated=updated
        self.connected=connected

    def updateStatus(self,available,free,total,open,ticket,updated,connected):
        self.available=available
        self.free=free
        self.total=total
        self.open=open
        self.ticket=ticket
        self.updated=updated
        self.connected=connected

class StationInfo(object):
    """Information on Dublin Bike stations"""
    def __init__(self):
        self.stations={}
        self.lastdetailupdate=0

    def updateStations(self):
        """Fetch an up-to-date list of stations with their specifics"""
        response = urllib2.urlopen('http://www.dublinbikes.ie/service/carto')
        soup = BeautifulSoup(response.read())

        for marker in soup.markers.find_all('marker'):
            station=Station(
                    int(marker['number']),
                    marker['address'],
                    marker['name'],
                    bool(marker['open']),
                    float(marker['lat']),
                    float(marker['lng']),
                    int(marker['bonus'])
                    )
            self.stations[station.number]=station
        self.lastdetailupdate=int(time.time())

    def getStationDetails(self,number):
        return self.stations[number]

    def getStationStatus(self,number,age=60):
        """Return the current Status of a Station.
        If the status is over <age> seconds old, refresh and then return"""
        pass

    def getLastDetailUpdate(self):
        return self.lastdetailupdate

    def updateStationStatus(self,number):
        """Fetch the current status of the given station number"""
        url="http://www.dublinbikes.ie/service/stationdetails/dublin/%s" % (number,)
        response = urllib2.urlopen(url)

        soup = BeautifulSoup(response.read())
        
        self.stations[number].updateStatus(
                int(soup.available.string),
                int(soup.free.string),
                int(soup.total.string),
                int(soup.ticket.string),
                int(soup.open.string),
                int(soup.updated.string),
                bool(soup.connected.string)
                )

