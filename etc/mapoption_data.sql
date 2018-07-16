show tables;


select * from asset_resource;

select * from asset_host;


select * from user_user;


select * from django_migrations;

select * from django_session;

select * from django_content_type;


select DISTINCT IP from webanalysis_accesslog a where not exists( select * from webanalysis_accesslogips b where a.ip = b.ip  );


select * from webanalysis_accesslogips;

delete from webanalysis_accesslogips;


select * from webanalysis_accesslog ;

#61.159.140.123
insert into webanalysis_accesslogips (ip,city,latitude,longitude) values('61.159.140.123','beijing',0,0);



SELECT * FROM webanalysis_accesslogips WHERE IP ='221.176.5.153';




select a.CITY,a.latitude,a.longitude,COUNT(b.*) from webanalysis_accesslogips a ,webanalysis_accesslog b
where a.city != 'N/A'
and a.ip = b.ip
and b.id = 18
GROUP BY a.CITY,a.latitude,a.longitude;


select CITY,COUNT(*) from webanalysis_accesslogips where city != 'N/A' GROUP BY CITY ;


select b.CITY,b.latitude,b.longitude,count(a.id) from webanalysis_accesslog a
 inner JOIN webanalysis_accesslogips b on a.ip = b.ip and b.city !='N/A'
where a.file_id=18
GROUP BY b.CITY,b.latitude,b.longitude;



select a.CITY,a.latitude,a.longitude ,count(b.id)
from webanalysis_accesslogips a
inner join webanalysis_accesslog b on a.ip = b.ip and b.file_id=18
where a.city !='N/A'
GROUP BY a.CITY,a.latitude,a.longitude;






select a.CITY,a.latitude,a.longitude,count(b.id)
from webanalysis_accesslogips a ,webanalysis_accesslog b
where a.city !='N/A'
and a.ip = b.ip
and b.file_id=18
GROUP BY a.CITY,a.latitude,a.longitude;


select a.CITY,a.latitude,a.longitude,count(b.id)
from webanalysis_accesslog b,webanalysis_accesslogips a
where b.file_id=18
and a.city !='N/A'
and b.ip = a.ip
GROUP BY a.CITY,a.latitude,a.longitude;



