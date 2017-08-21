from datetime import datetime
import numpy as np
import pandas as pd

from pynwb import get_class, load_namespaces
from pynwb import NWBFile
from form.backends.hdf5 import HDF5IO
from pynwb import get_build_manager

from allensdk.core.brain_observatory_cache import BrainObservatoryCache
from allensdk.brain_observatory import stimulus_info as si

oeid = 501474098
ns_path = "alleninstitute.namespace.yaml"
load_namespaces(ns_path)
Table = get_class('Table', 'alleninstitute')


boc = BrainObservatoryCache()
nwb_dataset = boc.get_ophys_experiment_data(oeid)
stimulus_epoch_table = nwb_dataset.get_stimulus_epoch_table()

fs = Table(stimulus_epoch_table=stimulus_epoch_table.to_dict(orient='list'),
           name='stimulus_epoch',
           source='acquisition',
           unit='second',
           help='None')


f = NWBFile(file_name='tmp.nwb',
            source='me',
            session_description='my first synthetic recording',
            identifier='EXAMPLE_ID',
            session_start_time=datetime.now(),
            experimenter='Dr. Bilbo Baggins',
            lab='Bag End Labatory',
            institution='University of Middle Earth at the Shire',
            experiment_description='empty',
            session_id='LONELYMTN')

f.add_stimulus(fs)

manager = get_build_manager()
io = HDF5IO('501474098_v2.nwb', manager, mode='w')
io.write(f)
io.close()
print 'OK'
