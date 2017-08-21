from pynwb import NWBNamespaceBuilder, NWBGroupSpec, NWBDatasetSpec, NWBAttributeSpec


ns_path = "alleninstitute.namespace.yaml"
ext_source = "alleninstitute.extensions.yaml"


nwb_ds = NWBDatasetSpec(doc='dataset_doc',
                        dtype=[{'label': 'stimulus', 'dtype': 'str'},
                               {'label': 'start', 'dtype': 'int'},
                               {'label': 'end', 'dtype': 'int'}],
                        name='stimulus_epoch_table')

ns_builder = NWBNamespaceBuilder('Allen Institute extensions', "alleninstitute")
ext = NWBGroupSpec('Stimulus epoch table',
                   datasets=[nwb_ds],
                   neurodata_type_inc='NWBContainer',
                   neurodata_type_def='Table',
                   attributes=[NWBAttributeSpec(name='help',
                                                dtype='str',
                                                doc='no help for you')])

ns_builder.add_spec(ext_source, ext)
ns_builder.export(ns_path)