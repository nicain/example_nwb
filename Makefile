TAG = 'neurodatawithoutborders/pynwb:feature-table_writer_dataset23'
.DEFAULT_GOAL := all

clean:
		rm -f alleninstitute.extensions.yaml
		rm -f alleninstitute.namespace.yaml
		rm -f 501474098_v2.nwb
		rm -f epoch_bar.png

docker:
		docker build --tag $(TAG)  -f Dockerfile .

extension:
		docker run -v `pwd`:/work_dir -it $(TAG) bash -c 'cd /work_dir; python create_table_extension.py'

run:
		docker run -v `pwd`:/work_dir -it $(TAG) bash -c 'cd /work_dir; python generate_v2_file.py'

example:
		jupyter notebook example.ipynb

all: clean docker extension run example