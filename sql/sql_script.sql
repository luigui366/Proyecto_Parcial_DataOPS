use Kaggle
go
--En caso no exista la tabla Netflix
if not exists (
	select * from SYS.TABLES
	where object_id = OBJECT_ID(N'dbo.netflix') and type = 'U')
create table netflix(
	show_id varchar(max),
	type_show varchar(max),
	title varchar(max),
	director varchar(max),
	cast_show varchar(max),
	country varchar(max),
	date_added varchar(max),
	release_year varchar(max),
	ratingg varchar(max),
	duration varchar(max),
	listed_in varchar(max),
	description_show varchar(max)
	)

--Si la tabla ya existe, entonces la trunco
TRUNCATE TABLE dbo.netflix

--Ingestar datos
bulk insert dbo.netflix
from 'C:\Users\Luigui\Desktop\CERTUS\3.DataOPS\proyecto_parcial\python\dataset\netflix_titles.csv'
with
(
	firstrow = 2, --Empieza en la 2da fila, ya que la 1ra en la cabecera
	fieldterminator = ',', --Indicamos separador de columnas
	rowterminator = '0x0a' --Hace referencia a un salto de linea
)

GO


--select * from netflix