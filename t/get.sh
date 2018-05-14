
#!/bin/sh

for file in {1200..1400}
do
	wget --wait=5 -O $file.png "https://webmail.iitg.ac.in/plugins/captcha/backends/watercap/image_generator.php?sq="$file
done