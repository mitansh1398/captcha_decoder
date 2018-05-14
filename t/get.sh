
#!/bin/sh

for file in {1000..1100}
do
	wget --wait=5 -O $file.png "https://webmail.iitg.ac.in/plugins/captcha/backends/watercap/image_generator.php?sq="$file
done