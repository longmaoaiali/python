# 虚拟机安装 -- python构造网络数据包 
### 虚拟机安装指南  
  https://blog.csdn.net/qq_39530821/article/details/102985497  
  https://blog.csdn.net/weixin_44410537/article/details/100938963 
### root账户  
  sudo passwd root 设置root账户 密码 
### Ubuntu img下载 ：http://old-releases.ubuntu.com/releases/ 
### kernel源码下载 https://www.kernel.org/ 
### unbutu获得源码 并编译安装 
  sudo apt install linux-source 命令获取源码 或者官网直接下载源码 
  tar -cjf 解压 .tar.bz2 文件 
  在Ubuntu 18.04上编译Linux内核 https://blog.csdn.net/qq_36290650/article/details/83052315 
### ubuntu指定默认启动的内核   
  /etc/default/grub   GRUB_DEFAULT参数指定要启动的内核  或者开机是直接ESC 进入boot界面进行选择要启动的内核 
  参考 https://www.cnblogs.com/zoneofmine/p/13229347.html  
### kenrel编译报错 warning: the frame size of 1072 bytes is larger than 1024 bytes  
  参考 https://blog.csdn.net/sddf313/article/details/80415122 
### 指定内核启动时的 root_delay 参数 
  /etc/default/grub    GRUB_CMDLINE_LINUX_DEFAULT  可以添加 root_delay  
  eg : GRUB_CMDLINE_LINUX_DEFAULT="quiet rootdelay=90" 
### Ubuntu 更新内核出现 Missing Module  /dev/sda1 not exist  
  参考 https://blog.csdn.net/guiguzi5512407/article/details/48086073?utm_source=blogxgwz8 
### Ubuntu中 sudo  apt-get install 安装软件时 Could not get lock /var/lib/dpkg/lock解决方案 
  参考 https://blog.csdn.net/u011596455/article/details/60322568 
### Ubuntu 虚拟机与主机设置共享文件夹后 目录在 /mnt/hgfs/ 最后不知道为什么会失效 
### Insmod 加载cfg80211.ko wifi驱动以后,开始设置为monitor模式 启动monitor接口
  1、ifconfig wlan0 down  手动setting关闭WIFI  大坑否则后面的mode monitor设置失败   
  2、iwconfig wlan0 mode monitor    
  3. rfkill会报错使用 rfkill unblock wifi 参考 https://blog.csdn.net/weixin_39584758/article/details/80622675    
  4、ifconfig wlan0 up   
  5、ifconfig wlan0 0.0.0.0   
  6、iwconfig wlan0 channel [1,13] // 选择一个信道监听  
  
### 使用python + 无线网卡构造beacon数据包模拟AP热点，板卡能够扫到对应信道的beacon帧 即证明工作在该信道.(wifi国家频谱测试)
  开发进度如下：
    之前在win10上面进行发包测试，一直解决不了兼容性导致失败，所以使用虚拟机在ubuntu进行开发，kernel版本 4.9   WIFI模组使用 atbm6022/rtl8188GTV
    目前kernel 驱动移植已完成  运行python beacon发包脚本，在自己的电脑监听interface 已经能够捕获beacon数据帧。  
  目前遇见的问题是实际抓sniff包没有抓到beacon数据帧，并且使用手机也没有扫到 liuyutest 的热点。8188 驱动log日志已上传  
 
