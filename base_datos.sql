IF DB_ID('DatosAbiertosDB') IS NULL
    CREATE DATABASE DatosAbiertosDB;
GO
USE DatosAbiertosDB;
GO
IF OBJECT_ID('dbo.RegistrosAPI', 'U') IS NULL
CREATE TABLE dbo.RegistrosAPI (
    id INT IDENTITY(1,1) PRIMARY KEY,
    id_api NVARCHAR(100) NOT NULL UNIQUE,
    codigo_departamento NVARCHAR(10),
    departamento NVARCHAR(150),
    municipio NVARCHAR(150),
    tipo NVARCHAR(150),
    longitud NVARCHAR(50),
    latitud NVARCHAR(50),
    json_original NVARCHAR(MAX),
    fecha_captura DATETIME2 DEFAULT SYSDATETIME()
);
GO
