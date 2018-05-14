
#!/bin/sh

for file in {100..500}
do
	wget --wait=1 -O $file.png "https://webmail.iitg.ac.in/plugins/captcha/backends/watercap/image_generator.php?sq="$file
done