# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 10:23:15 2015

@author: sarradj
"""

from acoular import EigSpectra, MicGeom, MaskedTimeSamples
from acoular.h5files import H5FileBase, _get_h5file_class
from acoular.internal import digest
from traits.api import File, Property, Instance, cached_property, \
on_trait_change, property_depends_on
from os import path

import tables
import numpy
import h5py


class TimeSamplesAIAABenchmark(MaskedTimeSamples):
    
    @on_trait_change('basename')
    def load_data( self ):
        #""" open the .h5 file and set attributes
        #"""
        if not path.isfile(self.name):
            # no file there
            self.numsamples = 0
            self.numchannels = 0
            self.sample_freq = 0
            raise IOError("No such file: %s" % self.name)
        if self.h5f != None:
            try:
                self.h5f.close()
            except IOError:
                pass
        file = _get_h5file_class()
        self.h5f = file(self.name)
        self.data = self.h5f.root.MicrophoneData.microphoneDataPa
        self.sample_freq = self.data.get_attr('sampleRateHz')
        (self.numsamples_total, self.numchannels_total) = self.data.shape


class TriggerAIAABenchmark(MaskedTimeSamples):
    
    @on_trait_change('basename')
    def load_data( self ):
        #""" open the .h5 file and set attributes
        #"""
        if not path.isfile(self.name):
            # no file there
            self.numsamples = 0
            self.numchannels = 0
            self.sample_freq = 0
            raise IOError("No such file: %s" % self.name)
        if self.h5f != None:
            try:
                self.h5f.close()
            except IOError:
                pass
        file = _get_h5file_class()
        self.h5f = file(self.name)
        self.data = self.h5f.root.TachoData.tachoDataV
        self.sample_freq = self.data.get_attr('sampleRateHz')
        (self.numsamples_total, self.numchannels_total) = self.data.shape


class CsmAIAABenchmark(EigSpectra):
    """
    Class to use CSM that is stored in AIAA Benchmark HDF5 file
    """

    #: Full name of the .h5 file with data
    name = File(filter=['*.h5'], 
        desc="name of data file")

    #: Basename of the .h5 file with data, is set automatically
    basename = Property( depends_on = 'name', #filter=['*.h5'], 
        desc="basename of data file")
        
    #: number of channels
    numchannels = Property()

    #: HDF5 file object
    h5f = Instance(tables.File, transient = True)
    
    # internal identifier
    digest = Property( depends_on = ['basename'])

    @cached_property
    def _get_digest( self ):
        return digest(self)
    
    @cached_property
    def _get_basename( self ):
        return path.splitext(path.basename(self.name))[0]
    
    @on_trait_change('basename')
    def load_data( self ):
        #""" open the .h5 file and set attributes
        #"""
        if not path.isfile(self.name):
            # no file there
            raise IOError("No such file: %s" % self.name)
        if self.h5f != None:
            try:
                self.h5f.close()
            except IOError:
                pass
        self.h5f = tables.open_file(self.name, mode='r+')

    #@property_depends_on( 'block_size, ind_low, ind_high' )
    def _get_indices ( self ):
        try:
            return range(self.fftfreq().shape[0])#[ self.ind_low: self.ind_high ]
        except IndexError:
            return range(0)

    @property_depends_on('digest')
    def _get_numchannels ( self ):
        try:
            return self.h5f.root.MetaData.ArrayAttributes._f_getattr('microphoneCount')
        except IndexError:
            return range(0)

    @property_depends_on('digest')
    def _get_csm ( self ):
        """
        cross spectral matrix is loaded from file 
        """
        csmre = self.h5f.root.CsmData.csmReal[:].transpose((2,0,1))
        csmim = self.h5f.root.CsmData.csmImaginary[:].transpose((2,0,1))
        sign = self.h5f.root.CsmData._f_getattr('fftSign')
        return csmre + sign * 1j * csmim

    def fftfreq ( self ):
        """Return the Discrete Fourier Transform sample frequencies.
        
        Returns
        -------
        f : ndarray
            Array of length *block_size/2+1* containing the sample frequencies.
        """
        return numpy.array(self.h5f.root.CsmData.binCenterFrequenciesHz[:].flatten(), dtype=float)

class MicAIAABenchmark(MicGeom):

    #: Name of the .h5-file from wich to read the data.
    from_file = File(filter=['*.h5'],
        desc="name of the h5 file to import")

    #: Basename of the .xml-file, without the extension; is set automatically / readonly.
    basename = Property( depends_on = 'from_file',
        desc="basename of h5 file")

    @cached_property
    def _get_basename( self ):
        return path.splitext(path.basename(self.from_file))[0]

    @on_trait_change('basename')
    def import_mpos( self ):
        """
        Import the microphone positions from .h5 file.
        Called when :attr:`basename` changes.
        """
        if not path.isfile(self.from_file):
            # no file there
            raise IOError("No such file: %s" % self.from_file)
        #h5f = h5py.File(self.from_file,'r')
        h5f = tables.open_file(self.from_file,'r')
        
        self.mpos_tot = h5f.root.MetaData.ArrayAttributes.microphonePositionsM[:].swapaxes(0,1)
        h5f.close()




