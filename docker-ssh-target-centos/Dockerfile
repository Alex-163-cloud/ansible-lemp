FROM quay.io/centos/centos:stream9

RUN dnf install -y openssh-server python3 sudo && \
    ssh-keygen -A && \
    echo 'root:root' | chpasswd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    dnf clean all

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
