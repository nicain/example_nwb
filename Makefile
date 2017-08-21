TAG = 'neurodatawithoutborders/pynwb:feature-table_writer_dataset23'

docker:
		docker build --tag $(TAG)  -f Dockerfile .

run:
		docker run -v `pwd`:/work_dir -it $(TAG) bash -c 'cd /work_dir; python generate_v2_file.py'

example:
		jupyter notebook example.ipynb

