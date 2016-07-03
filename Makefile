download_data:
	curl -L `yadisk-direct https://yadi.sk/d/SqsWFcpds9rTL` -o data.tar.gz
	md5sum --status -c data.tar.gz.md5 || echo File verification failed!

extract_data:
	mkdir data
	tar -axf data.tar.gz -C data
