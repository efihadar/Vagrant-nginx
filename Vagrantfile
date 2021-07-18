# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure(2) do |config|
        config.vm.box = "centos/7"
        config.vm.box_check_update = true
        config.vm.hostname = "root"
	config.vm.network :forwarded_port, guest: 80, host: 80, auto_correct: true
        config.vm.network :forwarded_port, guest: 443, host: 443, auto_correct: true
        config.vm.provision "file", source: "nginx.conf", destination: "~/"
        config.vm.provision "file", source: "server.py", destination: "~/"
        config.vm.provision "shell", path: "bootstrap.sh"
 	
end