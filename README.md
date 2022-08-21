# rc_rpi_fpv_video_stream
Streams NTSC / PAL @ 5.8GHz FPV video using a Raspberry Pi with the Eachine ROTG01 Pro FPV Receiver
![show_video](https://user-images.githubusercontent.com/18071111/185803224-71a5c7e5-ed19-4496-a582-b5f6663266b7.jpg)

# Required Libraries
Need to install opencv first

# Auto Start Script
```
mkdir /home/pi/.config/autostart
nano /home/pi/.config/autostart/show_video.desktop
```
`/home/pi/.config/autostart/show_video.desktop`
```
[Desktop Entry]
Type=Application
Name=Show_Video
Exec=/usr/bin/python3 /home/pi/rc_rpi_fpv_video_stream/show_video.py
```

