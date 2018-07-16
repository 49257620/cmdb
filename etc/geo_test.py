# encoding: utf-8
# Author: LW


import geoip2.database


def get_city_location(ips):
    city_list = []
    with geoip2.database.Reader('GeoLite2-City.mmdb') as reader:
        for ip in ips:
            city = {}
            try:
                response = reader.city(ip)
                city['ip'] = ip
                city['city'] = response.city.names.get('zh-CN', response.city.names.get('en'))
                city['latitude'] = response.location.latitude
                city['longitude'] = response.location.longitude
                city_list.append(city)
            except BaseException as e:
                print(ip, e)

    return city_list


if __name__ == '__main__':
    ip_list = ['61.159.140.123',
               '66.249.64.5',
               '66.249.64.10',
               '123.125.68.30',
               '123.125.68.20',
               '111.85.25.71',
               '218.200.66.201',
               '10.35.1.82',
               '113.95.36.30',
               '123.125.68.37',
               '218.200.66.204',
               '66.249.64.15',
               '218.200.66.198',
               '37.58.100.88',
               '60.223.255.219',
               '218.200.66.196',
               '218.200.66.205',
               '123.139.94.147',
               '153.0.7.250',
               '218.200.66.199',
               '171.106.90.131',
               '37.58.100.73',
               '110.184.24.134',
               '218.200.66.197',
               '218.200.66.202',
               '123.125.68.36',
               '123.125.68.21',
               '123.139.215.156',
               '163.125.48.92',
               '220.172.215.69',
               '123.125.68.14',
               ]
    ll = get_city_location(ip_list)
    for x in ll:
        print(x)
