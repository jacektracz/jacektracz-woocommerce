FROM php:7.0-apache

RUN \
      export http_proxy=http://proxy-chain.intel.com:911 && \
      export https_proxy=http://proxy-chain.intel.com:911 && \
      apt-get update && \
      apt-get install -y --force-yes \
                     apt-utils \
                     tar \
                     git \
                     git-core \
                     curl \
                     vim \
                     wget \
                     tmux  \
                     dialog \
                     net-tools \
                     build-essential \
                     lsb-release && \
    ( \
        wget -O mysql-apt-config.deb https://dev.mysql.com/get/mysql-apt-config_0.6.0-1_all.deb && \
        dpkg -i mysql-apt-config.deb && \
        echo deb http://repo.mysql.com/apt/debian/ jessie mysql-5.6 > /etc/apt/sources.list.d/mysql.list && \
        apt-get update && \
        apt-get install libmysqlclient-dev mysql-client-core-5.6 -y --force-yes \
    ) && \
    apt-get install -y --force-yes libldap2-dev libsasl2-dev libssl-dev libffi-dev && \
    apt-get install -y --force-yes libxml2-dev libxmlsec1-dev xmlsec1 swig pkg-config && \
    apt-get install -y --force-yes supervisor openssh-server && \
    apt-get install -y --force-yes libapache2-mod-authnz-external && \
	apt-get install -y --force-yes ldap-utils && \
    apt-get install -y --force-yes libldb-dev && \
    ln -s /usr/lib/x86_64-linux-gnu/libldap.so /usr/lib/libldap.so && \
    apt-get update && \
    apt-get install -y --force-yes libjpeg-dev && \
    apt-get install -y --force-yes libfreetype6-dev  && \
    apt-get install -y --force-yes zlib1g-dev && \
    apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
    && apt-get install -y pkg-config build-essential libmemcached-dev \
    && docker-php-ext-install -j$(nproc) iconv mcrypt pdo_mysql bcmath mbstring ldap \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd && \
    ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib && \
    ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib && \
    ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib && \
    ln -s /usr/include/x86_64-linux-gnu/openssl/opensslconf.h /usr/include/openssl && \
    ( \
        git clone https://github.com/php-memcached-dev/php-memcached.git && \
        cd php-memcached && \
        git checkout php7 && \
        phpize && \
        ./configure --disable-memcached-sasl && \
        make && \
        make install \
    ) && \
    docker-php-ext-enable memcached

COPY build.sh /var/www/
COPY php.ini /usr/local/etc/php/


RUN mkdir -p /var/run/sshd /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
# RUN dpkg-divert --local --rename --add /sbin/initctl
# RUN ln -s /bin/true /sbin/initctl

RUN service apache2 restart

CMD ["/usr/bin/supervisord"]