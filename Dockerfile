FROM ubuntu

WORKDIR /opt/AchievementAnnouncer
RUN echo "Europe/Berlin" > /etc/timezone
RUN ln -sf /usr/share/zoneinfo/Europe/Berlin /etc/localtime
RUN apt-get update -y && apt-get install -y apt-utils tzdata python3 python3-pip
RUN dpkg-reconfigure -f noninteractive tzdata
RUN pip3 install requests tweepy 
ADD AchievementAnnouncer /opt/AchievementAnnouncer
RUN chmod +x /opt/AchievementAnnouncer/AchievementAnnouncer.py
# 23 Stunden CoolDown Zeit
CMD while true; do cd /opt/AchievementAnnouncer && /opt/AchievementAnnouncer/tarry -until=22:00:00 > /dev/null 2>&1 && ./AchievementAnnouncer.py && sleep 82800; done