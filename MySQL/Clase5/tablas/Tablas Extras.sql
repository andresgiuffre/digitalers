-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: prueba
-- ------------------------------------------------------
-- Server version	5.5.5-10.1.38-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `empleados`
--

DROP TABLE IF EXISTS `empleados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `empleados` (
  `IdEmpleado` int(11) DEFAULT NULL,
  `Apellidos` text,
  `Nombre` text,
  `Cargo` text,
  `FechaNacimiento` date DEFAULT NULL,
  `Pais` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empleados`
--

LOCK TABLES `empleados` WRITE;
/*!40000 ALTER TABLE `empleados` DISABLE KEYS */;
INSERT INTO `empleados` VALUES (1,'Davolio','Nancy','Representante de ventas','1968-12-08','EE.UU.'),(2,'Fuller','Andrew','Vicepresidente comercial','1952-02-19','EE.UU.'),(3,'Leverling','Janet','Representante de ventas','1963-08-30','EE.UU.'),(4,'Peacock','Margaret','Representante de ventas','1958-09-19','EE.UU.'),(5,'Buchanan','Steven','Gerente de ventas','1955-03-04','Reino Unido'),(6,'Suyama','Michael','Representante de ventas','1963-07-02','Reino Unido'),(7,'King','Robert','Representante de ventas','1960-05-29','Reino Unido'),(8,'Callahan','Laura','Coordinador ventas interno','1958-01-09','EE.UU.'),(9,'Dodsworth','Anne','Representante de ventas','1969-07-02','Reino Unido');
/*!40000 ALTER TABLE `empleados` ENABLE KEYS */;
UNLOCK TABLES;


--
-- Table structure for table `productos_neptuno`
--

DROP TABLE IF EXISTS `productos_neptuno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `productos_neptuno` (
  `IdProducto` int(11) DEFAULT NULL,
  `NombreProducto` text,
  `NombreContacto` text,
  `NombreCategoria` text,
  `PrecioUnidad` double DEFAULT NULL,
  `Suspendido` int(11) DEFAULT NULL,
  `IdProveedor` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos_neptuno`
--

LOCK TABLES `productos_neptuno` WRITE;
/*!40000 ALTER TABLE `productos_neptuno` DISABLE KEYS */;
INSERT INTO `productos_neptuno` VALUES (1,'Te Dharamsala','Charlotte Cooper','Bebidas',18,0,1),(2,'Cerveza tibetana Barley','Charlotte Cooper','Bebidas',19,0,1),(3,'Sirope de regaliz','Charlotte Cooper','Condimentos',10,0,1),(4,'Especias Cajun del chef Anton','Shelley Burke','Condimentos',22,0,2),(5,'Mezcla Gumbo del chef Anton','Shelley Burke','Condimentos',21.35,1,2),(6,'Mermelada de grosellas de la abuela','Regina Murphy','Condimentos',25,0,3),(7,'Peras secas organicas del tio Bob','Regina Murphy','Frutas/Verduras',30,0,3),(8,'Salsa de arandanos Northwoods','Regina Murphy','Condimentos',40,0,3),(9,'Buey Mishi Kobe','Yoshi Nagase','Carnes',97,1,4),(10,'Pez espada','Yoshi Nagase','Pescado/Marisco',31,0,4),(11,'Queso Cabrales','Antonio del Valle Saavedra ','Lacteos',21,0,5),(12,'Queso Manchego La Pastora','Antonio del Valle Saavedra ','Lacteos',38,0,5),(13,'Algas Konbu','Mayumi Ohno','Pescado/Marisco',6,0,6),(14,'Cuajada de judias','Mayumi Ohno','Frutas/Verduras',23.25,0,6),(15,'Salsa de soja baja en sodio','Mayumi Ohno','Condimentos',15.5,0,6),(16,'Postre de merengue Pavlova','Ian Devling','Reposteria',17.45,0,7),(17,'Cordero Alice Springs','Ian Devling','Carnes',39,1,7),(18,'Langostinos tigre Carnarvon','Ian Devling','Pescado/Marisco',62.5,0,7),(19,'Pastas de te de chocolate','Peter Wilson','Reposteria',9.2,0,8),(20,'Mermelada de Sir Rodney\'s','Peter Wilson','Reposteria',81,0,8),(21,'Bollos de Sir Rodney\'s','Peter Wilson','Reposteria',10,0,8),(22,'Pan de centeno crujiente estilo Gustaf\'s','Lars Peterson','Granos/Cereales',21,0,9),(23,'Pan fino','Lars Peterson','Granos/Cereales',9,0,9),(24,'Refresco Guarana Fantastica','Carlos Diaz','Bebidas',4.5,1,10),(25,'Crema de chocolate y nueces NuNuCa','Petra Winkler','Reposteria',14,0,11),(26,'Ositos de goma Gumbar','Petra Winkler','Reposteria',31.23,0,11),(27,'Chocolate Schoggi','Petra Winkler','Reposteria',43.9,0,11),(28,'Col fermentada Rossle','Martin Bein','Frutas/Verduras',45.6,1,12),(29,'Salchicha Thuringer','Martin Bein','Carnes',123.79,1,12),(30,'Arenque blanco del noroeste','Sven Petersen','Pescado/Marisco',25.89,0,13),(31,'Queso gorgonzola Telino','Elio Rossi','Lacteos',12.5,0,14),(32,'Queso Mascarpone Fabioli','Elio Rossi','Lacteos',32,0,14),(33,'Queso de cabra','Beate Vileid','Lacteos',2.5,0,15),(34,'Cerveza Sasquatch','Cheryl Saylor','Bebidas',14,0,16),(35,'Cerveza negra Steeleye','Cheryl Saylor','Bebidas',18,0,16),(36,'Escabeche de arenque','Michael Bjorn','Pescado/Marisco',19,0,17),(37,'Salmon ahumado Gravad','Michael Bjorn','Pescado/Marisco',26,0,17),(38,'Vino Cote de Blaye','Guylene Nodier','Bebidas',263.5,0,18),(39,'Licor verde Chartreuse','Guylene Nodier','Bebidas',18,0,18),(40,'Carne de cangrejo de Boston','Robb Merchant','Pescado/Marisco',18.4,0,19),(41,'Crema de almejas estilo Nueva Inglaterra','Robb Merchant','Pescado/Marisco',9.65,0,19),(42,'Tallarines de Singapur','Chandra Leka','Granos/Cereales',14,1,20),(43,'Cafe de Malasia','Chandra Leka','Bebidas',46,0,20),(44,'Azucar negra Malacca','Chandra Leka','Condimentos',19.45,0,20),(45,'Arenque ahumado','Niels Petersen','Pescado/Marisco',9.5,0,21),(46,'Arenque salado','Niels Petersen','Pescado/Marisco',12,0,21),(47,'Galletas Zaanse','Dirk Luchte','Reposteria',9.5,0,22),(48,'Chocolate holandes','Dirk Luchte','Reposteria',12.75,0,22),(49,'Regaliz','Anne Heikkonen','Reposteria',20,0,23),(50,'Chocolate blanco','Anne Heikkonen','Reposteria',16.25,0,23),(51,'Manzanas secas Manjimup','Wendy Mackenzie','Frutas/Verduras',53,0,24),(52,'Cereales para Filo','Wendy Mackenzie','Granos/Cereales',7,0,24),(53,'Empanada de carne','Wendy Mackenzie','Carnes',32.8,1,24),(54,'Empanada de cerdo','Jean-Guy Lauzon','Carnes',7.45,0,25),(55,'Pate chino','Jean-Guy Lauzon','Carnes',24,0,25),(56,'Gnocchi de la abuela Alicia','Giovanni Giudici','Granos/Cereales',38,0,26),(57,'Raviolis Angelo','Giovanni Giudici','Granos/Cereales',19.5,0,26),(58,'Caracoles de Borgona','Marie Delamare','Pescado/Marisco',13.25,0,27),(59,'Raclet de queso Courdavault','Eliane Noz','Lacteos',55,0,28),(60,'Camembert Pierrot','Eliane Noz','Lacteos',34,0,28),(61,'Sirope de arce','Chantal Goulet','Condimentos',28.5,0,29),(62,'Tarta de azucar','Chantal Goulet','Reposteria',49.3,0,29),(63,'Sandwich de vegetales','Ian Devling','Condimentos',43.9,0,7),(64,'Bollos de pan de Wimmer','Martin Bein','Granos/Cereales',33.25,0,12),(65,'Salsa de pimiento picante de Luisiana','Shelley Burke','Condimentos',21.05,0,2),(66,'Especias picantes de Luisiana','Shelley Burke','Condimentos',17,0,2),(67,'Cerveza Laughing Lumberjack','Cheryl Saylor','Bebidas',14,0,16),(68,'Barras de pan de Escocia','Peter Wilson','Reposteria',12.5,0,8),(69,'Queso Gudbrandsdals','Beate Vileid','Lacteos',36,0,15),(70,'Cerveza Outback','Ian Devling','Bebidas',15,0,7),(71,'Crema de queso Flotemys','Beate Vileid','Lacteos',21.5,0,15),(72,'Queso Mozzarella Giovanni','Elio Rossi','Lacteos',34.8,0,14),(73,'Caviar rojo','Michael Bjorn','Pescado/Marisco',15,0,17),(74,'Queso de soja Longlife','Yoshi Nagase','Frutas/Verduras',10,0,4),(75,'Cerveza Klosterbier Rhonbrau','Martin Bein','Bebidas',7.75,0,12),(76,'Licor Cloudberry','Anne Heikkonen','Bebidas',18,0,23),(77,'Salsa verde original Frankfurter','Martin Bein','Condimentos',13,0,12);
/*!40000 ALTER TABLE `productos_neptuno` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedores`
--

DROP TABLE IF EXISTS `proveedores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `proveedores` (
  `IdProveedor` int(11) DEFAULT NULL,
  `NombreContacto` text,
  `CargoContacto` text,
  `Direccion` text,
  `Ciudad` text,
  `Region` text,
  `Pais` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedores`
--

LOCK TABLES `proveedores` WRITE;
/*!40000 ALTER TABLE `proveedores` DISABLE KEYS */;
INSERT INTO `proveedores` VALUES (1,'Charlotte Cooper','Gerente de compras','49 Gilbert St.','Londres','Londres','Reino Unido'),(2,'Shelley Burke','Administrador de pedidos','P.O. Box 78934','New Orleans','','Estados Unidos'),(3,'Regina Murphy','Representante de ventas','707 Oxford Rd.','Ann Arbor','','Estados Unidos'),(4,'Yoshi Nagase','Gerente de marketing','98 Sekimai Musashino-shi','Tokyo','','Japon'),(5,'Carlos Garcia','Gerente Regional',' Cerrito 345','Buenos Aires','','Argentina'),(6,'Mayumi Ohno','Representante de marketing','92 Setsuko Chuo-ku','Osaka','','Japon'),(7,'Ian Devling','Gerente de marketing','74 Rose St.','Melbourne','','Australia'),(8,'Peter Wilson','Representante de ventas','29 King\'s Way','Manchester','RU','Reino Unido'),(9,'Lars Peterson','Agente de ventas','Kaloadagatan 13','Goteborg','','Suecia'),(10,'Carlos Diaz','Gerente de marketing','Av. das Americanas 12890','Sao Paulo','BR','Brasil'),(11,'Petra Winkler','Gerente de ventas','Tiergartenstrabe 5','Berlin','','Alemania'),(12,'Martin Bein','Ger. marketing internacional','Bogenallee 51','Frankfurt','','Alemania'),(13,'Sven Petersen','Coordinador de mercados','Frahmredder 112a','Cuxhaven','','Alemania'),(15,'Beate Vileid','Gerente de marketing','Hatlevegen 5','Sandvika','','Noruega'),(16,'Cheryl Saylor','Repr. de cuentas regional','3400 8th Avenue','Bend','USA','Estados Unidos'),(17,'Michael Bjorn','Representante de ventas','Brovallavagen 231','Stockholm','','Suecia'),(18,'Guylene Nodier','Gerente de ventas','203 Rue des Francs Bourgeois','Paris','','Francia'),(19,'Robb Merchant','Agente de cuentas al por mayor','2100 Paul Revere Blvd.','Boston','USA','Estados Unidos'),(20,'Chandra Leka','Propietario','471 Serangoon Loop Suite 402','Singapore','','Singapur'),(22,'Dirk Luchte','Gerente de contabilidad','Rijnweg 22','Zaandam','','Holanda'),(23,'Anne Heikkonen','Gerente de produccion','Valtakatu 12','Lappeenranta','','Finlandia'),(24,'Wendy Mackenzie','Representante de ventas','170 Prince Edward Parade','Sydney','','Australia'),(25,'Jean-Guy Lauzon','Gerente de marketing','2960 Rue St. Laurent','Montreal','','Canada'),(26,'Giovanni Giudici','Administrador de pedidos','Via dei Gelsomini 153','Salerno','','Italia'),(27,'Marie Delamare','Gerente de ventas','22 Rue Voiron','Montceau','','Francia'),(28,'Eliane Noz','Representante de ventas','3 Rue des Alpes Bat B','Annecy','','Francia'),(29,'Chantal Goulet','Gerente de contabilidad','148 rue Chasseur','Ste-Hyacinthe','','Canada');
/*!40000 ALTER TABLE `proveedores` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-31 19:33:15
