select af.year, af.folder, af.file, a.name from albums_files af join albums a on a.id=af.id order by 4,1,2,3
select * from starred order by year, folder, file

select ff.year, ff.folder, ff.file, c.name from faces_files af join contacts c on c.id=ff.id order by 4,1,2,3