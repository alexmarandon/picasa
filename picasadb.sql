select af.year, af.folder, af.file, a.name from albums_files af join albums a on a.id=af.id order by 4,1,2,3
select * from starred order by year, folder, file